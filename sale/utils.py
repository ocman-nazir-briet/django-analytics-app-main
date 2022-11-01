import uuid
from profiles.models import *
from shop.models import *
import matplotlib.pyplot as plt
from io import BytesIO
import base64
def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username

def get_customer_from_id(val):
    customer = myUser.objects.get(id=val)
    return customer

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    if chart_type == '#1':
        print("Bar Chart")
        plt.bar(data['transaction_id'], data['price'])
    elif chart_type == '#2':
        print("Pie Chart")
        labels = kwargs.get('labels')
        plt.pie(data=data, x='price', labels=labels)
    elif chart_type == '#3':
        print("Line Chart")
        plt.plot(data['transaction_id'], data['price'])
    else:
        print("No Chart Type")
    plt.tight_layout
    chart = get_graph()
    return chart
    
