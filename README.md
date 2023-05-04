
# APS 7 - Avalaliador e algoritmos de forca

------------------------------------------------------

Requerimentos:
- IDE (sua escolha)
- Python
- pip
    - requirements

File a rodar no IDE:
- main.py
    - necessário abrir o folder no explorer (esquerda) para acessar as funções

------------------------------------------------------

## Algoritmo: Probabilidade absoluta

Esse algoritmo é extremamente simples. Ele percorre a lista de palavras uma unica vez, e faz uma lista das letras das mais prováveis de aparecer para menos provável, e então chuta elas em ordem. Ele não verifica o tabuleiro, e sempre chuta na mesma ordem.

Ordem de chutes:
- `a, e, s, r, i, o, m, n, t, c, d, u, l, p, v, g, b, f, h, z, j, q, x, w, k, y`

------------------------------------------------------

## Algoritmo: Probabilidade de letra por rodada

Para fazer esse algoritmo, eu criei uma função que recebe a palavra sendo advinhada (com os desconhecidos sendo pontos) e o alfabeto disponivel (ou seja, sem as letras que ele chutou e errou). Exemplo:
- palavra: `cac..rr.`
- alfabetoAtual: `abcdefghijklmnopqtuvwxyz`

Ele entao utiliza _regex_ para filtrar a lista de todas as palavras, para aquelas que cabem no formato da palavra atual, tem o mesmo tamanho e contem somente as letras do alfabeto atual. Ele entao calcula a quantidade de ocorrencias de cada letra nessa lista filtrada (desconsiderando as que ja chutou), e seleciona a que aparece mais vezes. No exemplo acima, a lista de probabilidades fica assim:

- ocorrencias: `{'h': 2, 'o': 3}`

Com isso, ele seleciona a letra `o` e depois `h`, acertando a palavra `cachorro`

------------------------------------------------------

## Algoritmo: 
