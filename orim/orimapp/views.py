from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('orimapp/index.html')
    context = {
        'asdf': 'asdf'
    }
    return HttpResponse(template.render(context, request))
