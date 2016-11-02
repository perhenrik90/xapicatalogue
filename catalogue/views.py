import base64
import json
import urllib
import binascii

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Template, Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from models import LRS, xResource

# Create your views here.
def view_all_resources(request):

    c ={}
    
    user = request.user
    safe = '~()*!.\''
    
    # get the first LRS resource
    lrs = LRS.objects.all()[0]
    c["lrs"] = lrs
    resources = xResource.objects.all()

    # setup xapi actor
    actor = {}
    actor['name'] = user.first_name + " " + user.last_name
    actor['mbox'] = "mailto:"+user.email
    tcactor = json.dumps(actor)
    print(tcactor)

    for resource in resources:

        tcusername = lrs.username
        tckey = lrs.key
        tcurl = lrs.url

        pair = u''+(tcusername+":"+tckey)
        tchash = base64.b64encode(pair)
        
        url = resource.url + "?"
        urlparam = {}

        urlparam["tincan"] = "true"
        urlparam["endpoint"]=tcurl
        urlparam["auth"] = urllib.quote("Basic "+tchash)
        urlparam["actor"] = urllib.quote(tcactor, safe)

        urlpara = "tincan=true&"
        urlpara += "endpoint="+urlparam["endpoint"]
        urlpara += "&auth="+urlparam["auth"]
        urlpara += "&actor="+urlparam["actor"]

        print("\n\n"+urlpara)
        urlparam["activity_id"] = urllib.quote("www.example.com/course")
        urlparam["registration"] = urllib.quote("2981c910-6445-11e4-9803-0800200c9a36")

        resource.tcurl = url+ urlpara
                



    c["resources"] = resources
    
    template = loader.get_template("all_resources.html")
    context = RequestContext(request, c)
    return HttpResponse(template.render(context))


