from django.shortcuts import render

# Create your views here.
def jobMain(request):

    return render(request, 'jobplacement/jobMain.html', {})