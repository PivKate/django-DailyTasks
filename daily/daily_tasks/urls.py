from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
	path('adddaily/', views.addDaily, name='add'),
	path('complete/<daily_id>', views.completeDaily,name = 'complete'),
	path('deletecomplete', views.deleteComplete, name='deletecomplete'),
	path('deleteall', views.deleteAll, name='deleteall'),
]