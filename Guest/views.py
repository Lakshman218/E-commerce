from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

#------Seller registration----------

def sellerreg_Insert(request):
    dis=tbl_District.objects.all()
    pl=tbl_Place.objects.all()
    if request.method=="POST":
        disid=request.POST.get('sel_dis')
        dist=tbl_District.objects.get(id=disid)
        plid=request.POST.get('sel_plc')
        plc=tbl_Place.objects.get(id=plid)
        tbl_SellerReg.objects.create(sllrname=request.POST.get('txtname'),sllrcontact=request.POST.get('txtnum'),sllremail=request.POST.get('txtmail'),sllraddress=request.POST.get('txtaddress'),sllrlandmark=request.POST.get('txtlndmrk'),sllrpassword=request.POST.get('txtpswd'),sllrconformpswd=request.POST.get('txtcnfrm'),sllrproof=request.FILES.get('txtproof'),sllrphoto=request.FILES.get('txtphoto'),place=plc)
        send_mail(
            'Respected Sir/Madam '+request.POST.get('txtname'),#subject
            "\rYour Account Created SucessFully",#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtmail')],
        )
        return render(request,"Guest/SellerRegistration.html",{'DIS':dis})
    else:
        return render(request,"Guest/SellerRegistration.html",{'DIS':dis,'PLA':pl})

def ajax_plc(request):
    dis=request.GET.get('disd')
    plc=tbl_Place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{'PLC':plc})

#---------User registration-----------

def userreg_Insert(request):
    dis=tbl_District.objects.all()
    pl=tbl_Place.objects.all()
    
    if request.method=="POST":
        disid=request.POST.get('sel_dis')
        dist=tbl_District.objects.get(id=disid)
        plid=request.POST.get('sel_plc')
        plc=tbl_Place.objects.get(id=plid)
        tbl_UserReg.objects.create(usrname=request.POST.get('txtname'),usrcontact=request.POST.get('txtnum'),usremail=request.POST.get('txtmail'),usrgender=request.POST.get('gender'),usraddress=request.POST.get('txtaddress'),usrpassword=request.POST.get('txtpswd'),usrconformpswd=request.POST.get('txtcnfrm'),usrphoto=request.FILES.get('txtphoto'),place=plc)
        send_mail(
            'Respected Sir/Madam '+request.POST.get('txtname'),#subject
            "\rYour Account Created SucessFully",#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtmail')],
        )
        return render(request,"Guest/UserRegistration.html",{'DIS':dis})
    else:
        return render(request,"Guest/UserRegistration.html",{'DIS':dis,'PLA':pl})

#----Login------

def login_Insert(request):
    if request.method=="POST":
        Email=request.POST.get('txtmail')
        Password=request.POST.get('txtpswd')
        usercount=tbl_UserReg.objects.filter(usremail=Email, usrpassword=Password).count()
        sellercount=tbl_SellerReg.objects.filter(sllremail=Email, sllrpassword=Password,status=1).count()
        admincount=Adminlogin.objects.filter(email=Email,password=Password).count()
        if usercount>0:
            user=tbl_UserReg.objects.get(usremail=Email, usrpassword=Password)
            request.session["uid"]=user.id
            return redirect("WebUser:userhomepage")
        elif sellercount>0:
            seller=tbl_SellerReg.objects.get(sllremail=Email, sllrpassword=Password)
            request.session["sid"]=seller.id
            return redirect("WebSeller:sellerhomepage")
        elif admincount>0:
            admin=Adminlogin.objects.get(email=Email,password=Password)
            request.session["aid"]=admin.id
            return redirect("WebAdmin:Home")
        else:
            error="Invalid Credentials!!"
            return render(request, "Guest/Login.html",{'ERROR':error})
    else:
        return render(request, "Guest/Login.html")
    
def homepage_Insert(request):
    return render(request,"Guest/Homepage.html")

    

