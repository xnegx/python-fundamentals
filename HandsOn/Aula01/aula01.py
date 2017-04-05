# -*- coding: utf-8 -*-

# CONSTANTE
PI = 3.14

inteiro = 10
print type(inteiro)

decimal = 0.003
print type(decimal)

texto = "4linux Devops"
print type(texto)

dicionario = {"nome": "4linux"}
print type(dicionario)

lista = ["item1", "item2"]
print type(lista)

tupla = (1, 2, 3, "Python")
print type(tupla)


name = {
    'nome': 'Gabriel',
    'endereço': {
        'rua': 'Rua vergueiro',
        'numero': 3057
    },
    'telefone': {
        'celular': 11912344567,
        'residencial': 1112348765
    }
}
print name

# LIST
frutas = ['pera', 'uva', 'banana', ['maracuja', 'morango'], 'manga']
print frutas[3][0]

frutas[3][0] = 'abacate'

print frutas

# TUPLAS immutable
frutas = ('pera', 'uva', 'morango')
frutas[0] = 'abacate'
frutas()
print frutas
