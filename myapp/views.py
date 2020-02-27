from django.shortcuts import render
from django.contrib.auth import models
from . import models


# Create your views here.

def index(request):
    question=models.Question.objects.get(id=1)
    choice=models.Choice.objects.all()
    print(choice[0])
    return render(request,'index.html',{'question':question,'choice':choice})

def select(request):
    question=models.Question.objects.get(id=1)
    choice=models.Choice.objects.all()
    choice_sel=models.Choice.objects
    if request.method=='POST':
        c=request.POST.get('choice_c')
        if c=='A':
           var= models.Choice.objects.get(id=1)
           var.votes+=1
           var.save()
           print("vote: A")
           print(models.Choice.objects.get(id=1).votes)
        elif c=='B':
           var= models.Choice.objects.get(id=2)
           var.votes+=1
           var.save()
           print("vote: B")
           print(models.Choice.objects.get(id=2).votes)
        elif c=='C':
           var= models.Choice.objects.get(id=3)
           var.votes+=1
           var.save()
           print("vote: C")
           print(models.Choice.objects.get(id=3).votes)
        return render(request,'index.html',{'question':question,'choice':choice})
