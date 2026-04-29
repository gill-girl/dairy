from django.urls import path
 
from. import views 


app_name='cart'
urlpatterns = [
    path('add/<int:product_id>/',views.cart_add, name='cart_add'),
    path('',views.cart_detail, name='cart_detail'),
    path('remove/<int:item_id>/',views.cart_remove,name='remove_item'),
    path('view/',views.cart_view,name='cart_view'),
    

]
