#region ¨¨¨MENUS¨¨¨
##1ºmenu##
def Operações_basicas():
    print("___OPERAÇÕES_BÁSICAS___")
    print("1.Adição")
    print("2.Subtração")
    print("3.Multipicação")
    print("4.Divisão")
    print("5.OPERAÇÕES COMPLEXAS")

##2ºmenu##
def Operações_complexas():
    print("\n___Operações_complexas___")
    print("1.Potencia")
    print("2.Raiz")
    print("3.Calculo de Pitagoras")
    print("4.Voltar")
#endregion
#Determina como funciona cada metodo
def modelos_contas(a, b, c, d, e): #MODELO, METODO, NUM1, NUM2, DECISOR
    if a == 1:
        if b == '1': #METODO DA ADIÇÃO
            return c + d
        elif b == '2': #METODO DA SUBTRAÇÃO
            return c - d
        elif b == '3': #METODO DA MULTIPLICAÇÃO
            return c * d
        elif b == '4': #METODO DA DIVISÃO
            return c / d
    
    elif a == 2:
        if b == '1': #METODO DA POTENCIA
            return c ** d
        elif b == '2': #METODO DA RAIZ 
            return c ** (1 / d)
        elif b == '3': #TEOREMA DE PITAGORAS
            if e == '1': #METODO DE PITAGORAS-HIPOTENUZA
                return ((c**2) + (d**2)) ** (1 / 2)
            elif e == '2': #METODO DE PITAGORAS-CATETO
                return ((c**2) - (d**2)) ** (1 / 2)

while True: #DETERMINA O INICIO E A REPETIÇÃO DA CALCULADORA
    decisor = 0 #SERVE  PARA NÃO DAR PROBLEMA NA HORA DA CONFIRMAÇÃO COM A FUNÇÃO
    def verificar(x, opcoes): #função que faz a verificação geral, usando duas variaveis
        while True: #serve para repetir o código 
            if x not in opcoes: #determina se é preciso mudar o metodo
                print("\n Você escolheu uma opção invalida")
                x = input("Digite o uma opção valida: ") #reprenetação da variavel 
            else:
                return x #atualiza a variavel

    #region O_basicas
    Operações_basicas() #mostra o menu de operações básicas pro usuario
    metodo = input("Digite o metodo escolhido: ") #Determina o metodo
    opcoes = ['1','2','3','4','5'] # opções que o usuario pode escolher
    metodo = verificar(metodo, opcoes) #VERIFICA O METODO ENTRE 1 E 5
    modelo = 1

    if metodo != '5': # é p/entrar nas variaveis das operações básicas
        if metodo in opcoes: 
            num1 = float(input("Digite o primeiro número: ")) #pede o primeiro numero
            num2 = float(input("Digite o proximo número: ")) #pede o segundo numero
  #endregion
    #region O_complexas
    if metodo == '5': # é p/entrar nas variaveis das operações complexas
        Operações_complexas()  #mostra o menu de operações complexas pro usuario
        metodo = input("digite a operação escolhida: ") #Escolhe qual o tipo de conta
        opcoes = ['1','2','3','4'] #possiveis respostas
        metodo = verificar(metodo, opcoes) #confirma se a variavel esta valida
        modelo = 2 
        
        if metodo == '1': ###POTENCIA###
            num1 = float(input("Digite a base: ")) #pede a base 
            num2 = float(input("Digite o expoente: ")) #pede qual vai ser o expoente

        elif metodo == '2': ###RADICIAÇÃO###
            num1 = float(input("Digite o número dentro da chapa: ")) #pede a base 
            num2 = float(input("Digite a base da raiz: ")) #pede qual vai ser o expoente

        elif metodo == '3': ###TEOREMA DE PITAGORAS###
            print("\n O que vc deseja achar?")
            print("1. Hipotenuza")
            print("2. Cateto")
            print("3. Voltar")
            decisor = input("")
            opcoes = ['1','2','3']
            decisor = verificar(decisor, opcoes)

            if decisor == '1': ###HIPOTENUZA###
                num1 = float(input("Digite o valor do Primiro cateto: ")) #pede o cateto
                num2 = float(input("Digite o valor do Segundo cateto: ")) #pede o cateto

            elif decisor == '2': ###CATETO###
                num1 = float(input("Digite o valor da hipotenuza: ")) #pede a hipotenuza
                num2 = float(input("Digite o valor do cateto: ")) #pede o cateto
        
    #endregion
    resultado = modelos_contas(modelo, metodo, num1, num2, decisor)
    print("O resultado da operação é:")#mostra o resultado
    print(resultado)

    #menu de reutilização
    print("Você deseja continuar usando a calculadora? (sim/não)") # o usuario quer usar
    contin = input("").lower()
    r_validas = ['sim', 'nao', 'não', 's', 'n'] #respostas aceitaveis pelo sistema
    contin = verificar(contin, r_validas) #faz a validação
    
    if contin == 'não' or contin == 'nao' or contin== 'n': #vê se a resposta esta no negativa
        break
