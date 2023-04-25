# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import joblib

model = joblib.load('static/RandomForestRegressor')

# Create your views here.
from django.http import HttpResponse

def homes(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def prediction(request):

    if request.method != 'POST':
        return render(request, 'prediction.html')
    age = int(request.POST.get('age'))
    sex = int(request.POST.get('sex'))
    bmi = float(request.POST.get('bmi'))
    children = int(request.POST.get('children'))
    smoker = int(request.POST.get('smoker'))
    region = int(request.POST.get('region'))

    pred = round(model.predict([[age, sex, bmi, children, smoker, region]])[0])
    print(pred)

    output = {"output": pred}

    return render(request, 'prediction.html', output)

