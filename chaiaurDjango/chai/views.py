from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm


# Create your views here.
def all_chai(request):
    chais= ChaiVariety.objects.all().order_by('-date_added')
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai= get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})


def chai_store_view(request):
    return render(request, 'chai/chai_stores.html')


def chai_store_view(request):
    stores= None
    if request.method == 'POST':
        form= ChaiVarietyForm(request.POST)
        if form.is_valid():
            selected_chai= form.cleaned_data['chai_varity']
            Store.objects.filter(chai_varieties= selected_chai)
            stores= selected_chai.stores.all()
    else:
        form= ChaiVarietyForm()
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})