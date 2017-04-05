#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:46:55 2017
@author: Everton
"""

idade = input('Qual sua idade ? ')

if idade >= 18:
    print 'Responda "sim" ou "nao" para as respostas abaixo..'
    habilitacao = raw_input ('Possui habilitacao ? ')
    if habilitacao.lower() == 'sim':
        alchool = raw_input ('Ingeriu bebidas alcolicas ? ')
        if alchool.lower() == 'sim':
            print 'Voce nao pode dirigir.'
        else:
            print 'Parabens , pode dirigir.'
    else:
        print 'Voce nao pode dirigir.'
else:
    print 'Voce nao pode dirigir.'