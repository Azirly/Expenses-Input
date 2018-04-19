from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the userindex.")
    
def detail(request, value):
    return HttpResponse("You're looking at question %s." % value)

def results(request, value):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % value)

def vote(request, value):
    return HttpResponse("You're voting on question %s." % value)