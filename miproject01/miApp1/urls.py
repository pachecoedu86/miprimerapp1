from django.urls import path
from miApp1.views import *

urlpatterns = [
    path("", inicio, name= "Inicio"),
    path("player/", createPlayer , name= "Players"),
    path("favorite/", sportLive, name= "Discipline"),
    path("colors/", colorFavorit, name="Colors"),
    path("strategy/", coachWinner,name= "Strategys"),
    path("sportsearch/",searchSport, name= "SearchDiscipline"),
    path("tofind/",tofind, name = "SearchResults"),

    
]
 