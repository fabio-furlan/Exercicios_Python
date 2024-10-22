# String são listas de bytes representando caracteres, podemos acessar suas posições usando colchetes
# por exemplo String [Posição Inicial: Posição Final]

Minha_String = 'Estudos para Analise de dados'
CPF = 'CPF:123452789'

print( type(Minha_String))
print (len(Minha_String))

print (Minha_String[0]) # acessa o primeiro elemento da str

print (Minha_String[-1]) # acessa o ultimo elemento da str

print (Minha_String[0:10]) # acessa posição do 0 ao 10 da str

print (CPF[-9:])