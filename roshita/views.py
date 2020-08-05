from django.shortcuts import render,redirect

from .models import Roshita
from .forms import RoshitaForm


# Create your views here.
def roshita_list(request):
    roshita_list = Roshita.objects.all()

    if request.method=='POST':
        form = RoshitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roshita:roshita_list')
            
    else:
        form = RoshitaForm()          

    return render(request,'roshita.html',{
        'roshita_list':roshita_list,
       
    }) 

def update_roshita(request,pk):
    roshita_id = Roshita.objects.get(pk=pk)
    updated_form = RoshitaForm(instance=roshita_id)
    if request.method == 'POST':
        updated_form = RoshitaForm(request.POST,instance=roshita_id)
    if updated_form.is_valid():
        updated_form.save()
        return redirect('roshita:roshita_list')
    else:
        updated_form = RoshitaForm(instance=roshita_id)

    return render(request,'update_roshita.html',{
        'update_form':updated_form,
    })

def roshtia_delete(request,pk):
    roshita_delete = Roshita.objects.get(pk=pk)
    roshita_delete.delete()
    return redirect('roshita:roshita_list')        