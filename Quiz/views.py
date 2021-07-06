from django.shortcuts import render, redirect
from django.http import HttpResponse
from json import dumps
from .models import Dummy,Student_data


def home(request):
    request.session['logged_in']=False
    return render(request, 'Quiz/index.html',{'title':"Login Form"})

def sign_up(request):
    return render(request, 'Quiz/sign_up.html',{'title':"Sign Up Form"})

def quiz(request):
    try:
        if request.session['logged_in']==True:
            data = Dummy.objects.all()
            ques = []
            for i in data:
                options = [i.options1,i.options2,i.options3,i.options4]
                values = {
                    'numb': i.number,
                    'question': i.question,
                    'answer':i.answer,
                    'options':options
                }
                ques.append(values)
            dataJSON = dumps(ques)
            content = {
                'title':'Quiz',
                'data': dataJSON
            }
            return render(request, 'Quiz/quiz.html', content)
        else:
            return HttpResponse("<h1>You have not logged in </h1>")
    except:
        return HttpResponse("<h1>You have not logged in </h1>")

def login_submission(request):
    ID = request.POST["e-mailID"]
    request.session['ID'] = ID
    data = Student_data.objects.filter(id=ID)
    Password = request.POST["password"]
    for i in data:
        if i.Password == Password:
            request.session['logged_in']=True
            return redirect(quiz)

    return HttpResponse("<h1>User name or password is incorrect<h1>")

def signup_submission(request):
    ID = request.POST["e-mailID"]
    Password = request.POST["password"]
    values = Student_data(id = ID,Password = Password,Time_take = 0,score = 0)
    values.save()
    return redirect(home)

def score_submission(request):
    try:
        if request.session['logged_in']==True:
            ID = request.session['ID']
            data = Student_data.objects.get(id=ID)
            score=request.GET.get('result')
            time = request.GET.get('time')
            print("Score: ",score)
            print("time: ",time)
            data.score = score
            data.Time_take = time
            data.save()
            return redirect(home)
    except:
        return HttpResponse("<h1>You have not logged in </h1>")


