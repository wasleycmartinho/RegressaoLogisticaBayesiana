# Regressão Logística Bayesiana (em contrução...)

Material introdutório sobre Regressão Logística Bayesiana.

## Introdução

O **Modelo de Regressão Logística** (*MRL*) é bastante utilizado em estudos sobre modelos de classificação. Esse modelo não-linear é uma técnica estatística utilizada para relacionar uma variável resposta (**Y**) com suas possíveis variáveis explicativas (**X**), geralmente a variável resposta é binária. Destaca-se como vantagens de uso, a sua facilidade em cálculos matemáticos e a possibilidade de interpretação dos parâmentros, o que diferencia de outros modelos existentes. 

No *MRL*, a variável resposta é ligada com as variáveis explicativas através de uma função de ligação denominada de *logit*. Em termos matemáticos, a função do modelo logístico é dado por: 

$$\ln \left( \frac{\pi(x_{i})}{1 - \pi(x_{i})} \right) = \bf{x}_{i}^{T} \bf{\beta}$$

Em que $\bf{x_{i}^{T}} = (1,x_{i1},...,x_{ip})$ é o vetor de variáveis explicativas com $i = 1,...,n$, $j = 0, 1,...,p$ e $\beta = (\beta_{0},...,\beta_{p})$ é a estimativa dos coeficientes. Caso, seja necessário descrever essa função através da chance de ocorrência ou odds da probabilidade de sucesso, pode-se definir: 

$$\frac{\pi(x_{i})}{1 - \pi(x_{i})} = \exp(\bf{x}_{i}^{T} \bf{\beta})$$

Em que **Y** será uma distribuição Bernoulli com parâmetros de sucesso $\pi(x_{i})$ e de fracasso $1 - \pi(x_{i})$. Assim, conclui-se que: 

$$P(Y = 1| X = x_{i}) = \frac{ \exp(\bf{x_{i}^{T}} \beta) }{1 + \exp(\bf{x_{i}^{T}} \beta)}$$ 

$$P(Y = 0| X = x_{i}) = \frac{1}{1 + \exp(\bf{x}_{i}^{T} \bf{\beta})}$$

Para ser obtido bons ajustes nesse modelo é necessário que a variável resposta tenha observações independentes e que a relação entre o *logit* da probabilidade de sucesso e as variáveis explicativas seja linear. 

Um dos problemas ao usar esse modelo está relacinado à possibilidade de usar variável resposta continuas de modo que seja necessário categorizar essa variável. Contudo, transformações desse tipo pode gerar problemas como incluir a seleção arbitrária do tamanho do intervalo e a seleção do ponto de corte o que pode ocasionar resultados menos precisos ou distorcidos. Com o objetivo de evitar esse problema, pode-se utilizar, como alternativa, o Modelo de Regressão Logística Bayesiana.  

O **Modelo de Regressão Logística Bayesiana** (*MRLB*) é um considerado um caso especial da Análise Discriminante Linear quando as variáveis dos fatores são todas contínuas. Em termos de equação esse modelo não difere da sua versão Clássica sendo a principal diferença entre os dois, a forma como são estimados os coeficientes de regressão.

Na versão clássica, usa-se para estimar os parâmetros o método de máxima verossimilhança, enquanto que na versão bayesiana, usa-se o método de máxima verossimilhança combinado com as informações à priori. Assim, a posteriori é proporcional a verossimilhança e a priori, conforme representação a seguir: 

$$\pi(\beta|x) \propto l(x|\beta) \times \pi(\beta)$$

É necessário identificar a distribuição a priori dos parâmetros do modelo, pois ela representa a informação inicial que foi observado nas amostras. Geralmente, aplica-se a distribuição Gaussiana, Cauchy, Uniforme, Gama ou Gama Inversa como a priori.   

De forma geral, os modelos bayesianos são complexos em termo de estimação dos parâmetros, com isso para estimar os parâmetros desse tipo de modelo é utilziado o Método de Cadeia de Markov de Monte Carlo (MCMC). O MCMC é uma amostrador de distribuições complexas sendo os mais conhecidos na literatura os amostradores de Metropolis-Hastings, Gibss Sampling e Hamiltonian Monte Carlo. 

Para avaliação do Modelo Logístico Bayesiano pode-se usar as métricas de Acurácia, Precisão, Recall e  F1, assim como usar o gráfico da Curva Roc, além de sua métrica AUC-ROC. Além do intervalos de credibilidade, distribuição posterior preditiva e Log-Score.

<!Existe duas filosofia em Estatística: a frequentista e a bayesiana. A diferença básica entre elas, é que a primeira considera que o parâmetro de estimação é um valor fixo desconhecido, enquanto que na segunda, considera que o parâmetro é uma variável aleatória.> 

## Referências
1. Alves, 2019
2. Souza et. al., 2006
3. Bezerra et. al., 2018
4. Marshall eta al. 1994
