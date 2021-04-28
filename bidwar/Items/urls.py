from django.urls import path
from .views import (ItemList,
	ItemCreate,
	bid,
	ItemDelete,
	ItemDetail
					)
a=1
app_name='Items'
urlpatterns=[
	
	path('',ItemList.as_view(),name='home') ,
	path('add',ItemCreate.as_view(),name='add') ,
	path('bid/<int:item>',bid,name='bid') ,
	path('delete/<int:pk>',ItemDelete.as_view(),name='delete') ,
	path('detail/<int:pk>',ItemDetail.as_view(),name='detail') ,
] 