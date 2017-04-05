i = 0

while i < 10:
    if i == 5:
        # break
        i+= 1
        continue
    print i
    i += 1

    #-------

for value in 'PYTHON':
    if value == 'T':
        continue
    print value

    #-------
animais = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais
animais.insert(1, 'tigre')
print animais
animais.remove('gato')
print animais
animais.pop()
print animais
print animais.count('tigre')
print animais
print len(animais)
print animais.index('tigre')
animais.reverse()
print animais

if 'tigre' in animais:
    print 'Encontrei o tigre'
