# Regressão Logística Bayesiana

Material introdutório sobre Regressão Logística Bayesiana.

## Introdução

O Modelo de Regressão Logística (*MRL*) é bastante utilizado em estudos sobre modelos de classificação. Esse modelo não-linear é uma técnica estatística utilizada para relacionar uma variável resposta (**y**) com suas possíveis variáveis explicativas (**x**), geralmente a variável resposta é binária. Destaca-se como vantagens de uso, a sua facilidade em cálculos matemáticos e a possibilidade de interpretação dos parâmentros, o que o diferencia de outros modelos existentes. 


No *MRL*, a variável resposta é ligada com as variáveis respostas através de uma função de ligação denominada de logit. Em termos matemáticos, a função do modelo logístico é dado por: 

$$\ln \left( \frac{\pi(x_{i})}{1 - \pi(x_{i})} \right) = \bm{x}_{i}^{T} \bm{\beta}$$

Existe duas filosofia em Estatística: a frequentista e a bayesiana. A diferença básica entre elas, é que a primeira considera que o parâmetro de estimação é um valor fixo desconhecido, enquanto que na segunda, considera que o parâmetro é uma variável aleatória. 



