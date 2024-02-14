from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import Blog
from django.contrib.messages.views import SuccessMessageMixin

path='blogs'
model_name=Blog
class BlogCreateView(SuccessMessageMixin,CreateView):
    model=model_name
    fields="__all__"
    success_message="Data Saved Successfully"
    template_name=f'{path}/create.html'

class BlogListView(ListView):
    model=model_name
    context_object_name="blogs"
    template_name=f'{path}/index.html'
    ordering=['title']
    
class BlogUpdateView(UpdateView):
    model=model_name
    # success_url='/create'
    fields=['title','description','image']
    # context_object_name='singleblog'
    template_name=f'{path}/ update.html'       
    
    
class BlogDeleteView(DeleteView):
    model=model_name
    success_url="/"
        
class BlogDetailView(DetailView):
    model=model_name
    context_object_name='singleblog'
    template_name=f"{path}/show.html"        