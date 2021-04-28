from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
	class Meta:
		model=Item
		fields=[
		'name',
		'description',
		'date_posted',
		'owner',
		'price']

class BidForm(forms.ModelForm):
	class Meta:
		model=Item
		fields=[
		'price',
		'bidder']