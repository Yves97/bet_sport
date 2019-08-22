from django.shortcuts import render
def home(request):
    return render(request,'index.html')

def score(request):
    return render(request,'pages/score.html')

def resultat(request):
    return render(request,'pages/resultat.html')
def handler404(request,exception):
    return render(request,'errors/404.html',{},status=404)
def handler500(request):
    return render(request,'errors/500.html',{},status=500)

