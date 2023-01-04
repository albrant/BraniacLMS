from django.http import HttpResponse
from django.views.generic import View

class HelloWorldView(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hello, world!")


def hello_world(request):
    return HttpResponse("Hello, world!")


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")
