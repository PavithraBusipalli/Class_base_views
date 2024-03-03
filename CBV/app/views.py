from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, FormView
from .forms import *
# Create your views here.

# Class vs Function based Views

# Returning String Response by both FUnction and Class based Views

def fun_str_res(request):
    return HttpResponse('<center>Hi There all! I am String Response from Function Based View</center>')
# generic class view is responsible for performing all types of operations but it can't do in a efficient and depth functionaly
# So have spicific class views for specific functionality 
class Cls_str_res(View):
    def get(self,request):
        return HttpResponse('<center>Hello I am from class based View<center>')
    


# Rendering template
    
def fun_rend_temp(request):
    return render(request,'fun_rend_temp.html')
# Its a generic way to render template with generic view, we've more specific way to render templaltes
class Cls_rend_temp(View):
    def get(self,request): # standard method : get
        return render(request,'Cls_rend_temp.html')
    
# TemplateView
class Cls_spec_temp(TemplateView):
    template_name = 'Cls_spec_temp.html'



# Rendering Forms

# Funbased View 
def fun_Scl_form(request):
    SO = SclForm()
    d = {'SO':SO}
    if request.method == 'POST':
        SFO = SclForm(request.POST)
        if SFO.is_valid():
            SFO.save()
            return HttpResponse('<center>School Created Successfully</center>')
    return render(request,'SclForm.html',d)

# Generic View
class Cls_gen_Form(View):
    def get(self,request):
        SO = SclForm()
        d = {'SO':SO}
        return render(request,'SclForm.html',d)
    def post(self,request):
        if request.method == 'POST':
            SDO = SclForm(request.POST)
            SDO.save()
            return HttpResponse('<center>School is Created</center>')

# Specific View : FormView
class Cls_Spec_SclForm(FormView):
    template_name = 'Cls_Spec_SclForm.html'
    form_class = SclForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('<center>School is Created successfully</center>')

