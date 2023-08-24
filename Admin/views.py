from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Seller.models import *
from Guest.models import tbl_SellerReg
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
# Create your views here.
# District

def district_InsertSelect(request):
    if 'aid' in request.session:
        districtdata=tbl_District.objects.all()
        if request.method=="POST":
            tbl_District.objects.create(dis_name=request.POST.get('txtdis'))
            return render(request, "Admin/District.html",{'viewdis':districtdata})
        else:
            return render(request, "Admin/District.html",{'viewdis':districtdata})
    else:
        return redirect("WebGuest:Insert_Login")
    
def Districtdelete(request,did):
    tbl_District.objects.get(id=did).delete()
    return redirect ("WebAdmin:Insert_Dis")

def Districtedit(request,did):
    dis=tbl_District.objects.get(id=did)
    if request.method=="POST":
        dis.dis_name=request.POST.get('txtdis')
        dis.save()
        return redirect("WebAdmin:Insert_Dis")
    else:
        return render(request,"Admin/District.html",{'editdis':dis})

# Place

def place_InsertSelect(request):
    if 'aid' in request.session:
        districtdata=tbl_District.objects.all()
        placedata=tbl_Place.objects.all()
        if request.method=="POST":
            disid=request.POST.get('sel_district')
            dist=tbl_District.objects.get(id=disid)
            tbl_Place.objects.create(plc_name=request.POST.get('txtplace'),plc_pincode=request.POST.get('txtpin'),district=dist)
            return render(request, "Admin/Place.html",{'viewdis':districtdata,'viewplc':placedata})
        else:
            return render(request, "Admin/Place.html",{'viewdis':districtdata,'viewplc':placedata})
    else:
        return redirect("WebGuest:Insert_Login")

def Placedelete(request,plc):
    tbl_Place.objects.get(id=plc).delete()
    return redirect ("WebAdmin:Insert_Plc")

def Placeedit(request,plc):
    plac=tbl_Place.objects.get(id=plc)
    if request.method=="POST":
        plac.plc_name=request.POST.get('txtplace')
        plac.plc_pincode=request.POST.get('txtpin')
        plac.save()
        return redirect("WebAdmin:Insert_Plc")
    else:
        return render(request,"Admin/Place.html",{'editplace':plac})

# Category

def category_InsertSelect(request):
    if 'aid' in request.session:
        categorydata=tbl_Category.objects.all()
        if request.method=="POST":
            tbl_Category.objects.create(cat_name=request.POST.get('txtcat'))
            return render(request,"Admin/Category.html",{'viewcat':categorydata})
        else:
            return render(request,"Admin/Category.html",{'viewcat':categorydata})
    else:
        return redirect("WebGuest:Insert_Login")
    
def Categorydelete(request,cit):    
    tbl_Category.objects.get(id=cit).delete()
    return redirect ("WebAdmin:Insert_Cat")
    
def Categoryedit(request,cit):
    cat=tbl_Category.objects.get(id=cit)
    if request.method=="POST":
        cat.cat_name=request.POST.get('txtcat')
        cat.save()
        return redirect("WebAdmin:Insert_Cat")
    else:
        return render(request,"Admin/Category.html",{'editcat':cat})
    
# Subcategory

def SubCatg_InsertSelect(request):
    if 'aid' in request.session:
        categorydata=tbl_Category.objects.all()
        SubCategorydata=tbl_SubCategory.objects.all()
        if request.method=="POST":
            catid=request.POST.get('sel_category')
            categ=tbl_Category.objects.get(id=catid)
            tbl_SubCategory.objects.create(sub_name=request.POST.get('txtcatg'),category=categ)
            return redirect ("WebAdmin:Insert_SubCatg")
        else:
            return render(request,"Admin/SubCategory.html",{'viewcat':SubCategorydata,'dis':categorydata})
    else:
        return redirect("WebGuest:Insert_Login")
    
def Subcatdelete(request,sub):
    tbl_SubCategory.objects.get(id=sub).delete()
    return redirect ("WebAdmin:Insert_SubCatg")

#---------NewSeller---------

def newsllr_Insert(request):
    if 'aid' in request.session:
        data=tbl_SellerReg.objects.filter(status=0)
        return render(request,"Admin/Newseller.html",{'data':data})
    else:
        return redirect("WebGuest:Insert_Login")

def acptsllr_Insert(request):
    if 'aid' in request.session:
        data=tbl_SellerReg.objects.filter(status=1)
        return render(request,"Admin/Acceptedsllr.html",{'data':data})
    else:
        return redirect("WebGuest:Insert_Login")

def rjctsllr_Insert(request):
    if 'aid' in request.session:
        data=tbl_SellerReg.objects.filter(status=2)
        return render(request,"Admin/Rejectedsllr.html",{'data':data})
    else:
        return redirect("WebGuest:Insert_Login")

def AcceptSell(request,aid):
    if 'aid' in request.session:
        data=tbl_SellerReg.objects.get(id=aid)
        data.status=1
        name=data.sllrname
        email=data.sllremail
        data.save()
        send_mail(
            'Respected Sir/Madam '+name,#subject
            "\rYour Account Acceepted you can login  ",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return redirect("WebAdmin:Insert_newsllr")
    else:
        return redirect("WebGuest:Insert_Login")

def RejectSell(request,rid):
    if 'aid' in request.session:
        data=tbl_SellerReg.objects.get(id=rid)
        data.status=2
        name=data.sllrname
        email=data.sllremail
        data.save()
        send_mail(
            'Respected Sir/Madam '+name,#subject
            "\rYour Account Rejected",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return redirect("WebAdmin:Insert_newsllr")
    else:
        return redirect("WebGuest:Insert_Login")

#----Complaint------

def viewcomp_Insert(request):
    if 'aid' in request.session:
        userdata=tbl_UserReg.objects.all()
        sellerdata=tbl_SellerReg.objects.all()
        usercomplaint=tbl_complaint.objects.filter(status=0,user__in=userdata)
        sellercomplaint=tbl_complaint.objects.filter(status=0,seller__in=sellerdata)
        return render(request, "Admin/Viewcomplaint.html", {'usercomp':usercomplaint,'selercomp':sellercomplaint})
    else:
        return redirect("WebGuest:Insert_Login")

#-----Reply---------

def reply_Insert(request,rid):
    if 'aid' in request.session:
        comp=tbl_complaint.objects.get(id=rid)
        if request.method=="POST":
            comp.reply=request.POST.get('txtrply')
            comp.status=1
            comp.save()
            return redirect("WebAdmin:Viewcomplaint")
        else:
            return render(request, "Admin/Reply.html")
    else:
        return redirect("WebGuest:Insert_Login")

#------feedback------

def viewfdbk_Insert(request):
    if 'aid' in request.session:
        userdata=tbl_UserReg.objects.all()
        sellerdata=tbl_SellerReg.objects.all()
        usercomplaint=tbl_feedback.objects.filter(user__in=userdata)
        sellercomplaint=tbl_feedback.objects.filter(seller__in=sellerdata)
        return render(request, "Admin/Viewfeedback.html", {'usercomp':usercomplaint,'selercomp':sellercomplaint})
    else:
        return redirect("WebGuest:Insert_Login")

def homepage(request):
    if 'aid' in request.session:
        return render(request,"Admin/Homepage.html")
    else:
        return redirect("WebGuest:Insert_Login")

def logout(request):
    del request.session['aid']
    return redirect('WebGuest:Insert_Login')