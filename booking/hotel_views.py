from django.shortcuts import render,redirect
from .models import *
from rest_framework import generics
import requests
from .serialization import *
from django.http import HttpResponse


# Create your views here.
def hotelform(request):
    k=hotel_quary.objects.all()
    kl=hotel_faqitem.objects.all()
    nav=navbar.objects.all()

    if request.method=="GET":
        #cl=requests.get("http://127.0.0.1:8000/cardsapi/")
       # res=cl.json()
        res=hotel_cards.objects.all()
        return render(request,"hotel_templates/searchform.html",{'nav':nav,'res':res,'k':k,'kl':kl})
        # return render(request,"hotel_templates/form.html",{'res':res})

class cardsapi(generics.ListCreateAPIView):
    queryset=hotel_cards.objects.all()
    serializer_class=cardsserializationclass

class cardsapi2(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_cards.objects.all()
    serializer_class=cardsserializationclass    

#...axis...#
    
class axis_api(generics.ListCreateAPIView):
    queryset=hotel_axisoffer.objects.all()
    serializer_class=hotel_axis_serialization

class axis_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_axisoffer.objects.all()
    serializer_class=hotel_axis_serialization

class axis_api1(generics.ListCreateAPIView):
    queryset=hotel_axisoffer1.objects.all()
    serializer_class=hotel_axisserialization1

class aixs_update1(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_axisoffer1.objects.all()
    serializer_class=hotel_axisserialization1


class axispolicy_api(generics.ListCreateAPIView):
    queryset=hotel_axispolicy.objects.all()
    serializer_class=hotel_axispolicy_serialization

class axispolicy_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_axispolicy.objects.all()
    serializer_class=hotel_axispolicy_serialization


def hotel_axisform(request):
    if request.method=="GET":
       # sh=requests.get("http://127.0.0.1:8000/axis_api/")
        #rdx=sh.json()
        #sk=requests.get("http://127.0.0.1:8000/axis_api1/")
        #rx=sk.json()
        #si=requests.get("http://127.0.0.1:8000/axispolicy_api/")
        #rd=si.json()
        rdx=hotel_axispolicy.objects.all()
        rx=hotel_axispolicy.objects.all()
        rd=hotel_axispolicy.objects.all()
        return render(request,"hotel_templates/axis_offer.html",{'rdx':rdx,'rx':rx,'rd':rd})

#...icici...#
    
class icici_api(generics.ListCreateAPIView):
    queryset=hotel_icicioffer.objects.all()
    serializer_class=hotel_icici_serialization

class icici_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_icicioffer.objects.all()
    serializer_class=hotel_icici_serialization

class icici_api1(generics.ListCreateAPIView):
    queryset=hotel_icicioffer1.objects.all()
    serializer_class=hotel_iciciserialization1

class icici_update1(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_icicioffer1.objects.all()
    serializer_class=hotel_iciciserialization1


class icicipolicy_api(generics.ListCreateAPIView):
    queryset=hotel_icicipolicy.objects.all()
    serializer_class=hotel_icicipolicy_serialization

class icicipolicy_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_icicipolicy.objects.all()
    serializer_class=hotel_icicipolicy_serialization


def hotel_iciciform(request):
    if request.method=="GET":
       # sh=requests.get("http://127.0.0.1:8000/icici_api/")
       # p=sh.json()
       # sk=requests.get("http://127.0.0.1:8000/icici_api1/")
       # q=sk.json()
       # si=requests.get("http://127.0.0.1:8000/icicipolicy_api/")
       # r=si.json()
        p=hotel_icicioffer.objects.all()
        q=hotel_icicioffer1.objects.all()
        r=hotel_icicioffer1.objects.all()
        return render(request,"hotel_templates/icici_offer.html",{'p':p,'q':q,'r':r})


#...HSBC...#
    
   
class hsbc_api(generics.ListCreateAPIView):
    queryset=hotel_hsbcoffer.objects.all()
    serializer_class=hotel_hsbc_serialization

class hsbc_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_hsbcoffer.objects.all()
    serializer_class=hotel_hsbc_serialization

class hsbc_api1(generics.ListCreateAPIView):
    queryset=hotel_hsbcoffer1.objects.all()
    serializer_class=hotel_hsbcserialization1

class hsbc_update1(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_hsbcoffer1.objects.all()
    serializer_class=hotel_hsbcserialization1


class hsbcpolicy_api(generics.ListCreateAPIView):
    queryset=hotel_hsbcpolicy.objects.all()
    serializer_class=hotel_hsbcpolicy_serialization

class hsbcpolicy_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_hsbcpolicy.objects.all()
    serializer_class=hotel_hsbcpolicy_serialization


def hotel_hsbcform(request):
    if request.method=="GET":
       # sh=requests.get("http://127.0.0.1:8000/hsbc_api/")
       # sp=sh.json()
       # sk=requests.get("http://127.0.0.1:8000/hsbc_api1/")
       # pq=sk.json()
       # si=requests.get("http://127.0.0.1:8000/hsbcpolicy_api/")
       # rj=si.json()
        sp=hotel_hsbcoffer.objects.all()
        pq=hotel_hsbcoffer1.objects.all()
        rj=hotel_hsbcoffer1.objects.all()
        return render(request,"hotel_templates/hsbc_offer.html",{'sp':sp,'pq':pq,'rj':rj})

#...SBI...#
    
class sbi_api(generics.ListCreateAPIView):
    queryset=hotel_sbioffer.objects.all()
    serializer_class=hotel_sbi_serialization

class sbi_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_sbioffer.objects.all()
    serializer_class=hotel_sbi_serialization

class sbi_api1(generics.ListCreateAPIView):
    queryset=hotel_sbioffer1.objects.all()
    serializer_class=hotel_sbiserialization1

class sbi_update1(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_sbioffer1.objects.all()
    serializer_class=hotel_sbiserialization1


class sbipolicy_api(generics.ListCreateAPIView):
    queryset=hotel_sbipolicy.objects.all()
    serializer_class=hotel_sbipolicy_serialization

class sbipolicy_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_sbipolicy.objects.all()
    serializer_class=hotel_sbipolicy_serialization


def hotel_sbiform(request):
    if request.method=="GET":
        #sh=requests.get("http://127.0.0.1:8000/sbi_api/")
        #ps=sh.json()
        #sk=requests.get("http://127.0.0.1:8000/sbi_api1/")
        #pk=sk.json()
        #si=requests.get("http://127.0.0.1:8000/sbipolicy_api/")
        #pspk=si.json()
        ps=hotel_sbioffer.objects.all()
        pk=hotel_sbioffer.objects.all()
        pspk=hotel_sbioffer1.objects.all()
        return render(request,"hotel_templates/sbi_offer.html",{'ps':ps,'pk':pk,'pspk':pspk})

#...KOTAK...#
    
class hotel_kotakapi(generics.ListCreateAPIView):
    queryset=hotel_kotakoffer.objects.all()
    serializer_class=hotel_kotak_serialization

class hotel_kotakupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_kotakoffer.objects.all()
    serializer_class=hotel_kotak_serialization

class hotel_kotakapi1(generics.ListCreateAPIView):
    queryset=hotel_kotakoffer1.objects.all()
    serializer_class=hotel_kotakserialization1

class hotel_kotakupdate1(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_kotakoffer1.objects.all()
    serializer_class=hotel_kotakserialization1


class hotel_kotakpolicyapi(generics.ListCreateAPIView):
    queryset=hotel_kotakpolicy.objects.all()
    serializer_class=hotel_kotakpolicy_serialization

class hotel_kotakpolicyupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_kotakpolicy.objects.all()
    serializer_class=hotel_kotakpolicy_serialization


def hotel_kotakform(request):
    if request.method=="GET":
       # sh=requests.get("http://127.0.0.1:8000/hotel_kotakapi/")
       # aib=sh.json()
        #sk=requests.get("http://127.0.0.1:8000/hotel_kotakapi1/")
        #bic=sk.json()
        #si=requests.get("http://127.0.0.1:8000/hotel_kotakpolicyapi/")
        #cid=si.json()
        aib=hotel_kotakoffer.objects.all()
        bic=hotel_kotakoffer.objects.all()
        cid=hotel_kotakoffer1.objects.all()
        return render(request,"hotel_templates/hotel_kotakoffer.html",{'aib':aib,'bic':bic,'cid':cid})


#.....BOB.....#
    
    
class hotel_bobapi(generics.ListCreateAPIView):
    queryset=hotel_boboffer.objects.all()
    serializer_class=hotel_bob_serialization

class hotel_bobupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_boboffer.objects.all()
    serializer_class=hotel_bob_serialization

class hotel_bobapi1(generics.ListCreateAPIView):
    queryset=hotel_boboffer1.objects.all()
    serializer_class=hotel_bobserialization1

class hotel_bobupdate1(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_boboffer1.objects.all()
    serializer_class=hotel_bobserialization1


class hotel_bobpolicyapi(generics.ListCreateAPIView):
    queryset=hotel_bobpolicy.objects.all()
    serializer_class=hotel_bobpolicy_serialization

class hotel_bobpolicyupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_bobpolicy.objects.all()
    serializer_class=hotel_bobpolicy_serialization


def hotel_bobform(request):
    if request.method=="GET":
       # sh=requests.get("http://127.0.0.1:8000/hotel_bobapi/")
       # bob=sh.json()
       # sk=requests.get("http://127.0.0.1:8000/hotel_bobapi1/")
       # bob1=sk.json()
       # si=requests.get("http://127.0.0.1:8000/hotel_bobpolicyapi/")
        #bob2=si.json()
        bob=hotel_boboffer.objects.all()
        bob1=hotel_boboffer.objects.all()
        bob2=hotel_boboffer1.objects.all()
        return render(request,"hotel_templates/hotel_boboffer.html",{'bob':bob,'bob1':bob1,'bob2':bob2})


#...FEDERAL...#

class federal_api(generics.ListCreateAPIView):
    queryset=hotel_federaloffer.objects.all()
    serializer_class=hotel_federal_serialization

class federal_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_federaloffer.objects.all()
    serializer_class=hotel_federal_serialization

class federal_api1(generics.ListCreateAPIView):
    queryset=hotel_federaloffer1.objects.all()
    serializer_class=hotel_federalserialization1

class federal_update1(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_federaloffer1.objects.all()
    serializer_class=hotel_federalserialization1


class federalpolicy_api(generics.ListCreateAPIView):
    queryset=hotel_federalpolicy.objects.all()
    serializer_class=hotel_federalpolicy_serialization

class federalpolicy_update(generics.RetrieveUpdateDestroyAPIView):
    queryset=hotel_federalpolicy.objects.all()
    serializer_class=hotel_federalpolicy_serialization


def hotel_federalform(request):
    if request.method=="GET":
       # sh=requests.get("http://127.0.0.1:8000/federal_api/")
       # abi=sh.json()
       # sk=requests.get("http://127.0.0.1:8000/federal_api1/")
       # bci=sk.json()
       # si=requests.get("http://127.0.0.1:8000/federalpolicy_api/")
       # cdi=si.json()
        abi=hotel_federaloffer.objects.all()
        bci=hotel_federaloffer.objects.all()
        cdi=hotel_federaloffer1.objects.all()
        return render(request,"hotel_templates/federal_offer.html",{'abi':abi,'bci':bci,'cdi':cdi})


#...quary...#
    
def hotel_cardsreg(request):
    if request.method=="POST":
        ques=request.POST['ques']
        ans=request.POST['ans']
        k=hotel_quary(ques=ques,ans=ans)
        k.save()
        return redirect("/home")
    return render(request,"hotel_templates/a.html")
      
def hotel_cardstb(request):
    if request.method=="GET":
        k=hotel_quary.objects.all()
    return render(request,"hotel_templates/tb.html",{'k':k})

def hotel_cardsup(request,id):
    if request.method=="POST":
        ques=request.POST['ques']
        ans=request.POST['ans']
        k=hotel_quary.objects.get(id=id)
        k.ques=ques
        k.ans=ans
        k.save()
        return redirect("/tb")
    return render(request,"hotel_templates/up.html")

def hotel_cardsedit(request,id):
    if request.method=="GET":
        k1=hotel_quary.objects.get(id=id)
    return render(request,"hotel_templates/up.html",{'k1':k1})

def hotel_cardsdelete(request,id):
    if request.method=="GET":
        k=hotel_quary.objects.get(id=id)
        k.delete()
        return redirect("/tb")
       
#...faq...#

def hotel_faqreg(request):
    if request.method=="POST":
        question=request.POST['question']
        answer=request.POST['answer']
        k=hotel_faqitem(question=question,answer=answer)
        k.save()
        return redirect("/hotelform")
    return render(request,"hotel_templates/faqreg.html")

def hotel_faqtab(request):
    if request.method=="GET":
        ks=hotel_faqitem.objects.all()
    return render(request,"hotel_templates/faqdata.html",{'ks':ks})

def hotel_faqedit(request,id):
    if request.method=="GET":
        k1=hotel_faqitem.objects.get(id=id)
    return render(request,"hotel_templates/faqupdate.html",{'k1':k1})

def hotel_faqupdate(request,id):
    if request.method=="POST":
        question=request.POST['question']
        answer=request.POST['answer']
        k=hotel_faqitem.objects.get(id=id)
        k.question=question
        k.answer=answer
        k.save()
        return redirect("/hotelform")
    return render(request,"hotel_templates/faqupdate.html")

def hotel_faqdelete(request,id):
    if request.method=="GET":
        k=hotel_faqitem.objects.get(id=id)
        k.delete()
    return redirect("/hotelform")           
