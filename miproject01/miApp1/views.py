from django.shortcuts import render
from django.http import HttpResponse
from miApp1.forms import jugadorFormulario
from miApp1.forms import sportFormulario
from miApp1.forms import colorFormulario 
from miApp1.forms import coachFormulario
from miApp1.models import *

# Create your views here.

def inicio(request):

    return render(request,"miApp1/inicio.html")

def player(request):

    play1 = Player(name= "Eduardo", surname= "Pacheco", age= 36 ,email= "eleduardo30@gmail.com" )
    play1.save()

    return render(request,"miApp1/player.html")

def discipline(request):
    
    sport1 = favoriteSport(sport= "Basquet ball", country= "Buenos Aires")    
    sport1.save()

    return render (request,"miApp1/favorite.html")

def color(request):

    multicolor1 = favoriteColor(color1= "Azul", color2= "Amarillo")
    multicolor1.save()

    return render (request,"miApp1/colors.html" )

def coach(request):

    technical= favoriteCoach(name= "Phil", surname= "Jackson", age= 54 )
    technical.save()

    return render (request, "miApp1/strategy.html")


def createPlayer(request):

    if request.method == "POST":

        formulario1 = jugadorFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            play1 = Player(name=info["name"],surname=info["surname"],age=info["age"],email=info["email"])

            play1.save()

            return render(request, "miApp1/inicio.html")

    else:
        formulario1 = jugadorFormulario()  
                 
        
    return  render(request,"miApp1/player.html", {"form1": formulario1})


def sportLive(request):

    if request.method == "POST":

        formulario2 = sportFormulario(request.POST)

        if formulario2.is_valid():

            info2 = formulario2.cleaned_data

            sport1 = favoriteSport( sport=info2["sport"] , country=info2["country"]) 

            sport1.save()

            return render (request, "miApp1/inicio.html")

    else:
        formulario2 = sportFormulario()     

    return render(request,"miApp1/favorite.html", { "form2" : formulario2})    


def colorFavorit(request):
    if request.method == "POST":

        formulario3 = colorFormulario(request.POST)

        if formulario3.is_valid():

            info3 = formulario3.cleaned_data

            multicolor1=favoriteColor(color1=info3["color1"], color2=info3["color2"]) 

            multicolor1.save()  

            return render (request,"miApp1/inicio.html")

    else:
        formulario3 = colorFormulario()

    return render(request,"miApp1/colors.html", {"form3" : formulario3})   



def coachWinner(request):
    if request.method == "POST":

        formulario4 = coachFormulario(request.POST)

        if formulario4.is_valid():

            info4 = formulario4.cleaned_data

            technical= favoriteCoach(name = info4["name"] , surname = info4["surname"],age = info4["age"])

            technical.save()

            return render (request,"miApp1/inicio.html")

    else:
        formulario4 = coachFormulario()

    return render(request,"miApp1/strategy.html" , {"form4" : formulario4})  
      

def searchSport(request):

    return render(request, "miApp1/inicio.html")

def tofind(request):
    
    if request.GET["sport"]:

       sport = request.GET["sport"] 

       country = favoriteSport.objects.filter(sport__iexact=sport)

       return render (request, "miApp1/results.html", {"country": country , "sport": sport})


    else:

        answer = "You didn't send data."


    return HttpResponse (answer)    

    

        

     







                    

               
                        


        
        

        

       









    
