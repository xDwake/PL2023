# TPC4:  Ficheiros CSV com listas e funções de agregação

(publicado em **2023.03.06**)

Cria um programa em Python que implementa um conversor de um ficheiro CSV (Comma separated values) para o formato JSON.
Para se poder realizar a conversão pretendida, é importante saber que a primeira linha do CSV dado funciona como cabeçalho
que define o que representa cada coluna.
Por exemplo, o seguinte ficheiro "`alunos.csv`":

```
Número,Nome,Curso
3162,Cândido Faísca,Teatro
7777,Cristiano Ronaldo,Desporto
264,Marcelo Sousa,Ciência Política
```
Que corresponde a uma tabela com 3 registos de informação: a primeira linha de cabeçalho identifica os campos de cada registo, `Número`, `Nome`, `Curso`, e as linhas seguintes contêm os registos de informação.

No entanto, os CSV recebidos poderão conter algumas extensões cuja semântica se explica a seguir:

### 1. Listas

No cabeçalho, cada campo poderá ter um número `N` que representará o número de colunas que esse campo abrange.
Por exemplo, imaginemos que ao exemplo anterior se acrescentou um campo `Notas`, com `N = 5` ("`alunos2.csv`"):

```
Número,Nome,Curso,Notas{5},,,,,
3162,Cândido Faísca,Teatro,12,13,14,15,16
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,18
```

Isto significa que o campo Notas abrange 5 colunas (reparem que se colocaram os campos que sobram a vazio, para o
**CSV bater certo**).

### 2. Listas com um intervalo de tamanhos

Para além de um tamanho único, podemos também definir um intervalo de tamanhos `{N, M}`, significando que o número de
colunas de um certo campo pode ir de `N` até `M` ("`alunos3.csv`"):

```
Número,Nome,Curso,Notas{3,5},,,,,
3162,Cândido Faísca,Teatro,12,13,14,,
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,
```

À semelhança do ponto anterior, havendo colunas vazias, os separadores têm de estar lá, o número de colunas deverá ser sempre igual ao valor máximo de colunas, poderão é estar preenchidas com informação ou não.

### 3. Funções de agregação

Para além de listas, podemos ter funções de agregação, aplicadas a essas listas.
Veja os seguintes exemplos: "`alunos4.csv`"

```
Número,Nome,Curso,Notas{3,5}::sum,,,,,
3162,Cândido Faísca,Teatro,12,13,14,,
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,
```

 e "`alunos5.csv`":

 ```
Número,Nome,Curso,Notas{3,5}::media,,,,,
3162,Cândido Faísca,Teatro,12,13,14,,
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,
 ```

## Resultados esperados

O resultado final esperado é um ficheiro JSON resultante da conversão dum ficheiro CSV.
Por exemplo, o ficheiro "`alunos.csv`" (original), deveria ser transformado no seguinte ficheiro "`alunos.json`":

```
[
  {
    "Número": "3612",
    "Nome": "Cândido Faísca",
    "Curso": "Teatro"
  },
  {
    "Número": "7777",
    "Nome": "Cristiano Ronaldo",
    "Curso": "Desporto"
  },
  {
    "Número": "264",
    "Nome": "Marcelo Sousa",
    "Curso": "Ciência Política"
  }
]
```

No caso de existirem listas, os campos que representam essas listas devem ser mapeados para listas em JSON ("`alunos2.csv ==> alunos2.json`"):

```
[
  {
    "Número": "3612",
    "Nome": "Cândido Faísca",
    "Curso": "Teatro",
    "Notas": [12,13,14,15,16]
  },
  {
    "Número": "7777",
    "Nome": "Cristiano Ronaldo",
    "Curso": "Desporto",
    "Notas": [17,12,20,11,12]
  },
  {
    "Número": "264",
    "Nome": "Marcelo Sousa",
    "Curso": "Ciência Política",
    "Notas": [18,19,19,20,18]
  }
]
```

Nos casos em que temos uma lista com uma função de agregação, o processador deve executar a função associada à lista, e
colocar o resultado no JSON, identificando na chave qual foi a função executada ("`alunos4.csv ==> alunos4.json`"):

```
[
  {
    "Número": "3612",
    "Nome": "Cândido Faísca",
    "Curso": "Teatro",
    "Notas_sum": 39
  },
  {
    "Número": "7777",
    "Nome": "Cristiano Ronaldo",
    "Curso": "Desporto",
    "Notas_sum": 72
  },
  {
    "Número": "264",
    "Nome": "Marcelo Sousa",
    "Curso": "Ciência Política",
    "Notas_sum": 76
  }
]
```

#### Outros...

Se tiverem tempo e vontade podem sempre estender este enunciado acrescentando outras funções de agregação (maior, menor, ...), a possibilidade de termos mais de uma função de agregação em simultâneo num ficheiro, ... a creatuvidade no seu melhor...
