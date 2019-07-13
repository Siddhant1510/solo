
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from books.models import book_info

def db_view(request):
    dataset = book_info.objects.all()
    template = loader.get_template("user/userdb.html")
    content = {
            "dataset" : dataset,
    }
    return HttpResponse(template.render(content,request))
