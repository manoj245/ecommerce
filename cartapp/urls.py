from django.urls import path
from cartapp import views
app_name='cartapp'
urlpatterns=[
  path('addcart/' ,views.addcart),
  path('insertcart/',views.insertcart),
  path('cartview/',views.cartview),
  path('delete/',views.delete),
  path('modifycart/',views.modifycart),
  path('modifiedcart/',views.modifiedcart),
]