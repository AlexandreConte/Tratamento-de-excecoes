# Tratamento de Exceções

Ônibus são um meio de transporte comum. Para não violar as regras de transito é importante conhecer o estado atual do ônibus (ligado ou desligado), o número de pessoas que estão dentro do ônibus no momento e a capacidade total de pessoas permitida.

As ações típicas de um ônibus são ligar, desligar e permitir ou não a entrada de um passageiro. Para isso, deve-se controlar a quantidade de pessoas que entram e saem do ônibus, se o ônibus está vazio (sem passageiros) ou se já está com a capacidade máxima.

Também deve-se controlar se o ônibus está ligado (ligado=True) ou desligado (ligado=False).

Esses controles são realizados por meio da implementação de exceções.

Implemente as exceções esperadas e dispare as exceções nos momentos devidos.

Não é necessário implementar o tratamento das exceções, pois o código de testes do Moodle já implementa esses tratamentos.

Quando o controlador inicializar o ônibus, é importante garantir que os parâmetros de inicialização sejam válidos.
Existem 4 casos que podem invalidar o comando de inicialização:

- Quando existe algum parâmetro que não é um valor inteiro ou booleano, de acordo com os respectivos tipos.
- Quando existe algum parâmetro inteiro com valor negativo.
- Se o número atual de passageiros não respeita a restrição da capacidade de passageiros dentro do ônibus.
- Se ao inicializar o ônibus for definido que o mesmo está desligado (ligado=False).

Quando qualquer um desses casos ocorrer, o comando de inicialização é considerado inválido e o ônibus deve manter seu estado anterior.

IMPORTANTE: Implemente o exercício seguindo exatamente as Classes disponibilizadas pelo professor.