from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Index</h1>")
 
def url_name(request):
    message = request.GET.get("message")
    name = request.GET.get("name")
    return HttpResponse(f"<h1>Hello {name}! {message}!</h1>")