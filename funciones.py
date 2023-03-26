# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:01:26 2022

@author: david
"""
import random

'''En este fichero se guardan las funciones auxiliares que se necesiten'''

#Dada una particion de un nodo, devuelve la etiqueta del conjunto al que pertenece el nodo
def buscar(particion, a):
    aux = a
    while particion[aux] > 0:
        aux = particion[aux]
    
    return aux


#Dada una partición y dos nodos, una ambos nodos en una unica particion
def unir(particion, a, b):
    if particion[a] < particion[b]:
        particion[b] = a
    elif particion[a] == particion[b]:
        particion[a] = particion[a] -1
    else:
        particion[a] = b
              

#dada una lista vacia y su tamano, devuelve la lista inicializada a true
#posible entrada: lista=[], 3
#posible salida: lista= [true, true, true]
def inicializarATrue(lista,N):
    for i in range(N):
        lista.append(True)
    return lista


#Dada una lista vacia y un tamano, anade las posiciones y las rellena con 0
def inicializarACero(lista,N):
    for i in range(N):
        lista.append(0)
    return lista


#dada una lista vacia y su tamano, devuelve la lista inicializada a infinito
#posible entrada: lista=[], 3
#posible salida: lista= [inf, inf, inf]
def inicializarAMenosInfinito(lista, N):
    for i in range(N):
        lista.append(float('-inf'))
    return lista


#dado un grafo (G) inserta en una lista todos sus nodos
def anadirNodos(G):
    N=[]
    for i in range(len(G)):
        N.append(i)
    return N


#dado un grafo (G) inserta en una lista todas sus aristas y su peso
def anadirAristas(G):
    A=[]
    for i in range(len(G)):
        for j in range(i, len(G)):
            if G[i][j]>0:
                A.append((i,j,G[i][j]))
                
    return A


#dado un grafo (G) calcula el volumen de trafico total (el peso total de las aristas) PARA PRUEBAS
def calcularTrafico(G):        
    total=0
    for i in range(len(G)):
        for j in range(i,len(G)):
            total=total+G[i][j]
    return total
            
    
#dada una lista de nodos y una lista de distancias D, devuelve el nodo con mayor D de entre aquellos cuyo cand es true
def buscarMaximo(cand,D):
    aux= float('-inf')
    sol=0
    for i in range(len(D)):
        if cand[i]==True and D[i]>aux:
            aux=D[i]
            sol=i
    return sol


#dado un grafo (G) y un nodo (n), devuelve una lista de nodos adyacentes a n
def adyacentes(G, n):
    lista=[]
    for i in range(len(G)):
        if G[n][i]>0:
            lista.append(i)
    return lista


#dada la direccion de un fichero con la informacion del grafo, guarda dicha informacion en las variables G (matriz 2x2), N (valor) y A (valor)
def almacenarGrafo(direccion):
    f = open(direccion, 'r')
    N = int(f.readline())
    A = int(f.readline())
    G=[]
    
    for i in range(N):
        G.append([])
        for j in range(N):
            G[i].append(0)
    linea = f.readline()
    
    while linea != "":
        vLinea = linea.split(" ")        
        i= int(vLinea[0])
        j= int(vLinea[1])
        G[i][j]= float(vLinea[2])
        G[j][i]= float(vLinea[2])
        linea = f.readline()
    return (G,N,A)


#Dados el trafico total de los tramos abiertos, el numero de tramos cortados, y la lista de tramos a cortar, escribe la informacion en un fichero con el nombre indicado
def escribirEnFichero(trafico,tramosCerrados,S, direccion):
    f = open(direccion, 'w')
    f.write(str(trafico))
    f.write('\n')
    f.write(str(tramosCerrados))
    f.write('\n')
    for i in range(len(S)):
        f.write(str(S[i][0]))
        f.write(' ')
        f.write(str(S[i][1]))
        f.write(' ')
        f.write(str(S[i][2]))
        f.write('\n')
    f.close()


#Dado un numero de nodos y de aristas, genera un grafo aleatorio y lo escribe en un fichero
def generarGrafo(nodos, aristas):
    listaNodos = list(range(nodos))
    listaPesos = list(range(1,50))
    listaAristas = []
    f = open("grafo1.txt",'w')
    f.write(str(nodos))
    f.write('\n')
    f.write(str(aristas))
    f.write('\n')
    i=0
    while i < aristas:
        nodo1 = listaNodos[i % nodos]
        if i < nodos-1:
            nodo2 = listaNodos[(i % nodos)+1]
        elif i==nodos-1:
            nodo2 = 0
        else:
            nodo2 = random.choice(listaNodos)
        if nodo1 != nodo2:
            if (nodo1,nodo2) not in listaAristas:
                listaAristas.append((nodo1,nodo2))
                f.write(str(nodo1))
                f.write(' ')
                f.write(str(nodo2))
                f.write(' ')
                f.write(str(random.choice(listaPesos)))
                f.write('\n')
                i=i+1 
    f.close()