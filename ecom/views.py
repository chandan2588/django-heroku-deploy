from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from ecom.models import ProdTable
# Create your views here.

class ecomForm(ModelForm):
    class Meta:
        model = ProdTable
        fields = ['pname','pamount']

def ecom_list(request, template_name='ecom/ecom_list.html'):
    ecomsProducts = ProdTable.objects.all()
    data = {}
    data['object_list'] = ecomsProducts
    return render(request, template_name, data)

def ecom_create(request, template_name='ecom/ecom_form.html'):
    form = ecomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ecom_list')
    return render(request, template_name, {'form':form})

def ecom_update(request, pk, template_name='ecom/ecom_form.html'):
    ecomUpdate = get_object_or_404(ProdTable, pk=pk)
    form = ecomForm(request.POST or None, instance=ecomUpdate)
    if form.is_valid():
        form.save()
        return redirect('ecom_list')
    return render(request, template_name, {'form':form})

def ecom_delete(request, pk, template_name='ecom/ecom_confirm_delete.html'):
    ecomDelete = get_object_or_404(ProdTable, pk=pk)    
    if request.method=='POST':
        server.delete()
        return redirect('ecom_list')
    return render(request, template_name, {'object':ecomDelete})