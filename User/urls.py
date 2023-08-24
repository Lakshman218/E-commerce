from django.urls import path
app_name = "WebUser"
from User import views
urlpatterns= [
    path('Userhomepage/',views.userhomepage_Insert, name="userhomepage"),
    path('Myprofile/', views.userprofile_Insert, name="myprofile"),
    path('Editprofile/', views.usereditprfl_Insert, name="editprofile"),
    path('changepassword/', views.userchangepswd_Insert, name="changepassword"),

    path("Viewproduct/<int:sid>", views.viewproduct_Insert, name="view_product"),
    path("ajaxproduct/", views.AjaxProduct, name="ajax-product"),
    path("addtocart/<int:pid>",views.Addtocart,name="addtocart"),

    path("Viewseller/", views.viewseller_Insert, name="view_seller"),
    path("ajaxseller/", views.Ajaxseller, name="ajax-seller"),

    path("Complaint/",views.ComplaintInsert, name="complaintinsert"),
    path("Feedback/",views.FeedbackInsert, name="feedbackinsert"),

    path("DeleteComplaint/<int:uid>",views.Complaint_delete,name="deletecompl"),
    path("DeleteFeedback/<int:uid>",views.Feedback_delete,name="deletefeed"),

    path("mycart/",views.mycart, name="mycart"),

    path('getqnty/',views.get_qnty,name="GetQty"),
    path('removeqty/<int:did>',views.removecart,name="removeqty"),
    path('removeqtys/<int:did>',views.removecarts,name="removeqtys"),
    path('payment/',views.PAYMENT,name="payment"),
    path('processingpayment/',views.processingpayment,name="processingpayment"),
    path('patmentsucessful/',views.paysucess,name="patmentsucessful"),

    path('Mybookings/',views.mybookings,name="my_bookings"),

    path('Logout/',views.logout,name="logout"),

]
