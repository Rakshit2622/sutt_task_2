from django.urls import path
from . import views

urlpatterns =[
		path('',views.IndexView , name='Index_view'),
    	path('<int:question_id>/results/', views.results, name='results'),
    	path('<int:question_id>/vote/', views.vote, name='vote'),
    	path('view-all/', views.IndexView_copy,name='Index_view_copy')
]