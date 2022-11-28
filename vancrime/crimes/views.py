from django.shortcuts import render
from .models import crime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    crime_list = crime.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(crime_list, 100)
    try: 
        crimes = paginator.page(page)
    except PageNotAnInteger: 
        crimes = paginator.page(1)
    except EmptyPage:
        crimes: paginator.page(paginator.num_pages)

    return render(request, 'hello.html', {'crimes': crimes})