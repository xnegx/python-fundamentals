#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:37:16 2017

@author: Everton
"""
nome = 'Everton'

if nome:
    print 'Primeiro IF'
    if nome == 'D':
        print 'Segundo IF'
    elif nome == 'A':
        print 'Primeiro ELIF'
    elif nome == 'C':
        print 'Segundo ELIF'
    else:
        print 'Primeiro ELSE'