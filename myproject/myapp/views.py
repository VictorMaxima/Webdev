from django.shortcuts import render
from myapp.models import Book

# Create your views here.
def first(request):
	q = request.GET.get('q', None)
	items = ' '
	if q is None or q is "":
		Books = Book.objects.all()
		return render(request, 'myapp/index.html', {'books' : Books})
	elif q is not None:
		Books = Book.objects.filter(title__contains=q)
		return render(request, 'myapp/index.html', {'books': Books})
