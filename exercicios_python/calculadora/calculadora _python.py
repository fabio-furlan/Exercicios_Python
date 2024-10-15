# coding: utf-8

# ## -------------------- Python Calculator --------------------

# ### Selecione o numero da operação desejada
#
# #### 1 - Soma
# #### 2 - Subtração
# #### 3 - Multiplicação
# #### 4 - Divisão

# In[3]:


while True:
    operacao = input(
        '0peracoes( \n1_soma, \n2_subtracao, \n3_multiplicacao, \n4_divisao) \nQual operacao deseja fazer? ')
    if operacao == 'sair' or operacao == 'Sair':
        break
    elif operacao == '1' or operacao == '2' or operacao == '3' or operacao == '4':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    else:
        print(' Operacao invalida')
    if operacao == '1':
        total = num1 + num2
        print(total)
    elif operacao == '2':
        total = num1 - num2
        print(total)
    elif operacao == '3':
        total = num1 * num2
        print(total)
    elif operacao == '4':
        total = num1 / num2
        print(total)
