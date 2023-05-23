from django.shortcuts import render, redirect
from .models import movie
from .forms import movie_form

# Create your views here.


def index(request):
    film = movie.objects.all()
    context = {'movie_list': film}
    return render(request, "index.html", context)


def detail(request, movie_id):
    Movie = movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': Movie})


def add_movie(request):
    if request.method == "POST":
        Name = request.POST.get('name', )
        Year = request.POST.get('year', )
        Disc = request.POST.get('disc', )
        Poster = request.FILES['poster']
        film = movie(name=Name, disc=Disc, year=Year, poster=Poster)
        film.save()
        return redirect('/')
    return render(request, "add.html")


def update(request,id):
    Mvie = movie.objects.get(id=id)
    form = movie_form(request.POST or None, request.FILES, instance=Mvie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form': form, "movie": Mvie})


def delete (request, id):
    if request.method=="POST":
        Movie = movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
