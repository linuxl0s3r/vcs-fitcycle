import logging
from statsd.defaults.django import statsd
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
stdlogger = logging.getLogger('django')

def index(request):
    template = get_template("polls/index.html")
    return HttpResponse(template.render())

#@csrf_protect
def signup(request):
    template = get_template("polls/signup.html")

    stdlogger.info("In signup page")

    statsd.incr('fitcycle.signup',1)
    foo_timer = statsd.timer('signupTimer')
    
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            firstname=request.POST.get('firstname','')
            lastname=request.POST.get('lastname','')
            email=request.POST.get('email','')
            stdlogger.info("creating object for saving to db")
            prospect_obj=prospect(firstname=firstname, lastname=lastname, email=email)
            try:
               stdlogger.info("About to save")
               foo_timer.start()
               prospect_obj.save()
               foo_timer.stop()
            except Exception, e:
               stdlogger.error("Error in saving: %s" % e)

            return HttpResponseRedirect(reverse('index'))

    else:
        form=PostForm()
    
#    context = RequestContext(request,{'form':form})
#    return render(request, "polls/signup.html", {'form':form})
    return HttpResponse(template.render({'form':form}, request))


