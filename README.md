## Conteúdo
* Planejamento fatorial
* Testes de hipóteses
* Mapa de cores

## Bibliotecas
* Pandas 1.4.4
* Numpy 1.21.5
* PyDOE2 1.3.0
* Seaborn 0.11.2
* Statsmodels 0.13.2
* Scipy 1.7.3
* Matplotlib 3.5.2

## Limites
|Ingrediente|Limite superior (kg)|Limite inferior (kg)|
:---: | :---: | :---:
|Chocolate|0,5|1,5|
|Farinha|0,1|0,5|

## Enunciado
Uma padaria quer aumentar a produção de cupcakes, mas o proprietário tem dúvidas sobre como passar de uma produção em escala pequena para uma escala maior e capaz de atender mais clientes.
O proprietário precisa entender melhor a receita de modo a tirar mais proveito dela, evitando gastar dinheiro com ingredientes desnecessários. Dessa forma, será possível não produzir um número maior de cupcakes a cada fornada, aumentando seu lucro.

Dentre todos os ingredientes, aqueles que mais geram confusão são as quantidades de farinha e chocolate. É necessário descobrir como esses ingredientes afetam os cupcakes produzidos e, principalmente, elencar qual é o mais importante.
* Por exemplo, em um cenário no qual falta chocolate, será possível adicionar um pouco mais de farinha e ainda assim produzir a mesma quantidade de cupcakes?
* Se a farinha estiver cara, será possível compensar com uma maior quantidade de chocolate, mantendo a mesma produção de cupcakes?

Para pensar sobre essas questões o proprietário levantou algumas informações com colegas:
* O Lucas, que tem uma loja de bolos e já está acostumado a produzir em grandes quantidades, acredita que a farinha é o ingrediente mais importante. Além disso, Lucas afirmou que adiciona 450g de farinha e 200g de chocolate em suas receitas, seguindo essas medidas à risca. Entretanto, ele nunca trabalhou com cupcakes - ou seja, a sua resposta é apenas representativa para bolos.

* A amiga Ana, por sua vez, é apaixonada por cupcakes e está acostumada a prepará-los há muito tempo, ainda que não trabalhe em larga escala, se limitando a uma produção mais caseira com receita menos "restritas" (com ingredientes a gosto). Para ela, a farinha e o chocolate têm igual importância. No seu método, ela adiciona os ingredientes aos poucos e a olho, o que não ajuda muito o processo da Bel.

Para solucionar o problema, o proprietário da padaria decidiu controlar todo o sistema, variando a quantidade de farinha e de chocolate, e fazendo o registro do número de cupcakes produzidos a cada fornada.
Com isso, ela garamte que o sistema controlado é representativo da sua realidade de trabalho - isto é, receitas de cupcakes nas quantidades que ela precisa produzir em sua padaria. Além disso, ele também coletou os dados necessários para entender as relações entre as variáveis e até mesmo prever os resultados.

## Objetivo
Entender como a quantidade de farinha e chocolate afetam a quantidade de cupcakes produzidos.

## Receita (rende 12 porções)
> 430 g de farinha

> 130 g de chocolate

> 4 ovos

> 150 g de manteiga

> 200 g de açúcar

> 5 g de fermento

## Resultado dos ensaios (planejamento fatorial)
|Farinha|Chocolate|Quantidade|
:---: | :---: | :---:
|-1|-1|19|
|1|-1|37|
|-1|1|24|
|1|1|49|