from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.loader import get_template
from django.template import RequestContext
from .forms import PostForm
from .models import prospect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#from django.views.decorators.csrf import csrf_protect

def index(request):
    template = get_template("polls/index.html")
    return HttpResponse(template.render())

#@csrf_protect
def signup(request):
    template = get_template("polls/signup.html")
    
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            firstname=request.POST.get('firstname','')
            lastname=request.POST.get('lastname','')
            email=request.POST.get('email','')
            prospect_obj=prospect(firstname=firstname, lastname=lastname, email=email)
            prospect_obj.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form=PostForm()
    
#    context = RequestContext(request,{'form':form})
#    return render(request, "polls/signup.html", {'form':form})
    return HttpResponse(template.render({'form':form}, request))


