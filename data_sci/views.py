from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_index_view(request):
    '''This function render index page of Data_sci views'''

    return HttpResponse('Welcome to 6322775122 Ploypichcha Anupatanun views!')

def data_sci_item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'data_sci/index.html',context = context_data)