#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:56:44 2017
@author: Everton
"""

# exemplos de funcoes


animais = ['tigre','boi','galinha']

def exibir_lista(lista):
    for a in lista:
        print a
        
exibir_lista(animais)
print

# funcao com parametros y=opcional,se nada for declarado ele vai assumir valor 2
def somar(x,y=2):
    return x+y

#funcao sem saber quantos argumentos 
def subtrair (*args):
    print args
    
subtrair(2,3,10,50)
print

# kwargs precisa de chaves e valores para criar um dicionario
def mutiplicar (**kwargs):
    print kwargs

mutiplicar(a=2,b=1,c=4,d=6)
print


# lambda = funcao anonima 
f = lambda x,y,z: x+y+z
print f(1,2,3)

print
# labda acima representa a funcao somarvarios abaixo
def somarvarios(x,y,z):
    return x + y + z
print somarvarios(1,2,3)

words = ['pera','uva','mamao']

print
# outro labda abaixo comparando com outra funcao
def size(words):
    return [len(w) for w in words]
print size(words)

print

def size1(words):
    lista = []
    for w in words:
        lista.append(len(w))
    return lista
 

frutas = lambda words:[len(w) for w in words]
print frutas(words)







