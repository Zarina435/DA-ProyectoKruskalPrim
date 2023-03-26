# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:36:45 2022

@author: david
"""

from funciones import *
import time
        
def kruskal(G,N,A):
    sol = anadirAristas(G)
    numNodos=0
    P = len(N)
    cand = A # Almacena las aristas
    cand = sorted(cand, key=lambda item: item[2], reverse=True) # Ordenado por el peso
 
    traficoAbierto = 0
  
    # inicializar Particion
    particion = []
    for nodo in range(P):
        particion.append(-nodo)
    
    
    while numNodos < P-1:
        (a, b, peso) = cand.pop(0)
        Ra = buscar(particion, a)
        Rb = buscar(particion, b) 
        if Ra != Rb:
            unir(particion, Ra, Rb)
            sol.remove((a,b,peso))
            numNodos+=1
            traficoAbierto+=peso
    
    return (traficoAbierto, len(sol), sol)



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
(trafico, tramos, S )= kruskal(G,N,A)
fin1=time.time()

print("tiempo antes de escribir:   ",(fin1-inicio)-1)
escribirEnFichero(trafico,tramos,S, listaSalida[0])
fin2=time.time() 
print("tiempo despues de escribir: ",(fin2-inicio)-1)