from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'sujan',
        'shital',
        'anamika'
    ]
    # return HttpResponse("<h1>this is home page</h1>")
    return JsonResponse(friends,safe=False)