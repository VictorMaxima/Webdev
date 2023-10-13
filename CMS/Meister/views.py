from django.shortcuts import render
from .models import Entry
# Create your views here.
def entries_index(request):
    return render(request, 'Meister/entry_index.html', {'entry_list': Entry.objects.all})