from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Template, Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def view_all_resources(request):

    c ={}
    
    template = loader.get_template("all_resources.html")
    context = RequestContext(request, c)
    return HttpResponse(template.render(context))
