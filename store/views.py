import random
import json
from django.db.models.fields import AutoField
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import manufacture, medicine, patient, buy, bill

meds=[]
qunti=[]

def my_login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("store:billing"))
        else:
            return render(request, "store/login.html", {
                "message": "Invalid username or password."
            })
    else:
        return render(request, "store/login.html")

def billing(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        p=patient()
        p.name=name
        p.age=age
        p.sex=gender
        p.phone=phone
        p.address=address
        p.save()

        pat=patient.objects.filter(name=name).first()

        bi=bill()
        bi.pid=pat
        bi.save()

        total=0

        for i in range(0,len(meds)):
            b=buy()
            b.billid=bi
            b.mid=meds[i]
            b.qty=qunti[i]
            pri=meds[i].price
            cost=(pri/10)*(qunti[i])
            b.cost=cost
            b.save()
            total+=cost

        bi.total=total
        bi.save()
        
        meds.clear()
        return HttpResponseRedirect(reverse("store:bills"))

    med=medicine.objects.all()
    return render(request, "store/billing.html", {
        "meds" : med
    })

def bills(request):
    b=reversed(bill.objects.all())
    return render(request, "store/bills.html", {
        "bills" : b
    })

def add(request):
    if request.method == "POST":
        name = request.POST["name"]
        dosage = request.POST["dosage"]
        manu = request.POST["manu"]
        composition = request.POST["composition"]
        stock = request.POST["stock"]
        expiry = request.POST["expiry"]

        man=manufacture.objects.filter(name=manu).first()

        med=medicine()
        med.name=name
        med.dosage=dosage
        med.manu=man
        med.composition=composition
        med.stock=stock
        med.expiry=expiry
        med.save()

        return HttpResponseRedirect(reverse("store:view"))

    manufactures=manufacture.objects.all()
    return render(request, "store/add.html", {
        "manufactures" : manufactures
    })

def view(request):
    meds=reversed(medicine.objects.all())
    return render(request, "store/view.html", {
        "meds" : meds
    })

@csrf_exempt
@login_required
def med(request):
    data=json.loads(request.body)
    medi=data["medicine"]
    qty=int(data["quantity"])

    med=medicine.objects.filter(name=medi).first()
    med.stock-=qty
    med.save()

    meds.append(med)
    qunti.append(qty)

    return JsonResponse({"message": "Email sent successfully."}, status=201)