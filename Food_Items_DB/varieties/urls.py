from django.urls import path
from varieties import views
from varieties.views import showitem
urlpatterns = [
    path('',views.showitem, name='showallitems'),
    path('additem',views.addProduct, name='additem'),
    path('itemdetails/<int:pk>',views.itemdetail,name='itemdetails'),
    path('updateitem/<int:pk>',views.updateitem,name='updateitem'),
    path('delete/<int:pk>',views.deleteitem,name='deleteitem'),
    path('search',views.searchbar,name='searchbar')

]
