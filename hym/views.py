from django.shortcuts import render

def main(request):
	return render(request, 'main.html')

def accesorio(request):
	return render(request, 'accesorio.html')

def ropa(request):
	return render(request, 'ropa.html')

def imagenes(request):
	return render(request, 'imagenes.html')