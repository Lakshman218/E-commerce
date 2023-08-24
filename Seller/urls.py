from django.urls import path
app_name = "WebSeller"
from Seller import views
urlpatterns = [
    path('Sellerhomepage/',views.sellerhomepage_Insert, name="sellerhomepage"),
    path('Myprofile/', views.sellerprofile_Insert, name="myprofile"),
    path('Editprofile/', views.sellereditprfl_Insert, name="editprofile"),
    path('changepassword/', views.sellerchangepswd_Insert, name="changepassword"),

    path("Sellerproduct/",views.sellerproduct_insert,name="Insert_product"),
    path('deleteproduct/<int:pro>', views.Productdelete, name="deleteproduct"),
    path('ajaxsub/',views.ajax_sub,name="Ajax_subc"),

    path("Complaint/",views.ComplaintInsert, name="complaintinsert"),
    path("Feedback/",views.FeedbackInsert, name="feedbackinsert"),

    path("DeleteComplaint/<int:sid>",views.Complaint_delete,name="deletecompl"),
    path("DeleteFeedback/<int:sid>",views.Feedback_delete,name="deletefeed"),
    path('removeqty/<int:did>',views.removecart,name="removeqtys"),
    path('Userbookings/',views.userbookings,name="user_bookings"),
    path("accept/<int:oid>",views.acceptorder,name="acceptorder"),
    path("reject/<int:oid>",views.rejectorder,name="rejectorder"),
    path("deliver/<int:oid>",views.deliverorder,name="deliverorder"),

    path('Logout/',views.logout,name="logout"),
]