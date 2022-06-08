from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from httplib2 import Http
from .models import ReimbursementRequest as rr
from django.contrib.auth.models import User
from .forms import SubmitRequest, TrackSpending
from django.core.mail import send_mail

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
                    email_message = 'Your Reimbursement Request has been approved.\n'
                    email_message += 'If you have any problems or concerns please contact\n'
                    email_message += response.user.first_name + ' ' + response.user.last_name + '(' + response.user.email + ')\n'
                    email_message += 'Thank you'
                    # send_mail('Reimbursement Request Approved', email_message, 'v311938@gmail.com', [rr.objects.get(id=int(i)).user.email], fail_silently=False) # This only send to milesbellaire456
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

            email_message = response.user.first_name + ' ' + response.user.last_name + ' has submited a new reimbursement request.\n'
            email_message += 'They have requested $' + str(r_request.amount) + ' for ' + r_request.reason
            staff_list = []
            for user in User.objects.all():
                if user.is_staff:
                    staff_list.append(user.email)
            # send_mail('Reimbursement Request Received', email_message, 'v311938@gmail.com', staff_list, fail_silently=False)

            return HttpResponseRedirect("/current-requests")
    else:
        form = SubmitRequest()
    return render(response, "main/request.html", {"form":form})


def budget_tracking(response):
    return render(response, "main/budget_tracking.html", {})

def tracking(response):
    if response.method == "POST":
        form = TrackSpending(response.POST)
        if form.is_valid():
            print(response.POST)
    else:
        form = TrackSpending()
    return render(response, "main/tracking.html", {"form":form})

def pivot_table(response):
    return render(response, "main/pivot_table.html", {})

def spreadsheet(response):
    return render(response, "main/spreadsheet.html", {})

def index(response):
    return render(response, "main/index.html", {})