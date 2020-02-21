from django.shortcuts import render
#getting the Http Responce on template
from django.http import HttpResponse

from .forms import  StudnetRegisterForm,UserForm
from django.views import  generic
from .models import  StudentRegister
from django.urls import reverse_lazy
#filtering Student Objects
from .filters import Searchfilter




#StudentForm Details and User Deatils  
class StudentReg(generic.TemplateView):
    template_name='register.html'
    def get(self,request):
        context = {
            'student': StudnetRegisterForm,
            'user': UserForm
          }
        return render(request,self.template_name,context)

    def post(self,request):
        user_form = UserForm(data=request.POST)
        profile_form = StudnetRegisterForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return   HttpResponse("sucess")




#get the all the StudentDetails

class StudentDetails(generic.ListView):
    model=StudentRegister

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['filter'] = Searchfilter(self.request.GET, queryset=self.get_queryset())
        return  context

#update the all the StudentDetails

class StudentUpdate(generic.UpdateView):
    model =StudentRegister
    fields = '__all__'
    success_url = reverse_lazy('stu_list')

    
#delete the all the StudentDetails

class StudentDelete(generic.DeleteView):
    model =StudentRegister
    success_url = reverse_lazy('stu_list')



