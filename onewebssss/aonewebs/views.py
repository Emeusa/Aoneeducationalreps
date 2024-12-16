from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import AeducationalForm, RegistrationForm
from .models import AoneEducational, Account

# Create your views here.


def home(response):
    return render(response, "aonewebs/home.html", {})

def rules_v(response):
    return render(response, "aonewebs/rules.html", {})

def aboutus_v(response):
    return render(response, "aonewebs/members.html", {})


def coursespage(response):
    user = response.user

    if user.is_authenticated:
        form = AeducationalForm()
        
    else:
        messages.warning(response, "Your account is about to expire.") 
        return redirect("/login")
    
    return render(response, "aonewebs/courses.html", {})



def examsform(request):
    user = request.user

    if user.is_authenticated:

        if request.method == "POST":
            form = AeducationalForm(request.POST)
            if form.is_valid():

                examform = form.save(commit=False)
                examform.owner = request.user
                examform.save()

                return redirect("/viewedit")
            
        else:

                
            form = AeducationalForm()
    else:
        return redirect("/login")
    return render(request, "aonewebs/utme.html", {"form":form})



def updateforms(request, aoneEducational_id):
    user = request.user

    if user.is_authenticated:

        uforms  =   AoneEducational.objects.get(pk=aoneEducational_id)
        form = AeducationalForm(request.POST or None, instance=uforms)
        if form.is_valid():
            form.save()
            return redirect("/viewedit")
    else:
        return redirect("/login")
    return render(request, "aonewebs/updateform.html", {"uforms":uforms, "form":form})


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"User is already authenticated as {user.email}.")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("/")
        else:
            context["registration_form"] = form

    return render(request, "aonewebs/register.html", context)


def loguserout(request):
    logout(request)
    return redirect("/login")



def formviews(response, aoneEducational_id):
    user = response.user

    if user.is_authenticated:
        ls  =   AoneEducational.objects.get(pk=aoneEducational_id)

    else:
        return redirect("/login")
    return render(response, "aonewebs/lis.html", {"ls":ls})





def viewedit(response):

    user = response.user

    if user.is_authenticated:
        
        lists  =   AoneEducational.objects.all()

    else:
        return redirect("/login")
    return render(response, "aonewebs/waecneco.html", {"lists":lists})


















'''
     pr = form.cleaned_data["profile_code"]
            ln = form.cleaned_data["last_name"]
            fn = form.cleaned_data["first_name"]
            mn = form.cleaned_data["middle_name"]
            dt = form.cleaned_data["date_of_birth"]
            ge = form.cleaned_data["gender"]
            gn = form.cleaned_data["genotype"]
            bg = form.cleaned_data["b_group"]
            mr = form.cleaned_data["marital"]
            me = form.cleaned_data["madien_name"]
            em = form.cleaned_data["email"]
            cd = form.cleaned_data["contact_add"]
            ni = form.cleaned_data["nin"]
            mi = form.cleaned_data["mobile_number"]
            na = form.cleaned_data["nationality"]
            st = form.cleaned_data["state_of_origin"]
            lg = form.cleaned_data["local_gov"]
            oc = form.cleaned_data["occupation"]
            od = form.cleaned_data["office_add"]
            ph = form.cleaned_data["phone_no"]
            pn = form.cleaned_data["parent_mail"]
            al = form.cleaned_data["alevel_pro"]
            ps = form.cleaned_data["prefered_ex_state"]
            et = form.cleaned_data["exam_town"]
            fc = form.cleaned_data["first_choices"]
            po = form.cleaned_data["programme_one"]
            sc = form.cleaned_data["second_choices"]
            pt = form.cleaned_data["programme_two"]
            uo = form.cleaned_data["utme_sub_one"]
            ut = form.cleaned_data["utme_sub_two"]
            ur = form.cleaned_data["utme_sub_three"]
            uf = form.cleaned_data["utme_sub_four"]
            ns = form.cleaned_data["name_of_sec"]
            ex = form.cleaned_data["exam_type"]
            rg = form.cleaned_data["reg_mode"]
            ye = form.cleaned_data["yr_of_exam"]
            sn = form.cleaned_data["serial_no"]
            pu = form.cleaned_data["pin_no"]
            en = form.cleaned_data["exam_no"]
            nm = form.cleaned_data["num_of_sit"]
            oo = form.cleaned_data["olevel_sub_one"]
            go = form.cleaned_data["grade1"]
            ot = form.cleaned_data["olevel_sub_two"]
            gt = form.cleaned_data["grade2"]
            oh = form.cleaned_data["olevel_sub_three"]
            gh = form.cleaned_data["grade3"]
            of = form.cleaned_data["olevel_sub_four"]
            gf = form.cleaned_data["grade4"]
            oi = form.cleaned_data["olevel_sub_five"]
            gi = form.cleaned_data["grade5"]
            ox = form.cleaned_data["olevel_sub_six"]
            gx = form.cleaned_data["grade6"]
            oe = form.cleaned_data["olevel_sub_sev"]
            ge = form.cleaned_data["grade7"]
            og = form.cleaned_data["olevel_sub_eig"]
            gg = form.cleaned_data["grade8"]
            on = form.cleaned_data["olevel_sub_nin"]
            gn = form.cleaned_data["grade9"]

'''