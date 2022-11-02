from django.shortcuts import render
from urllib3 import HTTPResponse
from .models import *
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
import pandas as pd
from .utils import *


def index(request):
    sales_df = None
    positions_df = None
    merged_df = None
    df = None
    chart = None

    form = SaleSearchForm(request.POST or None)
    if request.method == "POST":
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        sale_qs =Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)

        if len(sale_qs) > 0:
            sales_df = pd.DataFrame(sale_qs.values())                                           #Sale_DF
            sales_df['customer_id'] = sales_df['customer_id'].apply(get_customer_from_id)       #Getting customer from ID
            sales_df['saleman_id'] = sales_df['saleman_id'].apply(get_salesman_from_id)         #Getting saleman from ID
            sales_df['created'] = sales_df['created'].apply(lambda x: x.strftime('%Y-%m-%d'))   #changing the format
            sales_df['updated'] = sales_df['updated'].apply(lambda x: x.strftime('%Y-%m-%d'))   #changing the format
            sales_df.rename({'customer_id': 'customer', 'saleman_id': 'salesman', 'id': 'sales_id'}, axis=1, inplace=True) #renaming

            positions_data=[]
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'positions_id': pos.id,
                        'porduct': pos.product.name,
                        'quantity':pos.quantity,
                        'price':pos.price,
                        'sales_id': pos.get_sales_id()
                    }
                    positions_data.append(obj)
            positions_df = pd.DataFrame(positions_data)                                 #Positions_DF
            merged_df = pd.merge(sales_df, positions_df, on='sales_id')                 #Merged_DF
            df = merged_df.groupby('transaction_id', as_index=False)['price'].agg('sum')
            chart = get_chart(chart_type, df, labels=df['transaction_id'].values)

            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
            merged_df = merged_df.to_html()
            df = df.to_html()                                                           #DF (for all charts)


        else:
            print("No Data Found")

    context = {
        'form':form, 
        'sales_df':sales_df, 
        'positions_df':positions_df, 
        'merged_df':merged_df,
        'df':df,
        'chart':chart,
        }
    return render(request, 'index.html', context)

# fbv
def list(request):
    list_objects = Sale.objects.all()
    csv = CSV.objects.all()
    return render(request, 'index.html', {'list_objects':list_objects, 'CSV':csv})

def detail(request, pk):
    obj = Sale.objects.get(id=pk)
    print(obj)
    return render(request, 'detail.html', {'obj':obj})

#cbv
class SaleListView(ListView):
    model = Sale
    template_name = 'sale.html'
    # context_object_name= 'qs'
    
class SaleDetailView(DetailView):
    model = Sale
    template_name = 'detail.html'
    context_object_name= 'obj'
