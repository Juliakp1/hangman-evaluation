
# APS 7 - Avalaliador e algoritmos de forca
Projeto onde criamos e testamos algoritmos de forca

------------------------------------------------------

Requerimentos:
- IDE (sua escolha)
- Python
- pip
    - requirements

File a rodar no IDE:
- against.py
    - Possibilita jogada entre os algoritmos
- demo.ipynb
    - Demosntra a logica por tras dos algoritmos

------------------------------------------------------

## Algoritmo: Probabilidade absoluta

Esse algoritmo é extremamente simples. Ele percorre a lista de palavras uma unica vez, e faz uma lista das letras das mais prováveis de aparecer para menos provável, e então chuta elas em ordem. Ele não verifica o tabuleiro, e sempre chuta na mesma ordem.

Ordem de chutes:
- `a, e, s, r, i, o, m, n, t, c, d, u, l, p, v, g, b, f, h, z, j, q, x, w, k, y`

------------------------------------------------------

## Algoritmo: Probabilidade por espaço vazio

Para fazer esse algoritmo, eu criei uma função que recebe a palavra sendo advinhada (com os desconhecidos sendo pontos) e o alfabeto disponivel (ou seja, sem as letras que ele chutou e errou). Exemplo:
- palavra: `.og.rte`
- alfabetoAtual: `bcdefghijklmnopqrtuvwxyz`

Ele utiliza _regex_ para filtrar a lista de todas as palavras, para aquelas que cabem no formato da palavra atual, tem o mesmo tamanho e contem somente as letras do alfabeto atual. Para encontrar o seu chute, ele percorre as palavra e separa a probabilidade das letras em espaços, e então seleciona um espaço vazio e seleciona a maior probabilidade desse local. No exemplo acima, a lista de probabilidades fica assim:

- ocorrencias na 1a letra: `{'i': 1}`

Com isso, ele seleciona a letra `i` e eventualmente acerta a palavra `iogurte`.

------------------------------------------------------

## Algoritmo: Probabilidade de letra por rodada

Para fazer esse algoritmo, eu criei uma função que recebe a palavra sendo advinhada (com os desconhecidos sendo pontos) e o alfabeto disponivel (ou seja, sem as letras que ele chutou e errou). Exemplo:
- palavra: `cac..rr.`
- alfabetoAtual: `abcdefghijklmnopqtuvwxyz`

Ele utiliza o mesmo processo de _regex_ que o algoritmo anterior para filtrar a lista de palavras. Ele entao calcula a quantidade de ocorrencias de cada letra nessa lista filtrada, desconsiderando as que ja chutou e somente contando a letra uma vez por palavra, e seleciona a que aparece mais vezes. No exemplo acima, a lista de probabilidades fica assim:

- ocorrencias: `{'h': 2, 'o': 2}`

Com isso, ele seleciona a letra `o` e depois de rodar novamente `h`, acertando a palavra `cachorro`.

------------------------------------------------------

# Conclusão

Em ordem, a performance dos algoritmos foi de 15%, 90% e 95%. Portanto, a melhor estrategia foi a do `probabilidade de letra por rodada`, que acaba tendo uma estrategia que ganha na maior parte das vezes. Analizando a sua performance, acredito que ele está proximo do limite maximo de acertos, que acaba acontecendo por conta do limite de 5 vidas, o que não permite ele acertar palavras como:

- `fal.`

Pois ela pode ser:

- `fali, falo`

Como é provavel que ele ja tenha gastado 4 vidas anteriormente, pois qualquer palavra de 4 letras significa que os seus chutes tem menos chances de revelar uma letra, é muito provavel que ele perca essa palavra. 

Se testarmos 'falo' com o algoritmo em si, temos esse resultado:

- `.a.o`
- chutes: `a, o, c, r, g, t, n`

Algumas palavras possíveis (o que o algoritmo encontrou nesse formato):

- `caso, raso, rato, gato, tato, nado, bafo, dano, saio, sapo, pato, pano, vazo` etc.

Como so temos 5 chutes, acaba sendo impossível descobrir a palavra somente utilizando chutes de uma letra. O algoritmo conseguiria resolver mais palavras com 6 vidas, mais problemas como o acima ainda ocorreria, o que significa que tem certas palavras que são simplesmente impossíveis de advinhar com consistência, considerando que são selecionadas aleatoriamente. 
