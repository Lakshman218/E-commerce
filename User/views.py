from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Seller.models import *
from User.models import *

# Create your views here.

def userhomepage_Insert(request):
    if 'uid' in request.session:
        return render(request, "User/Userhomepage.html")
    else:
        return redirect("WebGuest:Insert_Login")

def userprofile_Insert(request):
    if 'uid' in request.session:
        data= tbl_UserReg.objects.get(id=request.session['uid'])
        return render(request, "User/Usrprofile.html", {'data':data})
    else:
        return redirect("WebGuest:Insert_Login")

def usereditprfl_Insert(request):
    data = tbl_UserReg.objects.get(id=request.session['uid'])
    if request.method=="POST":
        data.usrname=request.POST.get('txtname')
        data.usrcontact=request.POST.get('txtnum')
        data.usraddress=request.POST.get('txtaddress')
        data.save()
        return redirect("WebUser:myprofile")
    else:
        return render(request, "User/Usreditprofile.html", {'data':data})
    
def userchangepswd_Insert(request):
    if 'uid' in request.session:
        if request.method=="POST":
            Usercount=tbl_UserReg.objects.filter(usrpassword=request.POST.get('currentpassword'),id=request.session["uid"]).count()
            if Usercount>0:
                User=tbl_UserReg.objects.get(usrpassword=request.POST.get('currentpassword'),id=request.session["uid"])
                if request.POST.get('newpassword')==request.POST.get('confirmpassword'):
                    User.usrpassword=request.POST.get('newpassword')
                    User.save()
                    return redirect("WebUser:userhomepage")
                else:
                    return render(request, "User/Usrchangepssd.html")
            else:
                return render(request, "User/Usrchangepssd.html")
        else:
            return render(request, "User/Usrchangepssd.html")
    else:
        return redirect("WebGuest:Insert_Login")    
    
#------view product---------

def viewproduct_Insert(request,sid):
    if 'uid' in request.session:
        request.session["seller"]=sid
        catdata=tbl_Category.objects.all()
        sellerdaat=tbl_SellerReg.objects.get(id=sid)
        product=tbl_Slrproduct.objects.filter(seller=sellerdaat)
        return render(request,"User/Userviewproduct.html",{'product':product,'CAT':catdata})
    else:
        return redirect("WebGuest:Insert_Login")

def viewseller_Insert(request):
    if 'uid' in request.session:
        dis=tbl_District.objects.all()
        seller=tbl_SellerReg.objects.filter(status=1)
        return render(request,"User/Usrviewseller.html",{'seller':seller,'DIS':dis})
    else:
        return redirect("WebGuest:Insert_Login")

#--------complaint----------

def ComplaintInsert(request):
    if 'uid' in request.session:
        us=tbl_UserReg.objects.get(id=request.session["uid"])
        data=tbl_complaint.objects.filter(user=us)
        if request.method=="POST":
            tbl_complaint.objects.create(content=request.POST.get('txtcomplaint'),user=us)
            return redirect("WebUser:complaintinsert")
        else:
            return render(request,"User/UserComplaint.html",{'Data':data})
    else:
        return redirect("WebGuest:Insert_Login")    
    
def FeedbackInsert(request):
    if 'uid' in request.session:
        us=tbl_UserReg.objects.get(id=request.session["uid"])
        data=tbl_feedback.objects.filter(user=us)
        if request.method=="POST":
            tbl_feedback.objects.create(content=request.POST.get('txtfdbk'),user=us)
            return redirect("WebUser:feedbackinsert")
        else:
            return render(request,"User/Userfeedback.html",{'Data':data})
    else:
        return redirect("WebGuest:Insert_Login")    

def Complaint_delete(request,uid):
    tbl_complaint.objects.get(id=uid).delete()
    return redirect("WebUser:complaintinsert")

def Feedback_delete(request,uid):
    tbl_feedback.objects.get(id=uid).delete()
    return redirect("WebUser:feedbackinsert")

def Ajaxseller(request):
    if request.GET.get('pid')!="":
        pl=tbl_Place.objects.get(id=request.GET.get('pid'))
        data=tbl_SellerReg.objects.filter(place=pl,status=1)
        return render(request,"User/Ajaxseller.html",{'seller':data})
    else:
        dis=tbl_District.objects.get(id=request.GET.get('did'))
        data=tbl_SellerReg.objects.filter(place__district=dis,status=1)
        return render(request,"User/Ajaxseller.html",{'seller':data})
    
def AjaxProduct(request):
    sellerdata=tbl_SellerReg.objects.get(id=request.session["seller"])
    if request.GET.get('sid')!="":
        pl=tbl_SubCategory.objects.get(id=request.GET.get('sid'))
        data=tbl_Slrproduct.objects.filter(subcategory=pl,seller=sellerdata)
        return render(request,"User/Ajaxproduct.html",{'product':data})
    else:
        dis=tbl_Category.objects.get(id=request.GET.get('cid'))
        data=tbl_Slrproduct.objects.filter(subcategory__category=dis,seller=sellerdata)
        return render(request,"User/Ajaxproduct.html",{'product':data})
    
#-----------Add to cart---------------

def Addtocart(request,pid):
    if 'uid' in request.session:
        
        message=""
        prod=tbl_Slrproduct.objects.get(id=pid)
        userdata=tbl_UserReg.objects.get(id=request.session["uid"])
        bcount=Booking.objects.filter(user=userdata,booking_status=0).count()
        if bcount>0:
            bookdata=Booking.objects.get(user=userdata,booking_status=0)
            cartcount=Cart.objects.filter(booking=bookdata,product=prod).count()
            if cartcount>0:
                message="Already Added"
                del request.session["seller"]
                return render(request,"User/Userviewproduct.html",{'mess':message})
            else:
                Cart.objects.create(booking=bookdata,product=prod)
                message="Added"
                del request.session["seller"]
                return render(request,"User/Userviewproduct.html",{'mess':message})
        else:
            Booking.objects.create(user=userdata)
            bcount=Booking.objects.filter(user=userdata,booking_status=0).count()
            if bcount>0:
                bookdata=Booking.objects.get(user=userdata,booking_status=0)
                cartcount=Cart.objects.filter(booking=bookdata,product=prod).count()
                if cartcount>0:
                    message="Already Added"
                    
                    return render(request,"User/Userviewproduct.html",{'mess':message})
                else:
                    Cart.objects.create(booking=bookdata,product=prod)
                    message="Added"
                   
                    return render(request,"User/Userviewproduct.html",{'mess':message})
            else:
                message="Failed"
                
                return render(request,"User/Userviewproduct.html",{'mess':message})
    else:  
        return redirect("WebGuest:Insert_Login")      
        
def mycart(request):
    if 'uid' in request.session:
        userdata=tbl_UserReg.objects.get(id=request.session["uid"])
        if request.method=="POST":
            return redirect("WebUser:payment")
        else:
            bcount=Booking.objects.filter(user=userdata,booking_status=0).count()
            if bcount>0:
                bookdata=Booking.objects.get(user=userdata,booking_status=0)
                request.session["bookings"]=bookdata.id
                data=Cart.objects.filter(booking=bookdata)
                return render(request,"User/Mycart.html",{'data':data})
            else:
                return render(request,"User/Mycart.html") 
    else:        
        return redirect("WebGuest:Insert_Login")

def get_qnty(request):
        qty=request.GET.get('QTY')
        alt=request.GET.get('ALT')
        cart=Cart.objects.get(id=alt)
        cart.cart_qty=qty
        cart.save()
        return redirect('WebUser:mycart')

def PAYMENT(request):   
    if 'uid' in request.session:
        if request.method=="POST": 
            ids=Booking.objects.get(id=request.session["bookings"])
            ids.booking_status=1
            ids.payment_status=1
            ids.save()
            return redirect("WebUser:processingpayment")
        else:
            return render(request,"User/Payment.html")
    else:    
        return redirect("WebGuest:Insert_Login")
            
        
def processingpayment(request):
    if 'uid' in request.session:
        return render(request,"User/runpayment.html")
    else:
        return redirect("WebGuest:Insert_Login")
   
def paysucess(request):
   if 'uid' in request.session:
        return render(request,"User/paysucessful.html")
   else:
       return redirect("WebGuest:Insert_Login")
    
#---------My bookings------------

def mybookings(request):
   if 'uid' in request.session:
    usr=tbl_UserReg.objects.get(id=request.session["uid"])
    data=Cart.objects.filter(booking__user=usr)
    return render(request,"User/MyBookings.html",{'data':data})
   else:
       return redirect("WebGuest:Insert_Login")
   
def logout(request):
    del request.session['uid']
    return redirect('WebGuest:Insert_Login')
   

def removecart(request,did):
    Cart.objects.get(id=did).delete()
    return redirect('WebUser:mycart')

def removecarts(request,did):
    Cart.objects.get(id=did).delete()
    return redirect('WebUser:my_bookings')