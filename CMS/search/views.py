from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage

# Create your views here.
def search(request):
    query = request.GET.get('q', None)
    results = ''
    if query:
        results = FlatPage.objects.filter(content__icontains=query)
    return render(request, 'search/search.html',{'query': query, 'results': results} )