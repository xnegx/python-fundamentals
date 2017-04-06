#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:23:31 2017
@author: Everton
"""

try:
    print 'primeira linha'
    func()
    print 3+3
except Exception as e:
    print  'Algo errado aconteceu, abaixo o codigo de erro: '
    print e
    
print
    
def funcao(valor):
    if valor:
        raise Exception ('Deu ruim')
    
try:
    print 'primeira linha'
    funcao(True)
    print 3+3
except Exception as e:
    print  'Algo errado aconteceu, abaixo o codigo de erro: '
    print e
finally:
    print 'Sempre executa'
    
    
