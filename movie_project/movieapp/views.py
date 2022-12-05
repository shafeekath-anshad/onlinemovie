from django.shortcuts import render, redirect
from . form import MovieForm
import django.contrib.auth.models
from .models import movie


# Create your views here.
def index(request):
    obj = movie.objects.all()
    con = {
        'result': obj
    }
    return render(request, "index.html", con)


def detail(request, movie_id):
    movies = movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movies})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year=request.POST.get('year')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        movies=movie(name=name, img=img, year=year, desc=desc)
        movies.save()
        return redirect('/')
    return render(request, "add.html")

def update(request, id):
    varmovie=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=varmovie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form':form, 'movie':varmovie})

def delete(request, id):
    if request.method=='POST':
        movievar=movie.objects.get(id=id)
        movievar.delete()
        return redirect('/')
    return render(request, "delete.html")

