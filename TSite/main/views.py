from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from httplib2 import Http
from .models import ReimbursementRequest as rr
from .forms import SubmitRequest

# Create your views here.

def title(response):
    return render(response, "main/title.html", {})

def current_requests(response):
    if response.user.is_staff:
        items = rr.objects.all()
        if response.method == "POST":
            skip = True
            for i in response.POST:
                if not skip:
                    rr.objects.filter(pk=int(i)).update(approved=True)
                else:
                    skip = False
                
    else:
        items = response.user.reimbursementrequest_set.all()
    return render(response, "main/current-requests.html", {"requests":items, "is_staff":response.user.is_staff})

def request(response):
    if response.method == "POST":
        form = SubmitRequest(response.POST)
        if form.is_valid():
            r_request = rr(user=response.user, reason=form.cleaned_data["reason"], amount=form.cleaned_data["amount"], payable_to=form.cleaned_data["payable_to"])
            r_request.save()
            return HttpResponseRedirect("/current-requests")
    else:
        form = SubmitRequest()
    return render(response, "main/request.html", {"form":form})


def spreadsheet(response):
    return render(response, "main/spreadsheet.html", {})