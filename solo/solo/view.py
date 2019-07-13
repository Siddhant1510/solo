from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.template import loader
from books.models import book_info , issued , book_request

def vaab_view(request):
    dataset = book_info.objects.all()
    template = loader.get_template("user/uservaab.html")
    content = {
            "dataset" : dataset,
    }
    return HttpResponse(template.render(content,request))

def index_page(request):
    return HttpResponse("<h1>Welcome To the Home Page</h1>")

def home_page(request):
    return render(request , "index.html")

def user_db(request):
    total_no_of_books = book_info.objects.count()
    total = book_info.objects.all()
    total_books = 0
    count = 1
    for i in total:
        total_books = total_books + book_info.objects.get(id=count).no_of_copies
        count = count+1
    template = loader.get_template("user/userdb.html")
    content = {
            "total_no_of_books" : total_no_of_books,
            "total_books" : total_books,
    }
    return HttpResponse(template.render(content,request))

def user_cp(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/usercp.html', {
        'form': form
    })

def user_vib(request):
    issued_books = issued.objects.all()
    dataset = book_info.objects.all()
    template = loader.get_template("user/uservib.html")
    content = {
            "issued_books" : issued_books,
            "dataset" : dataset,
    }
    return HttpResponse(template.render(content,request))

def user_sbr(request):
    if request.method == 'POST':
        if request.POST.get('book_name') and request.POST.get('book_author') and request.POST.get('comment') and  request.POST.get('user'):
            reqbook = book_request()
            reqbook.user = request.POST.get('user')
            reqbook.book_name = request.POST.get('book_name')
            reqbook.book_author = request.POST.get('book_author')
            reqbook.comment = request.POST.get('comment')
            reqbook.save()
            return render(request , "user/usersbr.html")

    else:
        return render(request , "user/usersbr.html")
