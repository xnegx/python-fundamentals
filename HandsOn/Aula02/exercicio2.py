#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:19:17 2017
@author: Everton
"""

idade = input('Qual sua idade ? ')
habilitacao = raw_input ('Possui habilitacao ? ')
alchool = raw_input ('Ingeriu bebidas alcolicas ? ')

if idade >= 18 and habilitacao == 'sim' and alchool =='nao':
    print 'Parabens , pode dirigir.'
else:
    print 'Voce nao pode dirigir.'