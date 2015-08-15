from django.shortcuts import *
from django.template.context import RequestContext

# Create your views here.
def home(request) :
    return render_to_response('blog/index.hamlpy', RequestContext(request, {'activetab': 'home'}))

def base(request) :
  return render_to_response('blog/blog.hamlpy', RequestContext(request, {'activetab': 'blog'}))
