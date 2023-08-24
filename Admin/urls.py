from django.urls import path
app_name = "WebAdmin"
from Admin import views
urlpatterns = [
    path("District/", views.district_InsertSelect, name="Insert_Dis"),
    path('deletedistrict/<int:did>', views.Districtdelete, name="deletedistrict"),
    path('editdistrict/<int:did>', views.Districtedit, name="editdistrict"),

    path("Place/", views.place_InsertSelect, name="Insert_Plc"),
    path('deleteplace/<int:plc>', views.Placedelete, name="deleteplace"),
    path('editplace/<int:plc>', views.Placeedit, name="editplace"),

    path("Category/", views.category_InsertSelect, name="Insert_Cat"),
    path('deletecategory/<int:cit>', views.Categorydelete, name="deletecategory"),
    path('editcategory/<int:cit>', views.Categoryedit, name="editcategory"),

    path("SubCategory/", views.SubCatg_InsertSelect, name="Insert_SubCatg"),
    path('deletesubcat/<int:sub>', views.Subcatdelete, name="deletesubcat"),

    path("Newseller/", views.newsllr_Insert, name="Insert_newsllr"),
    path("Acceptedseller/", views.acptsllr_Insert, name="Insert_acptsllr"),
    path("Rejectedseller/", views.rjctsllr_Insert, name="Insert_rjctsllr"),
    
    path("acceptsell/<int:aid>", views.AcceptSell, name="acceptseller"),
    path("rejectsell/<int:rid>", views.RejectSell, name="rejectseller"),

    path("Viewcomplaint/", views.viewcomp_Insert,name="Viewcomplaint"),
    path("Viewreply/<int:rid>", views.reply_Insert,name="Reply"),
    path("Viewfeedback/", views.viewfdbk_Insert,name="Viewfeedback"),

    path('Adminhomepage/',views.homepage, name="Home"),

    path('Logout/',views.logout,name="logout"),


]