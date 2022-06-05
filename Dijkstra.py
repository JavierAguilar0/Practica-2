import random
import numpy as np
import cv2
#Distancias de los nodos
distancias=np.array([random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),
                     random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),
                     random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),
                     random.randint(1, 100),random.randint(1, 100)])
#Nombres de los nodos
nombres=np.array(['Casa','Juan Alvarez','Alcalde','Morelos','Enrique Diaz de Leon',
                  "Vallarta",'Chapultepec'])
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
j=str(distancias[9])
k=str(distancias[10])
#dijkstra    
mapa={'casa':{'Juan Alvarez':distancias[0], 'Alcalde':distancias[1]},
      'Juan Alvarez':{'Alcalde':distancias[2], 'Enrique Diaz de Leon':distancias[3]},
      'Alcalde':{'Morelos':distancias[4], 'Enrique Diaz de Leon':distancias[5]},
      'Morelos':{'Enrique Diaz de Leon':distancias[6],'Vallarta':distancias[7]},
      'Enrique Diaz de Leon':{'Vallarta':distancias[8],'Chapultepec':distancias[9]},
      'Vallarta':{'Chapultepec':distancias[10]},
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
		print("La distancia más corta desde "+str.upper(vertice)+" hasta " +str.upper(fin)
        +" es " +str(distancia[fin]))
		print("El camino más corto es: " + str(camino))
dijkstra(mapa, 'casa', 'Chapultepec')
#sumatoria de distancias
sa=distancias[0]+distancias[2]+distancias[4]+distancias[6]+distancias[8]+distancias[10]
sb=distancias[0]+distancias[2]+distancias[4]+distancias[6]+distancias[9]
sc=distancias[0]+distancias[2]+distancias[4]+distancias[7]+distancias[8]+distancias[9]
sd=distancias[0]+distancias[2]+distancias[4]+distancias[7]+distancias[10]
se=distancias[0]+distancias[2]+distancias[5]+distancias[6]+distancias[7]+distancias[10]
sf=distancias[0]+distancias[2]+distancias[5]+distancias[8]+distancias[10]
sg=distancias[0]+distancias[2]+distancias[5]+distancias[9]
sh=distancias[0]+distancias[3]+distancias[5]+distancias[4]+distancias[7]+distancias[10]
si=distancias[0]+distancias[3]+distancias[6]+distancias[7]+distancias[10]
sj=distancias[0]+distancias[3]+distancias[8]+distancias[10]
sk=distancias[0]+distancias[3]+distancias[9]
sl=distancias[1]+distancias[2]+distancias[3]+distancias[6]+distancias[7]+distancias[10]
sm=distancias[1]+distancias[2]+distancias[3]+distancias[8]+distancias[10]
sn=distancias[1]+distancias[2]+distancias[3]+distancias[9]
so=distancias[1]+distancias[4]+distancias[6]+distancias[8]+distancias[10]
sp=distancias[1]+distancias[4]+distancias[6]+distancias[9]
sq=distancias[1]+distancias[4]+distancias[7]+distancias[8]+distancias[9]
sr=distancias[1]+distancias[4]+distancias[7]+distancias[10]
ss=distancias[1]+distancias[5]+distancias[6]+distancias[7]+distancias[10]
st=distancias[1]+distancias[5]+distancias[8]+distancias[10]
su=distancias[1]+distancias[5]+distancias[9]
#Grafo con dijkstra
imagen2=255*np.ones((700,700,3),dtype=np.uint8)
cv2.circle(imagen2,(100,100),10,(0,0,0),-1)#nodo 1
cv2.circle(imagen2,(100,200),10,(0,0,0),-1)#nodo 2
cv2.circle(imagen2,(150,150),10,(0,0,0),-1)#nodo 3
cv2.circle(imagen2,(250,100),10,(0,0,0),-1)#nodo 4
cv2.circle(imagen2,(250,200),10,(0,0,0),-1)#nodo 5
cv2.circle(imagen2,(350,150),10,(0,0,0),-1)#nodo 6
cv2.circle(imagen2,(400,250),10,(0,0,0),-1)#nodo 7
#Nombres de los puntos a recorrer
cv2.putText(imagen2,nombres[0],(80,90),0,0.5,(255,0,255),1)#Nodo Origen
cv2.putText(imagen2,nombres[1],(60,230),0,0.5,(255,0,255),1)#Nodo 2
cv2.putText(imagen2,nombres[2],(165,155),0,0.5,(255,0,255),1)#Nodo 3
cv2.putText(imagen2,nombres[3],(240,90),0,0.5,(255,0,255),1)#Nodo 4
cv2.putText(imagen2,nombres[4],(200,230),0,0.5,(255,0,255),1)#Nodo 5
cv2.putText(imagen2,nombres[5],(370,155),0,0.5,(255,0,255),1)#Nodo 6
cv2.putText(imagen2,nombres[6],(350,275),0,0.5,(255,0,255),1)#Nodo Destino
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
cv2.putText(imagen2,j,(280,250),0,0.5,(255,0,0),1)#valor del vertice 5 con 7
cv2.putText(imagen2,k,(390,200),0,0.5,(255,0,0),1)#valor del vertice 6 con 7
#condiciones para elegir el camino mas corto y marcarlo
if (sa<sb and sa<sc and sa<sd and sa<se and sa<sf and sa<sg and sa<sh and sa<si and sa<sj
    and sa<sk and sa<sl and sa<sm and sa<sn and sa<so and sa<sp and sa<sq and sa<sr and sa<ss
    and sa<st and sa<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7    
if (sb<sa and sb<sc and sb<sd and sb<se and sb<sf and sb<sg and sb<sh and sb<si and sb<sj
    and sb<sk and sb<sl and sb<sm and sb<sn and sb<so and sb<sp and sb<sq and sb<sr and sb<ss
    and sb<st and sb<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(255,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(0,0,0),2)#conexion 6 con 7
if (sc<sa and sc<sb and sc<sd and sc<se and sc<sf and sc<sg and sc<sh and sc<si and sc<sj
    and sc<sk and sc<sl and sc<sm and sc<sn and sc<so and sc<sp and sc<sq and sc<sr and sc<ss
    and sc<st and sc<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(255,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(0,0,0),2)#conexion 6 con 7
if (sd<sa and sd<sb and sd<sc and sd<se and sd<sf and sd<sg and sd<sh and sd<si and sd<sj
    and sd<sk and sd<sl and sd<sm and sd<sn and sd<so and sd<sp and sd<sq and sd<sr and sd<ss
    and sd<st and sd<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (se<sa and se<sb and se<sc and se<sd and se<sf and se<sg and se<sh and se<si and se<sj
    and se<sk and se<sl and se<sm and se<sn and se<so and se<sp and se<sq and se<sr and se<ss
    and se<st and se<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (sf<sa and sf<sb and sf<sc and sf<sd and sf<se and sf<sg and sf<sh and sf<si and sf<sj
    and sf<sk and sf<sl and sf<sm and sf<sn and sf<so and sf<sp and sf<sq and sf<sr and sf<ss
    and sf<st and sf<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (sg<sa and sg<sb and sg<sc and sg<sd and sg<se and sg<sf and sg<sh and sg<si and sg<sj
    and sg<sk and sg<sl and sg<sm and sg<sn and sg<so and sg<sp and sg<sq and sg<sr and sg<ss
    and sg<st and sg<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(255,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(0,0,0),2)#conexion 6 con 7
if (sh<sa and sh<sb and sh<sc and sh<sd and sh<se and sh<sf and sh<sg and sh<si and sh<sj
    and sh<sk and sh<sl and sh<sm and sh<sn and sh<so and sh<sp and sh<sq and sh<sr and sh<ss
    and sh<st and sh<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (si<sa and si<sb and si<sc and si<sd and si<se and si<sf and si<sg and si<sh and si<sj
    and si<sk and si<sl and si<sm and si<sn and si<so and si<sp and si<sq and si<sr and si<ss
    and si<st and si<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (sj<sa and sj<sb and sj<sc and sj<sd and sj<se and sj<sf and sj<sg and sj<sh and sj<si
    and sj<sk and sj<sl and sj<sm and sj<sn and sj<so and sj<sp and sj<sq and sj<sr and sj<ss
    and sj<st and sj<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (sk<sa and sk<sb and sk<sc and sk<sd and sk<se and sk<sf and sk<sg and sk<sh and sk<si
    and sk<sj and sk<sl and sk<sm and sk<sn and sk<so and sk<sp and sk<sq and sk<sr and sk<ss
    and sk<st and sk<su):
    cv2.line(imagen2,(100,100),(100,200),(255,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(0,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(255,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(0,0,0),2)#conexion 6 con 7
if (sl<sa and sl<sb and sl<sc and sl<sd and sl<se and sl<sf and sl<sg and sl<sh and sl<si
    and sl<sj and sl<sk and sl<sm and sl<sn and sl<so and sl<sp and sl<sq and sl<sr and sl<ss
    and sl<st and sl<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (sm<sa and sm<sb and sm<sc and sm<sd and sm<se and sm<sf and sm<sg and sm<sh and sm<si
    and sm<sj and sm<sk and sm<sl and sm<sn and sm<so and sm<sp and sm<sq and sm<sr and sm<ss
    and sm<st and sm<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (sn<sa and sn<sb and sn<sc and sn<sd and sn<se and sn<sf and sn<sg and sn<sh and sn<si
    and sn<sj and sn<sk and sn<sl and sn<sm and sn<so and sn<sp and sn<sq and sn<sr and sn<ss
    and sn<st and sn<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(255,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(255,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(255,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(0,0,0),2)#conexion 6 con 7
if (so<sa and so<sb and so<sc and so<sd and so<se and so<sf and so<sg and so<sh and so<si
    and so<sj and so<sk and so<sl and so<sm and so<sn and so<sp and so<sq and so<sr and so<ss
    and so<st and so<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (sp<sa and sp<sb and sp<sc and sp<sd and sp<se and sp<sf and sp<sg and sp<sh and sp<si
    and sp<sj and sp<sk and sp<sl and sp<sm and sp<sn and sp<so and sp<sq and sp<sr and sp<ss
    and sp<st and sp<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(255,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(0,0,0),2)#conexion 6 con 7
if (sq<sa and sq<sb and sq<sc and sq<sd and sq<se and sq<sf and sq<sg and sq<sh and sq<si
    and sq<sj and sq<sk and sq<sl and sq<sm and sq<sn and sq<so and sq<sp and sq<sr and sq<ss
    and sq<st and sq<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(255,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(0,0,0),2)#conexion 6 con 7
if (sr<sa and sr<sb and sr<sc and sr<sd and sr<se and sr<sf and sr<sg and sr<sh and sr<si
    and sr<sj and sr<sk and sr<sl and sr<sm and sr<sn and sr<so and sr<sp and sr<sq and sr<ss
    and sr<st and sr<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(255,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(0,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (ss<sa and ss<sb and ss<sc and ss<sd and ss<se and ss<sf and ss<sg and ss<sh and ss<si
    and ss<sj and ss<sk and ss<sl and ss<sm and ss<sn and ss<so and ss<sp and ss<sq and ss<sr
    and ss<st and ss<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(255,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(255,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (st<sa and st<sb and st<sc and st<sd and st<se and st<sf and st<sg and st<sh and st<si
    and st<sj and st<sk and st<sl and st<sm and st<sn and st<so and st<sp and st<sq and st<sr
    and st<ss and st<su):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(255,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(0,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(255,0,0),2)#conexion 6 con 7
if (su<sa and su<sb and su<sc and su<sd and su<se and su<sf and su<sg and su<sh and su<si
    and su<sj and su<sk and su<sl and su<sm and su<sn and su<so and su<sp and su<sq and su<sr
    and su<ss and su<st):
    cv2.line(imagen2,(100,100),(100,200),(0,0,0),2)#conexion 1 con 2
    cv2.line(imagen2,(100,100),(150,150),(255,0,0),2)#conexion 1 con 3
    cv2.line(imagen2,(100,200),(150,150),(0,0,0),2)#conexion 2 con 3
    cv2.line(imagen2,(100,200),(250,200),(0,0,0),2)#conexion 2 con 5
    cv2.line(imagen2,(150,150),(250,100),(0,0,0),2)#conexion 3 con 4
    cv2.line(imagen2,(150,150),(250,200),(255,0,0),2)#conexion 3 con 5
    cv2.line(imagen2,(250,100),(250,200),(0,0,0),2)#conexion 4 con 5
    cv2.line(imagen2,(250,100),(350,150),(0,0,0),2)#conexion 4 con 6
    cv2.line(imagen2,(250,200),(350,150),(0,0,0),2)#conexion 5 con 6
    cv2.line(imagen2,(250,200),(400,250),(255,0,0),2)#conexion 5 con 7
    cv2.line(imagen2,(350,150),(400,250),(0,0,0),2)#conexion 6 con 7
#se muestra la imagen
cv2.imshow('Dijkstra',imagen2)
cv2.waitKey()