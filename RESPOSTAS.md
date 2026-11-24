# Respostas — Reflexão sobre os paradigmas

**Nome:** José Sandokan Lucas  
**Matrícula:** 2534856

## 1. Orientação a objetos
Quais foram as vantagens e as dificuldades de resolver o problema com classes (semanas 1 e 2)?

A vantagem foi organizar melhor o código, separando os produtos em classes e facilitando sua utilização. Também foi possível aproveitar a herança e evitar repetições. A dificuldade foi entender como funcionam as classes, os métodos, as propriedades e a composição.

## 2. Programação funcional
Quais foram as vantagens e as dificuldades de resolver o problema com funções puras, sem classes e sem laços (semanas 3 e 4)?

A vantagem foi dividir o programa em funções menores, facilitando a organização e a realização dos cálculos. A dificuldade foi desenvolver as operações sem utilizar classes e laços de repetição, além de manter os dados originais sem modificações.

## 3. Comparação
Se o governo criasse uma nova categoria de produto (por exemplo, "redução de 30%"), o que você precisaria mudar em cada versão? Qual delas seria mais fácil de alterar? Por quê?

Na orientação a objetos, seria necessário criar uma nova classe para essa categoria e definir sua alíquota. Na programação funcional, seria preciso adicionar a nova categoria ao dicionário de alíquotas e ajustar as funções. Acredito que a orientação a objetos seria mais fácil de alterar, pois permite adicionar uma nova classe sem modificar grande parte do código.

## 4. Alíquota zero
Explique, com suas palavras, por que um produto da cesta básica ainda executa o método `imposto()` em vez de "pular" o cálculo.

Porque todos os produtos utilizam o mesmo método para calcular os impostos. No caso da cesta básica, a alíquota é zero, então o cálculo acontece normalmente, mas o resultado é R$ 0,00. Isso demonstra o polimorfismo, pois cada tipo de produto possui sua própria regra de cálculo.
