from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon


def index(request):
    pokemons = Pokemon.published.all()
    return render(
        request, 
        "index.html",
        {'pokemons':pokemons}
        )
    

def single(request, id):
    page = get_object_or_404(
        Pokemon,
        id=id,
        status=Pokemon.Status.PUBLISHED
    )
    return render(
        request, 
        "single.html",
        {'pokemon':page}
        )

