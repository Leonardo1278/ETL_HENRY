from fastapi import FastAPI
import pandas as pd
app = FastAPI()

# Se asigna un url y se descarga el archivo necesario para poder trabajar 
url ='D:\HENRY\Proyecto Individual 1\Data'
totaldata = pd.read_csv(url)


#Iniciamos la api 
@app.get('/')
async def read_root():
    return {'Primera API 00'}





#Defino primera función
@app.get('/first/')
async def get_max_duration(anio: int,plataforma:str, tiemp:str):
    if (tiemp) =='min':
        df1 = totaldata[(totaldata['releaseYear'] == anio) & (totaldata['platform'] == plataforma) & (totaldata['medida'] == 'min')]
        time = df1.tiempo.max()
        titulo = df1[df1.tiempo==time]['title']
        titulo = titulo.to_list()
        titulo = titulo[0]
        respuesta = f'La máxima duración es para la pelicula: "{titulo}" con {time} minutos de duración '
    else:
        df1 = totaldata[(totaldata['releaseYear'] == anio) & (totaldata['platform'] == plataforma) & (totaldata['medida'] == 'Season')]
        time = df1.tiempo.max()
        titulo = df1[df1.tiempo==time]['title']
        titulo = titulo.to_list()
        titulo = titulo[0]
        
        respuesta = f'La máxima duración es para la serie "{titulo}" con {time} de duración'

    return {respuesta}


#Defino segunda función 
@app.get('/segunda/')
async def get_count_plataform(plataforma:str):
    
    peliculas = ((totaldata['type'].str.contains('Movie')) & (totaldata['platform'] == plataforma)).sum()
    series = ((totaldata['type'].str.contains('TV Show')) & (totaldata['platform'] == plataforma)).sum()
    respuesta =f'la cantidad de peliculas en {plataforma} es : {peliculas} y de series es: {series}'

    return {respuesta}


#Defino tercera función 
@app.get('/tercera/')
async def get_listedin(genero:str):
    #genero cantidad de veces que existe el genero en cada plataforma 
   cantidadnet = ((totaldata['listedIn'].str.contains(genero)) & (totaldata['platform']=='Netflix')).sum()
   cantidaddis = ((totaldata['listedIn'].str.contains(genero)) & (totaldata['platform']=='Diseny')).sum()
   cantidadhul = ((totaldata['listedIn'].str.contains(genero)) & (totaldata['platform']=='Hulu')).sum()
   cantidadama = ((totaldata['listedIn'].str.contains(genero)) & (totaldata['platform']=='Amazon')).sum()

   # comparo manualmente para ver cual es el mayor de todos y poder retornar una respuesta  
   if ((cantidadnet > cantidadhul) & (cantidadnet > cantidaddis) & (cantidadnet > cantidadama)):
    cantidadveces = ((totaldata['listedIn'].str.contains(genero)) & (totaldata['platform']=='Netflix')).sum()
    respuesta = f'La plataforma en la que más se repite el género {genero} es Netflix, con una cantidad de:{cantidadveces}'
   elif  ((cantidaddis > cantidadhul) & (cantidaddis > cantidadnet) & (cantidaddis > cantidadama)):
    cantidadveces = ((totaldata['listedIn'].str.contains(genero)) & (totaldata['platform']=='Diseny')).sum()
    respuesta = f'La plataforma en la que más se repite el género {genero} es Diseny, con una cantidad de:{cantidadveces}'
   elif  ((cantidadhul > cantidaddis) & (cantidadhul > cantidadnet) & (cantidadhul > cantidadama)):
    cantidadveces = ((totaldata['listedIn'].str.contains(genero)) & (totaldata['platform']=='Hulu')).sum()
    respuesta = f'La plataforma en la que más se repite el género {genero} es Hulu, con una cantidad de:{cantidadveces}'
   else:
    cantidadveces = ((totaldata['listedIn'].str.contains(genero)) & (totaldata['platform']=='Amazon')).sum()
    respuesta = f'La plataforma en la que más se repite el género {genero} es Amazon, con una cantidad de:{cantidadveces}'

    return {respuesta}



#Defino cuarta función 
@app.get('/cuarta/')
async def cuartaconsulta(plataforma:str):
    
    peliculas = ((totaldata['type'].str.contains('Movie')) & (totaldata['platform'] == plataforma)).sum()
    series = ((totaldata['type'].str.contains('TV Show')) & (totaldata['platform'] == plataforma)).sum()
    ambas =f'la cantidad de peliculas en {plataforma} es : {peliculas} y de series es: {series}'

    return {ambas}


    

