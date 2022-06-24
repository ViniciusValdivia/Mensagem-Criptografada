# Mensagem Criptografada
 
## Esse projeto foi inspirado por duas questões de vestibulares sobre o assunto de Matrizes:
## uma da INSPER em 2018 e outra da FUVEST em 2019.
## Ambas tratam do assunto de criptografar uma mensagem usando usando propriedades de matrizes inversas.
## (https://www.aio.com.br/questions/content/leia-o-texto-para-responder-a-questao-a-tabela-a-seguir-sera-usada-para-a)
## (https://acervo.fuvest.br/fuvest/2019/fuv2019_2fase_dia2.pdf)

## Assim a mensagem de três palavras irá produzir uma matriz de 3 linhas (uma para cada palavra) e com número de colunas igual
## ao número de letras da maior palavra (cada coluna irá corresponder a uma letra da palavra, e os campos vazios são preenchidos com *). 
## Trocamos as letras por suas posições no alfabeto, e o * por zero.

## Criamos uma matriz "A" (3x3) invertível. A matriz "A" irá criptografar a mensagem que será enviada por meio da multiplicação
## da matriz A pela matriz da mensagem (com números).
## Justificativa matemática - p.11 e 23(https://www.ime.unicamp.br/~chico/ma092/ma092_30_prop_matrizes.pdf)

## O receptor da mensagem deverá multiplicar "A inversa" pela mensagem recebida.
## O resultado deve ser igual a matriz mensagem (com número).

## Substituímos os números pela letra da posição no alfabeto (e zero por *), temos a mensagem escrita seguindo as palavras de cada linha.

## O que pode ser feito:
## - Realizar o encaminhamento por e-mail da mensagem e a matriz "A inversa"
## - Aprimorar regras de criptografia
## - Aprimorar regras de procedimento e vericação matemática
