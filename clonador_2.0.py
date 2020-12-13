##EN EL DIRECTORIO DONDE SE QUIERA EJECUTAR SE DEBE INSTALAR EL REQUEST Y ACTIVAR EL VIRTAULENV PARA EL PROYECTO
##pipenv install requests
##pipenv shell
##baja de a 60 por hr... restricción de la api. Pendiente: Ver cómo hacer para que tome el login de github, así permite más. 

import os
import requests
##urls = ["https://github.com/ernesto-g/repo_prueba_clase1.git","https://github.com/ernesto-g/repo_prueba_clase1.git"]
#apellidos = ["flaco1_Sáraza","flaco2_adsada_asdErGómez"]
urls = []
apellidos = []
cursos = [] 

f = open("alumnos.csv","r")
while True:
	line = f.readline()
	parts = line.split(";")
	
	if len(parts)>=5:
		url = parts[4]
		api = parts[5]

		date = requests.get(api)
		date = date.json()["commit"]["author"]["date"]
		date = date[:10]
		date = date.replace("-","")
			
		if not ".git" in url:
			url = url.replace("\n","")
			url = url + ".git"
		url = url.replace("\n","")
		apellido = parts[0]
		apellido = apellido.replace(",","_")
		apellido = apellido.replace(" ","")
		apellido = apellido.replace("\n","")
		
		apellido = apellido + "_" + date
		
		curso = parts[1]
		curso = curso.replace("\n","")
		
		urls.append(url) 
		apellidos.append(apellido)
		cursos.append(curso)
	else:
		break
f.close()


i=0		
while True:
	ruta = cursos[i] + '//' + apellidos[i]
	
	cmd = "git clone "+urls[i]+" "+ruta
	
	os.system(cmd)
	
	i+=1
	if i>=len(urls):
		break


print("taran!")
  