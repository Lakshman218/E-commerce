from django.urls import path
app_name = "WebGuest"
from Guest import views
urlpatterns = [
    path("SellerRegistration/",views.sellerreg_Insert,name="Insert_Seller"),
    path('ajaxplc/',views.ajax_plc,name="Ajax_Place"),
    path("UserRegistration/",views.userreg_Insert,name="Insert_User"),
    path('Login/',views.login_Insert,name="Insert_Login"),
    path('',views.homepage_Insert, name="homepage"),
    
]