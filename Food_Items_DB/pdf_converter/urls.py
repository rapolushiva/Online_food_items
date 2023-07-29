from  django.urls import path
from .import views

urlpatterns=[
    path('shows/',views.show_products, name='showproducts'),
    path('createpdf/',views.pdf_report_created, name='createpdf'),
]


