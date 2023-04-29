from django.shortcuts import render

# Create your views here.
def filters(request):

    d={'data':'pyTHOn fUlL STack DEvelOPMent'}
    
    return render(request,'filters.html',d)