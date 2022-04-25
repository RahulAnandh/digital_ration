from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from digital_ration_app.models import *
import hashlib
# from reportlab.pdfgen import canvas 
from django.views.generic import View
from datetime import date
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def indexpage(request):
    data=Product_tb.objects.all()[:4]
    if request.session.has_key('userid'):
        # userid=request.GET['userid']
        # kartdata=Kart_tb.objects.all().filter(id='userid')
        # return render(request,'index.html',{'productdata':data,'kartdata':kartdata})
        return render(request,'index.html',{'productdata':data})
    else:
        return render(request,'index.html',{'productdata':data})

def loginuser(request):
    if request.session.has_key('userid'):
        productdata=Product_tb.objects.all()[:20]
        uid=request.session['userid']
        data=User_registration_tb.objects.all().filter(id=uid)
        kartdata=Kart_tb.objects.all().filter(userid=uid)
        return render(request,'profile.html',{'userdata':data,'productdata':productdata,'kartdata':kartdata})
    else:
        if request.method == "POST":
            email=request.POST['email']
            password=request.POST['password']
            hashpassword=hashlib.md5(password.encode('utf8')).hexdigest()
            query=User_registration_tb.objects.all().filter(email=email,password=hashpassword)
            if query:
                for x in query:
                    request.session['userid'] = x.id
                    request.session['useremail'] = x.email
                    uid=request.session['userid']
                    data=User_registration_tb.objects.all().filter(email=email,password=hashpassword)
                    productdata=Product_tb.objects.all()[:20]
                   
                return render(request,'profile.html',{'userdata':data,'productdata':productdata})
            # return HttpResponseRedirect('/')
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html')

def adminlogin(request):
    if request.session.has_key('adminid'):
        return render(request,'admin_panel.html')
    else:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            check=Admin_tb.objects.all().filter(email=email,password=password)
            if check:
                for x in check:
                    request.session['adminid'] = x.id
                    request.session['adminemail'] = x.email
                    uid=request.session['adminid']
                    return render(request,'admin_panel.html')
                else:
                    return render(request,'admin_login.html')
        else:
            return render(request,'admin_login.html',{'error':"Login to perform Task"})

def eventpage(request):
    return render(request,'events.html')

def aboutpage(request):
    return render(request,'about.html')

def productpage(request):
    return render(request,'products.html')

def servicespage(request):
    return render(request,'services.html')

def mailpage(request):
    if request.method == "POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        query=Contact_tb(name=name,phone=phone,email=email,subject=subject,message=message)
        query.save()
        today = date.today()
        notification=Notification_tb(notificationtype='Info Notification',date=today,message='One Mail Recived.!',read='False')
        notification.save()
        return render(request,'mail.html')
    else:
        return render(request,'mail.html')

def householdpage(request):
    return render(request,'household.html')

def vegetablespage(request):
    return render(request,'vegetables.html')

def kitchenpage(request):
    return render(request,'kitchen.html')

def subscribe(request):
    if request.method == "POST":
        email=request.POST['email']
        query=Subscribe_tb(email=email)
        query.save()
        today = date.today()
        notification=Notification_tb(notificationtype='Info Notification',date=today,message='One user Subscribed.!',read='False')
        notification.save()
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def singleproduct(request):
    return render(request,'single.html')

def productlist(request):
    if request.session.has_key('adminid'):
        data=Product_tb.objects.all()
        return render(request,'product_list.html',{'productdata':data})
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})

def userlist(request):
    if request.session.has_key('adminid'):
        data=User_registration_tb.objects.all()
        return render(request,'user_list.html',{'userdata':data})
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})
    

def verifieduserlist(request):
    if request.session.has_key('adminid'):
        data=User_registration_tb.objects.all().filter(verified = 'True')
        return render(request,'verified_user_list.html',{'userdata':data})
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})

def nonverifieduserlist(request):
    if request.session.has_key('adminid'):
        data=User_registration_tb.objects.all().filter(verified = 'False')
        return render(request,'non_verified_user_list.html',{'userdata':data})
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})

def addproduct(request):
    if request.session.has_key('adminid'):
        if request.method == "POST":
            image=request.FILES['image']
            month=request.POST['month']
            name=request.POST['name']
            price=request.POST['price']
            quantity=request.POST['quantity']
            discription=request.POST['discription']
            check=Product_tb.objects.all().filter(name=name,price=price,quantity=quantity,discription=discription,month=month)
            if check:
                return render(request,'add_product.html')
            else:
                today = date.today()
                notification=Notification_tb(notificationtype='Info Notification',date=today,message='Product is Created.!',read='False')
                notification.save()
                query=Product_tb(image=image,name=name,price=price,quantity=quantity,discription=discription,month=month)
                query.save()
                return render(request,'add_product.html')
        else:
            return render(request,'add_product.html')
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})

def userregistration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        gender = request.POST['gender']
        aadharnumber = request.POST['aadharnumber']
        rationcardnumber = request.POST['rationcardnumber']
        hashpassword=hashlib.md5(password.encode('utf8')).hexdigest()
        check=User_registration_tb.objects.all().filter(name=name,email=email,password=hashpassword,phone=phone,gender=gender,aadharnumber=aadharnumber,rationcardnumber=rationcardnumber)
        if check:
            return render(request,'user_registration.html')
        else:
            today = date.today()
            notification=Notification_tb(notificationtype='Info Notification',date=today,message='User is Created.!',read='False')
            notification.save()
            query=User_registration_tb(name=name,email=email,password=hashpassword,phone=phone,gender=gender,aadharnumber=aadharnumber,rationcardnumber=rationcardnumber,verified='False')
            query.save()
            subject = 'welcome to Digital Ration.'
            message = f'Hi {name}, thank you for registering in Digital Ration.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'user_registration.html')
    else:
        return render(request,'user_registration.html')

def editproduct(request):
    if request.session.has_key('adminid'):
        if request.method == "POST":
            pid=request.POST['pid']
            # image=request.FILES['image']
            name=request.POST['name']
            price=request.POST['price']
            quantity=request.POST['quantity']
            discription=request.POST['discription']
            query=Product_tb.objects.all().filter(id=pid).update(name=name,price=price,quantity=quantity,discription=discription)
            return HttpResponseRedirect('/productlist/')
        else:
            productid=request.GET['pid']
            data=Product_tb.objects.all().filter(id=productid)
            return render(request,'edit_product.html',{"editproductdata":data})
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})

def checkout(request):
    if request.session.has_key('userid'):
        if request.method == "POST":
            productid=request.POST['productid']
            usersessionid=request.session['userid']
            pid=Product_tb.objects.get(id=productid)
            uid=User_registration_tb.objects.get(id=usersessionid)
            existinkart=Kart_tb.objects.all().filter(productid=pid,userid=uid)
            if existinkart:
                return HttpResponseRedirect('/login/')
            else:
                Kart=Kart_tb(productcount='1',productid=pid,userid=uid)
                Kart.save()
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request,'login.html')

def userverification(request):
    if request.session.has_key('adminid'):
        uid=request.GET['uid']
        query=User_registration_tb.objects.all().filter(id=uid).update(verified='True')
        return HttpResponseRedirect('/nonverifieduserlist/')
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})

def issuecard(request):
    if request.session.has_key('adminid'):
        uid=request.GET['uid']
        data=User_registration_tb.objects.all().filter(id=uid)
        return render(request,'ration_card.html',{"carddata":data})
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})

def changepassword(request):
    if request.session.has_key('userid'):
        if request.method == "GET":
            uid=request.GET['uid']
            # data=User_registration_tb.objects.all().filter(email=email,password=password)
            data=User_registration_tb.objects.all().filter(id=uid)
            if data:
                return render(request,'change_user_password.html',{"data":data})
            else:
                return HttpResponseRedirect('/login/')
        if request.method == "POST":
            name=request.POST['uid']
            oldpassword=request.POST['oldpassword']
            newpassword=request.POST['newpassword']
            oldhashpassword=hashlib.md5(oldpassword.encode('utf8')).hexdigest()
            newhashpassword=hashlib.md5(newpassword.encode('utf8')).hexdigest()
            data=User_registration_tb.objects.all().filter(id=uid,password=oldhashpassword)
            if data:
                query=User_registration_tb.objects.all().filter(id=uid,password=oldhashpassword).update(password='newhashpassword')
                return HttpResponseRedirect('/login/')
            else:
                return HttpResponseRedirect('/login/')
    else:
        return render(request,'login.html',{'error':"Login to perform Task"})

def notifications(request):
    if request.session.has_key('adminid'):
        data=Notification_tb.objects.all().filter(read='False')
        return render(request,'notifications.html',{"notifications":data})
    else:
        return render(request,'admin_login.html',{'error':"Login to perform Task"})
    
def subscribers(request):
    if request.session.has_key('adminid'):
        data=Subscribers_tb.objects.all()
        return render(request,'subscribers.html',{"subscribers":data})
    else:
        return render(request,'subscribers.html',{'error':"Login to perform Task"})



def notificationdelete(request):
    if request.session.has_key('adminid'):
        nid=request.GET['nid']
        query=Notification_tb.objects.all().filter(id=nid).update(read='True')
        return HttpResponseRedirect('/notifications/')
    else:
        return render(request,'notifications.html',{'error':"Login to perform Task"})
    
def purchasedproduct(request):
    if request.session.has_key('adminid'):
        return render(request,'purchased_product.html')

def adminlogout(request):
    if request.session.has_key('adminid'):
        del request.session['adminid']
        return HttpResponseRedirect('/')
def userlogout(request):
    if request.session.has_key('userid'):
        del request.session['userid']
        return HttpResponseRedirect('/')

def profileview(request):
    if request.session.has_key('userid'):
        uid=request.GET['uid']
        data=User_registration_tb.objects.all().filter(id=uid)
        return render(request,'profiledata.html',{'userdata':data})

def january(request):
    data=Product_tb.objects.all().filter(month='January')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def february(request):
    data=Product_tb.objects.all().filter(month='February')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def march(request):
    data=Product_tb.objects.all().filter(month='March')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def april(request):
    data=Product_tb.objects.all().filter(month='April')
    return render(request,'monthviseview.html',{'monthwisedata':data})

def may(request):
    data=Product_tb.objects.all().filter(month='May')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def june(request):
    data=Product_tb.objects.all().filter(month='June')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def july(request):
    data=Product_tb.objects.all().filter(month='July')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def august(request):
    data=Product_tb.objects.all().filter(month='August')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def september(request):
    data=Product_tb.objects.all().filter(month='September')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def october(request):
    data=Product_tb.objects.all().filter(month='October')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def november(request):
    data=Product_tb.objects.all().filter(month='November')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def december(request):
    data=Product_tb.objects.all().filter(month='December')
    if data:
        return render(request,'monthviseview.html',{'monthwisedata':data})
    else:
        return render(request,'404.html')

def addtokart(request):
    if request.session.has_key('userid'):
        return render(request,'addtokart.html')

def removeitem(request):
    if request.session.has_key('userid'):
        kid=request.GET['kid']
        Kart_tb.objects.filter(id=kid).delete()
        return HttpResponseRedirect('/login/')

def edititem(request):
    if request.session.has_key('userid'):
        kid=request.GET['kid']
        singleitem=Kart_tb.objects.filter(id=kid)
        return render(request,'single.html',{'singleitem':singleitem})

def updatecount(request):
    if request.session.has_key('userid'):
        kid=request.POST['kid']
        count=request.POST['productcount']
        query=Kart_tb.objects.all().filter(id=kid).update(productcount=count)
        return HttpResponseRedirect('/login/')

def feedback(request):
    if request.session.has_key('adminid'):
        feedback=Contact_tb.objects.all()
        return render(request,'feedback.html',{'feedbackdata':feedback})

def purchasehistory(request):
    data=Kart_tb.objects.all()
    return render(request,'purchasehistory.html',{'purchasehistorydata':data})






        

    

