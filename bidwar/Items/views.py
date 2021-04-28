from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Item
from django.contrib.auth.models import User
from .forms import ItemForm,BidForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class ItemList(ListView):
	model = Item
	ordering= ['-date_posted']

class ItemDetail(DetailView):
	model=Item

class ItemCreate(LoginRequiredMixin,CreateView):
	model = Item
	fields = [
		'name',
		'description',
		'price']
	def form_valid(self,form):
		form.instance.owner =self.request.user
		return super().form_valid(form)

@login_required
def bid(request,item):
	obj=Item.objects.get(pk=item)
	cur=obj.price
	form=BidForm(request.POST or None,instance=obj)
	if form.is_valid():
		if(form.cleaned_data.get('price')>cur):
			form.save()
			
			return render(request,"Items/start.html",{})
		else:
			messages.success(request, f'Enter high bid')
	cnxt={
	'form':form
	}
	return render(request,"Items/bid.html",cnxt)
class ItemDelete(LoginRequiredMixin,UserPassesTestMixin,DetailView):
	model=Item
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.owner:
			return True
		return False

def about_view(request):
	return render(request,"Items/about.html",{})

def start_view(request):
	
	last = Item.objects.order_by('-id')[:3]
	cnxt = {
	'last' : last,

	}
	return render(request,"Items/start.html",cnxt)

