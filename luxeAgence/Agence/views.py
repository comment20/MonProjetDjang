from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import JsonResponse 
from .models import Note
import requests
import joblib


from django.views.decorators.csrf import csrf_exempt
import numpy as np



def home(request):
    return render(request,'home.html')

# maintenant definissons les champs de notre formulaire dans la base de données


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



def login(request):
   
    return render(request,'login.html')



# definition de la fonction prediction
@csrf_exempt
def predict_series(request):
    if request.method == 'POST':
        data = request.POST
        # Charger le modèle et faire la prédiction
        try:
            model = joblib.load(r"C:\Users\GENIUS ELECTRONICS\Music\MonProjetDjang\luxeAgence\data\logreg.joblib")
            print('le model est bien appeller')
            X = np.array([[
               float(data['francais']),
                float(data['histoire_geo']),
                float(data['anglais']), 
                float(data['mathematiques']), 
                float(data['physique_chimie'])]])
            prediction_class=None
            prediction=model.predict(X)[0]
            if (prediction==0):
                prediction_class='Série A'
            elif(prediction==1):
                prediction_class=' Série C'
            else:
                prediction_class='Série Technique'
            
            return JsonResponse({'prediction': prediction_class})
        except Exception as e:
            print(f"Erreur de prédiction : {e}")
            return JsonResponse({'error': 'Erreur de prédiction'})
    return JsonResponse({'error': 'Méthode non autorisée'})


       

#fonction note
@csrf_exempt
def note(request):
    if request.method == 'POST':
        data = request.POST
        note = Note(francais=data['francais'], 
                    histoire_geo=data['histoire_geo'], 
                    anglais=data['anglais'],
                    mathematiques=data['mathematiques'], 
                    physique_chimie=data['physique_chimie'])
        note.save()
        print("Note sauvegardée")
        url = ' http://127.0.0.1:8000/predict/'
        response = requests.post(url, data=data)
        print("Requête POST envoyée")
        if response.status_code == 200:
            try:
                prediction = response.json().get('prediction')
                print("Prédiction faite")
            except Exception as e:
                print(f"Erreur de décodage JSON : {e}")
                prediction = None
        else:
            print(f"Erreur de requête : {response.status_code}")
            prediction = None
        if prediction is not None:
            print("la prediction est :",prediction)
            print("Redirection vers la page résultat")
            return redirect('resultats', prediction=prediction)
        else:
            print("Erreur de prédiction")
            return render(request, 'note.html', {'error': 'Erreur de prédiction'})
    print("Retour à la page note")
    return render(request, 'note.html')
    
       
      
       


# definissons la fonction qui vas nous afficher le resultat
def resultats_view(request, prediction):
   # serie_mapping = {0: 'Série A', 1:' Série C'}
    #nom_serie = serie_mapping[int(prediction)]
    return render(request, 'resultats.html', {'prediction': prediction})


# Create your views here.

