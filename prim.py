# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:15:35 2022

@author: david
"""

from funciones import *
import time

def prim(G,N,A):
    
    #calculamos el trafico total de todas las aristas
    traficoAbierto = 0

    padre= inicializarACero([],len(N))
    #todos son candidatos para ser metidos en AR
    cand = inicializarATrue([],len(N))
    #distancia de cada nodo al mas cercano en AR
    D = inicializarAMenosInfinito([], len(N))
    #solucion
    sol = anadirAristas(G)
    #escogemos un nodo al azar y lo marcamos como el mas cercano
    D[0]=-1
    #indicamos que es el nodo inicial
    padre[0]=-1
    
    cont = 0
    while cont != len(N):
        #devuelve el nodo con mayor D entre aquellos cuyo Cand es true
        u = buscarMaximo(cand, D)
        #el nodo u pasa a estar en AR
        cand[u]=False
        
        if padre[u]!=-1:
            if (padre[u],u, G[padre[u]][u]) in sol:
                sol.remove((padre[u], u, G[padre[u]][u]))
                traficoAbierto = traficoAbierto + G[padre[u]][u]
            else:
                sol.remove((u,padre[u], G[padre[u]][u]))
                traficoAbierto = traficoAbierto + G[padre[u]][u]
            
        for v in adyacentes(G, u):
            if cand[v]==True and G[u][v] > D[v]:
                D[v]=G[u][v]
                padre[v]=u
        cont=cont+1
    return (traficoAbierto,len(sol),sol)




#Para facilitar las pruebas, almacenamos la direccion de los ficheros en una lista
listaPruebas = ['ficherosEntrada/1.grafo_5n_6a.txt',        'ficherosEntrada/2.grafo_15n_20a.txt',          #pruebas creadas [0-9]]
                'ficherosEntrada/3.grafo_30n_35a.txt',      'ficherosEntrada/4.grafo_100n_500a.txt',
                'ficherosEntrada/5.grafo_500n_1000a.txt',   'ficherosEntrada/6.grafo_1kn_2ka.txt',
                'ficherosEntrada/7.grafo_5kn_20ka.txt',     'ficherosEntrada/8.grafo_10kn_40ka.txt',
                'ficherosEntrada/9.grafo_25kn_60ka.txt',    'ficherosEntrada/10.grafo_50kn_100ka.txt',
                
                'ficherosEntrada/em_7n16a.txt',             'ficherosEntrada/em_9n36a.txt',                 #pruebas de egela [10-16]
                'ficherosEntrada/em_100n1000a.txt',         'ficherosEntrada/em_200n396a.txt',
                'ficherosEntrada/em_250n1273a.txt',         'ficherosEntrada/em_1000n8433a.txt',
                'ficherosEntrada/em_10000n61731a.txt']


#Almacenamos las direcciones de los ficheros de salida
listaSalida =  ['ficherosSalida/1.grafo_5n_6a_salida.txt',        'ficherosSalida/2.grafo_15n_20a_salida.txt',          #pruebas creadas [0-9]]
                'ficherosSalida/3.grafo_30n_35a_salida.txt',      'ficherosSalida/4.grafo_100n_500a_salida.txt',
                'ficherosSalida/5.grafo_500n_1000a_salida.txt',   'ficherosSalida/6.grafo_1kn_2ka_salida.txt',
                'ficherosSalida/7.grafo_5kn_20ka_salida.txt',     'ficherosSalida/8.grafo_10kn_40ka_salida.txt',
                'ficherosSalida/9.grafo_25kn_60ka_salida.txt',    'ficherosSalida/10.grafo_50kn_100ka_salida.txt',
                
                'ficherosSalida/em_7n16a_salida.txt',             'ficherosSalida/em_9n36a_salida.txt',                 #pruebas de egela [10-16]
                'ficherosSalida/em_100n1000a_salida.txt',         'ficherosSalida/em_200n396a_salida.txt',
                'ficherosSalida/em_250n1273a_salida.txt',         'ficherosSalida/em_1000n8433a_salida.txt',
                'ficherosSalida/em_10000n61731a_salida.txt']


print("Resolviendo ", listaPruebas[0], " ...")
(G,n,a) = almacenarGrafo(listaPruebas[0])
N = anadirNodos(G)
A = anadirAristas(G)

inicio= time.time()
time.sleep(1)
(trafico, tramos, S )= prim(G,N,A)
fin1=time.time()

print("tiempo antes de escribir:   ",(fin1-inicio)-1)
escribirEnFichero(trafico,tramos,S, listaSalida[0])
fin2=time.time() 
print("tiempo despues de escribir: ",(fin2-inicio)-1)
