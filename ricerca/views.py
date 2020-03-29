from django.shortcuts import render

from django.http import HttpResponse

from ricerca.models import Grafo

# Create your views here.

def index(request):
	import os
	import fnmatch
	import re
	REGIONI="REG"
	PROVINCE="PROV"	
	files=fnmatch.filter(os.listdir('../../COVID-19/GRPH/'), 'REGION*')
	Grafo.objects.filter(tipo="REG").delete()
	Grafo.objects.filter(tipo="PROV").delete()
	for file in files :
		m= re.match( '[a-z,A-Z]+_(.*).png'   , file)
		if m :
			REG=m.group(1)
			print(REG)
			Grafo.objects.create( title='REGIONE '+ REG, chiave=REG,tipo="REG",data_PC="")


	files=fnmatch.filter(os.listdir('../../COVID-19/GRPH/'), 'PROVINC*')
	for file in files :
		m= re.match( '[a-z,A-Z]+_(.*).png'   , file)
		if m :
			REG=m.group(1)
			print(REG)
			Grafo.objects.create( title='PROVINCIA '+ REG, chiave=REG,tipo="PROV",data_PC="")



	return HttpResponse("Hello, world. You're at the polls index."+REGIONI)


def lista_regioni(request):
	regioni = Grafo.objects.filter(tipo="REG").order_by('chiave')
	return render(request, 'ricerca/lista_regioni.html', {'regioni': regioni})

def lista_province(request):
	province = Grafo.objects.filter(tipo="PROV").order_by('chiave')
	return render(request, 'ricerca/lista_province.html', {'province': province})

def nazionale(request):
	return render(request, 'ricerca/nazionale.html')


















