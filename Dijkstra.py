import random
import numpy as np
import cv2
#Distancias de los nodos
distancias=np.array([random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100)])
#Nombres de los nodos
nombres=np.array(['Casa','Juan Alvarez','Alcalde','Morelos','Enrique Diaz de Leon','Chapultepec'])
#Conversion de los valores de enteros a string
a=str(distancias[0])
b=str(distancias[1])
c=str(distancias[2])
d=str(distancias[3])
e=str(distancias[4])
f=str(distancias[5])
g=str(distancias[6])
h=str(distancias[7])
i=str(distancias[8])
#dijkstra    
mapa={'casa':{'Juan Alvarez':distancias[0], 'Alcalde':distancias[1]},
      'Juan Alvarez':{'Alcalde':distancias[2], 'Enrique Diaz de Leon':distancias[3]},
      'Alcalde':{'Morelos':distancias[4], 'Enrique Diaz de Leon':distancias[5]},
      'Morelos':{'Enrique Diaz de Leon':distancias[6],'Chapultepec':distancias[7]},
      'Enrique Diaz de Leon':{'Chapultepec':distancias[8]},
      'Chapultepec':{}}

def dijkstra(mapa, vertice, fin):
	distancia={}
	avanzado={}
	restante=mapa
	infinito=9999999
	camino=[]

	for nodo in restante:
		distancia[nodo]=infinito
	distancia[vertice]=0

	while restante:
		nodominimo=None
		for nodo in restante:
			if nodominimo is None:
				nodominimo=nodo
			elif distancia[nodo]<distancia[nodominimo]:
				nodominimo=nodo

		for siguiente, peso in mapa[nodominimo].items():
			if peso + distancia[nodominimo]<distancia[siguiente]:
				distancia[siguiente]=peso+distancia[nodominimo]
				avanzado[siguiente]=nodominimo
		restante.pop(nodominimo)

	actual=fin
	while actual!=vertice:
		try:
			camino.insert(0,actual)
			actual=avanzado[actual]
		except KeyError:
			print("No es posible continuar el camino")
			break
	camino.insert(0,vertice)
	if distancia[fin]!=infinito:
		print("La distancia más corta desde " + str.upper(vertice) + " hasta " + str.upper(fin) + " es " + str(distancia[fin]))
		print("El camino más corto es: " + str(camino))

dijkstra(mapa, 'casa', 'Chapultepec')
#sumatoria de distancias
sa=distancias[0]+distancias[2]+distancias[4]+distancias[6]+distancias[8]
sb=distancias[0]+distancias[2]+distancias[4]+distancias[7]
sc=distancias[0]+distancias[2]+distancias[5]+distancias[6]+distancias[7]
sd=distancias[0]+distancias[2]+distancias[5]+distancias[8]
se=distancias[0]+distancias[3]+distancias[5]+distancias[4]+distancias[7]
sf=distancias[0]+distancias[3]+distancias[6]+distancias[7]
sg=distancias[0]+distancias[3]+distancias[8]
sh=distancias[1]+distancias[2]+distancias[3]+distancias[6]+distancias[7]
si=distancias[1]+distancias[2]+distancias[3]+distancias[8]
sj=distancias[1]+distancias[4]+distancias[6]+distancias[8]
sk=distancias[1]+distancias[4]+distancias[7]
sl=distancias[1]+distancias[5]+distancias[6]+distancias[7]
sm=distancias[1]+distancias[5]+distancias[8]
#Grafo con dijkstra
imagen2=255*np.ones((700,700,3),dtype=np.uint8)
cv2.circle(imagen2,(100,100),10,(0,0,0),-1)#nodo 1
cv2.circle(imagen2,(100,200),10,(0,0,0),-1)#nodo 2
cv2.circle(imagen2,(150,150),10,(0,0,0),-1)#nodo 3
cv2.circle(imagen2,(250,100),10,(0,0,0),-1)#nodo 4
cv2.circle(imagen2,(250,200),10,(0,0,0),-1)#nodo 5
cv2.circle(imagen2,(350,150),10,(0,0,0),-1)#nodo 6
#Nombres de los puntos a recorrer
cv2.putText(imagen2,nombres[0],(80,90),0,0.5,(255,0,255),1)#Nodo Origen
cv2.putText(imagen2,nombres[1],(60,230),0,0.5,(255,0,255),1)#Nodo B
cv2.putText(imagen2,nombres[2],(165,155),0,0.5,(255,0,255),1)#Nodo C
cv2.putText(imagen2,nombres[3],(240,90),0,0.5,(255,0,255),1)#Nodo D
cv2.putText(imagen2,nombres[4],(200,230),0,0.5,(255,0,255),1)#Nodo E
cv2.putText(imagen2,nombres[5],(370,155),0,0.5,(255,0,255),1)#Nodo Destino
#valores de los vertices
cv2.putText(imagen2,a,(80,150),0,0.5,(255,0,0),1)#valor del vertice 1 con 2
cv2.putText(imagen2,b,(125,125),0,0.5,(255,0,0),1)#valor del vertice 1 con 3
cv2.putText(imagen2,c,(130,180),0,0.5,(255,0,0),1)#valor del vertice 2 con 3
cv2.putText(imagen2,d,(160,215),0,0.5,(255,0,0),1)#valor del vertice 2 con 5
cv2.putText(imagen2,e,(185,120),0,0.5,(255,0,0),1)#valor del vertice 3 con 4
cv2.putText(imagen2,f,(200,175),0,0.5,(255,0,0),1)#valor del vertice 3 con 5
cv2.putText(imagen2,g,(260,150),0,0.5,(255,0,0),1)#valor del vertice 4 con 5
cv2.putText(imagen2,h,(300,125),0,0.5,(255,0,0),1)#valor del vertice 4 con 6
cv2.putText(imagen2,i,(300,190),0,0.5,(255,0,0),1)#valor del vertice 5 con 6

if sa<sb and sa<sc and sa<sd and sa<se and sa<sf and sa<sg and sa<sh and sa<si and sa<sj and sa<sk and sa<sl and sa<sm:
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
if sb<sa and sb<sc and sb<sd and sb<se and sb<sf and sb<sg and sb<sh and sb<si and sb<sj and sb<sk and sb<sl and sb<sm:
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
if sc<sa and sc<sb and sc<sd and sc<se and sc<sf and sc<sg and sc<sh and sc<si and sc<sj and sc<sk and sc<sl and sc<sm:
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
if sd<sa and sd<sb and sd<sc and sd<se and sd<sf and sd<sg and sd<sh and sd<si and sd<sj and sd<sk and sd<sl and sd<sm:
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
if se<sa and se<sb and se<sc and se<sd and se<sf and se<sg and se<sh and se<si and se<sj and se<sk and se<sl and se<sm:
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
if sf<sa and sf<sb and sf<sc and sf<sd and sf<se and sf<sg and sf<sh and sf<si and sf<sj and sf<sk and sf<sl and sf<sm:
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
if sg<=sa and sg<=sb and sg<=sc and sg<=sd and sg<=se and sg<=sf and sg<=sh and sg<=si and sg<=sj and sg<=sk and sg<=sl and sg<=sm:
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
if sh<sa and sh<sb and sh<sc and sh<sd and sh<se and sh<sf and sh<sg and sh<si and sh<sj and sh<sk and sh<sl and sh<sm:
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
if si<sa and si<sb and si<sc and si<sd and si<se and si<sf and si<sg and si<sh and si<sj and si<sk and si<sl and si<sm:
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
if sj<sa and sj<sb and sj<sc and sj<sd and sj<se and sj<sf and sj<sg and sj<sh and sj<si and sj<sk and sj<sl and sj<sm:
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
if sk<sa and sk<sb and sk<sc and sk<sd and sk<se and sk<sf and sk<sg and sk<sh and sk<si and sk<sj and sk<sl and sk<sm:
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
if sl<sa and sl<sb and sl<sc and sl<sd and sl<se and sl<sf and sl<sg and sl<sh and sl<si and sl<sj and sl<sk and sl<sm:
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
if sm<=sa and sm<=sb and sm<=sc and sm<=sd and sm<=se and sm<=sf and sm<=sg and sm<=sh and sm<=si and sm<=sj and sm<=sk and sm<=sl:
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
cv2.imshow('Dijkstra',imagen2)
cv2.waitKey()