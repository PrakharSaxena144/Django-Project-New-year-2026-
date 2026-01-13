from django.urls import path
from . import views  # '.' refers to the current directory where urls.py is located


# localhost:8000/chai/
# localhost:8000/chai/order/

urlpatterns = [
    path('', views.all_chai, name='all_chai'),  # All Chai page
    path('chai_stores/', views.chai_store_view, name='chai_store_view'),  # Chai store page
]

