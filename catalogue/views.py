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

    # get the first LRS resource
    lrs = LRS.objects.all()[0]
    c["lrs"] = lrs
    resources = xResource.objects.all()

    # setup xapi actor
    actor = {}
    actor["name"] = user.first_name + " " + user.last_name
    actor["mbox"] = "mailto:"+user.email
    tcactor = json.dumps(actor)

    for resource in resources:

        tcusername = lrs.username
        tckey = lrs.key
        tcurl = lrs.url

        pair = b''+(tcusername+":"+tckey)
        tchash = base64.b64encode(pair.encode('latin1'))
        
        url = resource.url + "?"
        urlparam = {}

        urlparam["tincan"] = True
        urlparam["endpoint"]=tcurl
        urlparam["auth"] = "Basic "+tchash
        #urlparam["actor"] = tcactor
        
        # urlparam += u"&activity_id="+urllib.quote("www.example.com/completed")
        urlparam["ampregistration"] = "2981c910-6445-11e4-9803-0800200c9a36"
        print(urllib.urlencode(urlparam))
        resource.tcurl = url+ urllib.urlencode(urlparam)




    c["resources"] = resources
    
    template = loader.get_template("all_resources.html")
    context = RequestContext(request, c)
    return HttpResponse(template.render(context))


