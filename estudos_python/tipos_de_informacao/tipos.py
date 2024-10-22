String = str('Olá Mundo')
Inteiro = int(10)
Flutuante = float (100.5)
Complex = complex ( 1j )
Lista = list (('Maça', 'Morango'))
Tupla = tuple (('A' , 'B'))
Range = range (6)
Dicionario = dict ( nome = 'Fábio' , age=40)
Set = set(('A','B','C'))
Fronzet = frozenset(('A', 'B', 'C'))
Boleano = bool( 5 )
Bytes = bytes (5)
ByteArray = bytearray(5)
Memoryview = memoryview( bytes(5))

from datetime import datetime
Data = datetime.today().date()

print(type(String)) 