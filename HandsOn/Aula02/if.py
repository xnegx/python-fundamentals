# IDADE
# ALCOOLIZADA
# HABILITACAO

idade = int(raw_input('Qual a sua idade? '))
alcoolizada = raw_input('Esta alcoolizada? (S/N): ').upper()
habilitada = raw_input('Possui habilitacao? (S/N): ').upper()

# if idade >= 18:
#     if habilitada == 'S':
#         if alcoolizada == 'N':
#             print 'Pode seguir, meu jovem!'
#         else:
#             print 'Preso em nome da lei'
#     else:
#         print 'Preso em nome da lei'
# else:
#     print 'Preso em nome da lei'

if idade >= 18 and habilitada.lower() == 'S' and alcoolizada =='N':
    print 'Pode seguir, meu jovem!'
else:
    print 'Preso em nome da lei'
