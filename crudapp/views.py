from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView,DetailView

# Create your views here.

class IndexView(ListView):
    template_name='crudapp/index.html'
    context_object_name='contact_list'

    def get_queryset(self):
        return Contact.objects.all()
    
class ContactDetailView(DetailView):
    model=Contact
    template_name='crudapp/contact_detail.html'
    context_object_name='contact'


def create(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form=ContactForm()
    context={'form':form}
    return render(request,'crudapp/create.html',context)

def edit(request, pk, template_name='crudapp/edit.html'):
    contact=get_object_or_404(Contact,pk=pk)
    form=ContactForm(request.POST or None,instance=contact)
    if form.is_valid():
        form.save()
        return redirect('index')
    context={'form':form}
    return render(request,template_name,context)

def delete(request,pk,template_name='crudapp/confirm_delete.html'):
    contact=get_object_or_404(Contact,pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    context={'object':contact}
    return render(request,template_name,context)
