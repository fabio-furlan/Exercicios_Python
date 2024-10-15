# Comando elif: caso haja necessidade de mais condições entre o if e o else
# executa a primeiro condição verdadeira que encontrar

x = 1
y = 2

if x == y:
    print("numeros iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("y maior que x")
else:
    print("numeros diferentes")
