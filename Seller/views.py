from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
from Seller.models import *

# Create your views here.

def sellerhomepage_Insert(request):
    if 'sid' in request.session:
        return render(request, "Seller/Sellerhomepage.html")
    else:
        return redirect("WebGuest:Insert_Login")

def sellerprofile_Insert(request):
    if 'sid' in request.session:
        data= tbl_SellerReg.objects.get(id=request.session['sid'])
        return render(request, "Seller/Slrprofile.html", {'data':data})
    else:
        return redirect("WebGuest:Insert_Login")

def sellereditprfl_Insert(request):
    data = tbl_SellerReg.objects.get(id=request.session['sid'])
    if request.method=="POST":
        data.sllrname=request.POST.get('txtname')
        data.sllrcontact=request.POST.get('txtnum')
        data.sllraddress=request.POST.get('txtaddress')
        data.save()
        return redirect("WebSeller:myprofile")
    else:
        return render(request, "Seller/Slreditprofile.html", {'data':data})
    
def sellerchangepswd_Insert(request):
    if 'sid' in request.session:
        if request.method=="POST":
            Sellercount=tbl_SellerReg.objects.filter(sllrpassword=request.POST.get('currentpassword'),id=request.session["sid"]).count()
            if Sellercount>0:
                Seller=tbl_SellerReg.objects.get(sllrpassword=request.POST.get('currentpassword'),id=request.session["sid"])
                if request.POST.get('newpassword')==request.POST.get('confirmpassword'):
                    Seller.sllrpassword=request.POST.get('newpassword')
                    Seller.save()
                    return redirect("WebSeller:sellerhomepage")
                else:
                    return render(request, "Seller/Slrchangepssd.html")
            else:
                return render(request, "Seller/Slrchangepssd.html")
        else:
            return render(request, "Seller/Slrchangepssd.html")
    else:
         return redirect("WebGuest:Insert_Login")   
    
#---------product-----------

def sellerproduct_insert(request):
    if 'sid' in request.session:
        cat=tbl_Category.objects.all()
        sub=tbl_SubCategory.objects.all()
        sel=tbl_SellerReg.objects.get(id=request.session["sid"])
        pro=tbl_Slrproduct.objects.filter(seller=sel)
        if request.method=="POST":
            catid=request.POST.get('sel_cat')
            catg=tbl_Category.objects.get(id=catid)
            subid=request.POST.get('sel_sub')
            subc=tbl_SubCategory.objects.get(id=subid)
            tbl_Slrproduct.objects.create(prdct_name=request.POST.get('txtname'),prdct_details=request.POST.get('txtdetails'),prdct_rate=request.POST.get('txtrate'),prdct_image=request.FILES.get('txtimg'),subcategory=subc,seller=sel)
            return render(request, "Seller/Slrproduct.html",{'CAT':cat,'SUB':pro})
        else:
            return render(request, "Seller/Slrproduct.html",{'CAT':cat,'SUB':pro})
    else:
         return redirect("WebGuest:Insert_Login")   
    
def Productdelete(request,pro):
    tbl_Slrproduct.objects.get(id=pro).delete()
    return redirect ("WebSeller:Insert_product")
    
def ajax_sub(request):
    cat=request.GET.get('cate')
    categ=tbl_Category.objects.get(id=cat)
    subc=tbl_SubCategory.objects.filter(category=categ)
    return render(request,"Seller/Ajaxsubcategory.html",{'SUBC':subc})

#--------complaint-------------

def ComplaintInsert(request):
    if 'sid' in request.session:
        us=tbl_SellerReg.objects.get(id=request.session["sid"])
        data=tbl_complaint.objects.filter(seller=us)
        if request.method=="POST":
            tbl_complaint.objects.create(content=request.POST.get('txtcomplaint'),seller=us)
            return redirect("WebSeller:complaintinsert")
        else:
            return render(request,"Seller/SlrComplaint.html",{'Data':data})
    else:
        return redirect("WebGuest:Insert_Login")    
    
def FeedbackInsert(request):
    if 'sid' in request.session:
        us=tbl_SellerReg.objects.get(id=request.session["sid"])
        data=tbl_feedback.objects.filter(seller=us)
        if request.method=="POST":
            tbl_feedback.objects.create(content=request.POST.get('txtfdbk'),seller=us)
            return redirect("WebUser:feedbackinsert")
        else:
            return render(request,"Seller/Slrfeedback.html",{'Data':data})
    else:
        return redirect("WebGuest:Insert_Login")    

def Complaint_delete(request,sid):
    tbl_complaint.objects.get(id=sid).delete()
    return redirect("WebSeller:complaintinsert")

def Feedback_delete(request,sid):
    tbl_feedback.objects.get(id=sid).delete()
    return redirect("WebSeller:feedbackinsert")

#------------user bookings--------------

def userbookings(request):
    if 'sid' in request.session:
        slr=tbl_SellerReg.objects.get(id=request.session["sid"])
        data=Cart.objects.filter(product__seller=slr)
        return render(request,"Seller/Userbookings.html",{'data':data})
    else:
        return redirect("WebGuest:Insert_Login")
  

def acceptorder(request,oid):
    data=Booking.objects.get(id=oid)
    data.booking_status=2
    data.save()
    return redirect("WebSeller:user_bookings")

def rejectorder(request,oid):
    data=Booking.objects.get(id=oid)
    data.booking_status=4
    data.save()
    return redirect("WebSeller:user_bookings")

def deliverorder(request,oid):
    data=Booking.objects.get(id=oid)
    data.booking_status=3
    data.save()
    return redirect("WebSeller:user_bookings")

def logout(request):
    del request.session['sid']
    return redirect('WebGuest:Insert_Login')

def removecart(request,did):
    Cart.objects.get(id=did).delete()
    return redirect('WebSeller:user_bookings')