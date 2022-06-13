import random
import numpy as np

print('************************************')
print('*******MENSAGEM CRIPTOGRADAFA*******')
print('************************************')

nome1_input = input('Mensagem de:')
nome2_input = input('Mensagem para:')
msg_input = input('Escreva uma mensagem com três palavras').lower()

# Com a mensagem de três palavras montamos uma matriz de 3 linhas (uma para cada palavra)
# O número de colunas será o número de letras da maior palavra
# Cada elemento da matriz será uma letra da palavra respeitando a ordem da palavra e da letra dentro da palavra
# As linhas das palavras menores serão preenchidas por *

palavras = msg_input.split()
tamanho_palavras = [len(palavras[0]),len(palavras[1]), len(palavras[2])]
print(tamanho_palavras)
def separa_letras(self):
    letras_x = []
    k = 0
    while k < len(self):
        l = self[k]
        letras_x.append(l)
        k += 1
    return(letras_x)

letras_1 = separa_letras(palavras[0])
letras_2 = separa_letras(palavras[1])
letras_3 = separa_letras(palavras[2])

maior_palavra = (max(tamanho_palavras))
print(maior_palavra)

k1 = 1
while k1 <= (maior_palavra - len(palavras[0])):
    letras_1.append("*")
    k1 += 1

k2 = 1
while k2 <= (maior_palavra - len(palavras[1])):
    letras_2.append("*")
    k2 += 1

k3 = 1
while k3 <= (maior_palavra - len(palavras[2])):
    letras_3.append("*")
    k3 += 1


matriz = np.array([letras_1, letras_2, letras_3])
print(matriz)

# Codificamos a matriz com a posição da letra no alfabeto no lugar da sua respectiva letra
# O símbolo * será codificado por zero

alfabeto = ['*','a','b','c','d','e','f','g','h','i',
             'j','k','l','m','n','o','p','q','r',
             's','t','u','v','w','x','y','z']

def transf_msg_n(self):
    msg_numero = []
    for x in self:
      msg_numero.append(alfabeto.index(x))

    return(msg_numero)

msg_numero_1 = transf_msg_n(letras_1)
msg_numero_2 = transf_msg_n(letras_2)
msg_numero_3 = transf_msg_n(letras_3)

matriz_msg_numero = np.array([msg_numero_1,msg_numero_2,msg_numero_3])

print(matriz_msg_numero)


# Para criptografar a mensagem será criada uma matriz 3x3 (A) com valores aleatórios
# A mensagem criptografada será a matriz resultante do produto da matriz A pela matriz da mensagem com números
# Para o receptor da mensagem conseguir ler a mensagem ele deve usar a matriz inversa de A e
# multiplicar pela mensagem criptografada que recebeu
# Com a matriz resultante basta converter os valores pelas letras de sua posição

# Para que seja possível esse processo entre as matrizes é necessário verificar que:
# 1) Determinante da matriz A deve ser diferente de zero
# 2) o produto de uma matriz e pela sua inversa deve resultar na matriz identidade

# GERADOR DA MATRIZ A (CHAVE DO MENSAGEIRO)

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
d = random.randint(0,100)
e = random.randint(0,100)
f = random.randint(0,100)
g = random.randint(0,100)
h = random.randint(0,100)
i = random.randint(0,100)


A = np.array([[a,b,c],[d,e,f],[g,h,i]])
print(A)

# CONDIÇÃO DA MATRIZ A (DETERMINANTE DIFERENTE DE ZERO)
d_principal_1 = A[0][0] * A[1][1] * A[2][2]
d_principal_2 = A[1][0] * A[2][1] * A[0][2]
d_principal_3 = A[2][0] * A[0][1] * A[1][2]

d_secundaria_1 = A[0][2] * A[1][1] * A[2][0]
d_secundaria_2 = A[1][2] * A[2][1] * A[0][0]
d_secundaria_3 = A[2][2] * A[0][1] * A[1][0]

determinante_A = d_principal_1 + d_principal_2 + d_principal_3 - d_secundaria_1 - d_secundaria_2 - d_secundaria_3
print(determinante_A)

# MATRIZ INVERSA DE A (CHAVE DO RECEPTOR)
# ELEMENTOS
#a_i = (e*i - f*h)/determinante_A
#b_i = (c*h - b*i)/determinante_A
#c_i = (b*f - c*e)/determinante_A

#d_i = (f*g - d*i)/determinante_A
#e_i = (a*i - c*g)/determinante_A
#f_i = (c*d - a*f)/determinante_A

#g_i = (d*h - e*g)/determinante_A
#h_i = (b*g - a*h)/determinante_A
#i_i = (a*e - b*d)/determinante_A

# SEM DIVIDIR CADA ELEMENTO PELO DETERMINANTE DE A
A_inversa = np.array([
                [(e*i - f*h),
                (c*h - b*i),
                (b*f - c*e)],
                [(f*g - d*i),
                (a*i - c*g),
                (c*d - a*f)],
                [(d*h - e*g),
                (b*g - a*h),
                (a*e - b*d)]])


print(A_inversa)


# VERIFICAÇÃO DAS CHAVES DE SEGURANÇA

id_11 = (A[0][0] * (e*i - f*h) + A[0][1] * (f*g - d*i) + A[0][2] * (d*h - e*g)) / determinante_A
id_12 = (A[0][0] * (c*h - b*i) + A[0][1] * (a*i - c*g) + A[0][2] * (b*g - a*h)) / determinante_A
id_13 = (A[0][0] * (b*f - c*e) + A[0][1] * (c*d - a*f) + A[0][2] * (a*e - b*d)) / determinante_A

id_21 = (A[1][0] * (e*i - f*h) + A[1][1] * (f*g - d*i) + A[1][2] * (d*h - e*g)) / determinante_A
id_22 = (A[1][0] * (c*h - b*i) + A[1][1] * (a*i - c*g) + A[1][2] * (b*g - a*h)) / determinante_A
id_23 = (A[1][0] * (b*f - c*e) + A[1][1] * (c*d - a*f) + A[1][2] * (a*e - b*d)) / determinante_A

id_31 = (A[2][0] * (e*i - f*h) + A[2][1] * (f*g - d*i) + A[2][2] * (d*h - e*g)) / determinante_A
id_32 = (A[2][0] * (c*h - b*i) + A[2][1] * (a*i - c*g) + A[2][2] * (b*g - a*h)) / determinante_A
id_33 = (A[2][0] * (b*f - c*e) + A[2][1] * (c*d - a*f) + A[2][2] * (a*e - b*d)) / determinante_A

id = np.array([[id_11,id_12,id_13],[id_21,id_22,id_23],[id_31,id_32,id_33]])

print(id)

# Agora para enviar a mensagem criptografada nós multiplicamos a matriz A pela matriz codificada da mensagem


def linha_cripto(self,l):
    linha_x_cripto = []
    k = 0
    while k < maior_palavra:
        elemento = self[l][0] * matriz_msg_numero[0][k] + self[l][1] * matriz_msg_numero[1][k] + self[l][2] * matriz_msg_numero[2][k]
        linha_x_cripto.append(elemento)
        k += 1
    return(linha_x_cripto)

linha_1_cripto = linha_cripto(A,0)
linha_2_cripto = linha_cripto(A,1)
linha_3_cripto = linha_cripto(A,2)

msg_cripto = np.array([linha_1_cripto,linha_2_cripto,linha_3_cripto])

print(msg_cripto)

# O receptor de posse da matriz inversa de A, ele a multiplica pela mensagem criptografada recebida
# O resultado será a matriz da mensagem codificada pela posição das letras
# Trocando os números pelas letras de suas respectivas posições as linhas da matriz irão apresentar
# a mensagem enviada

def linha_descripto(self,l):
    linha_x_descripto = []
    k = 0
    while k < maior_palavra:
        elemento = int((self[l][0] * msg_cripto[0][k] + self[l][1] * msg_cripto[1][k] + self[l][2] * msg_cripto[2][k]) / determinante_A)
        linha_x_descripto.append(elemento)
        k += 1
    return(linha_x_descripto)

linha_1_descripto = linha_descripto(A_inversa, 0)
linha_2_descripto = linha_descripto(A_inversa, 1)
linha_3_descripto = linha_descripto(A_inversa, 2)

msg_descripto = np.array([linha_1_descripto, linha_2_descripto, linha_3_descripto])

print(msg_descripto)


def linha_recebida(self):
    linha_x_msg_recebida = []
    k = 0
    while k < len(self):
        elemento = alfabeto[self[k]]
        linha_x_msg_recebida.append(elemento)
        k += 1
    return(linha_x_msg_recebida)

linha_1_msg_recebida = linha_recebida(linha_1_descripto)
linha_2_msg_recebida = linha_recebida(linha_2_descripto)
linha_3_msg_recebida = linha_recebida(linha_3_descripto)

msg_recebida = np.array([linha_1_msg_recebida,linha_2_msg_recebida,linha_3_msg_recebida])

print(msg_recebida)

