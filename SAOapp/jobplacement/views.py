from django.shortcuts import render

# Create your views here.

def mainpage(request):

    return render(request, 'jobplacement/main.html', {})

def jobMain(request):

    return render(request, 'jobplacement/jobMain.html', {})

def transRep(request):

    return render(request, 'jobplacement/trans_report.html', {})