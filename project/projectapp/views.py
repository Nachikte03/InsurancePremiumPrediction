from django.shortcuts import render
import pickle
import numpy as np

# Create your views here.
def home(request):
    if request.method=='POST':
        age= request.POST.get('age')
        sex= request.POST.get('sex')
        bmi= request.POST.get('bmi')
        children= request.POST.get('children')
        smoker= request.POST.get('smoker')
        region= request.POST.get('region')
        model = pickle.load(open("model.pkl","rb"))
        try:
            age = int(age)
            sex = int(sex)
            bmi = float(bmi)
            children = int(children)
            smoker = int(smoker)
            region = int(region)
        except:
            data = {
                "result": "Enter Valid Values"
            }
            return render(request,'home.html',data)
        if age>70 or age<10 or bmi<8 or bmi>40 or children >5:
            data = {
                "result": "Enter Valid Values"
            }
            return render(request,'home.html',data)
        prediction = model.predict([[age,sex,bmi,children,smoker,region]])
        print(age,sex,bmi,children,smoker,region)
        data = {
            "result": "Your Predicted Premium is :  " + str(np.around(prediction[0])) + " USD"
        }
        
        return render(request,'home.html',data)
    return render(request,'home.html')