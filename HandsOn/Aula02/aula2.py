lista = ['java', 'php', 'python']

for item in lista:
	print 'iterando item %s' % item
	if item == "python":
		print "Encontrado!"
else:
	print "nao foi possivel encontrar o python"
