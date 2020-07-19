from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def submit(request):
    q = request.GET['query']
    return HttpResponse(q)



def result(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    opt = request.GET['opt']

    if opt == "+":
        result = num1 + num2
    elif opt == "-":
        result = num1 - num2
    elif opt == "*":
        result = num1 * num2
    elif opt == "/":
        result = num1 / num2

    calcResult = str(num1) + " " + opt + " " + str(num2) + " = " + str(result)

    return render(request, 'result.html', {'calcResult': calcResult })
    #render의 매개변수는 request, 어떤 페이지 띄울지, 선택 사항(3번째)