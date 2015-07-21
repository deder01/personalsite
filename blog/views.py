from django.shortcuts import *
from django.template.context import RequestContext

# Create your views here.
def hello(request):
    name = "Bogo"
    html = "<html><body>Hi %s from views.py. </body></html>" %name
    return HttpResponse(html)

def hello_template(request) :
    name="Bogo"
    return render_to_response('hello.html', RequestContext(request, {'name':name}))
