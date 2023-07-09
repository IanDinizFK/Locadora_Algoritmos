# Locadora Algoritmos
Este é um projeto que foi elaborado em Dezembro de 2022, para finalizar a disciplina de Algoritmos.
O projeto é um simples controlador de estoque, onde há duas funcionalidades (Comprador e Gerente)

* Python
* TKInter (Interface)
* PandasDB (Banco de Dados)

### Comprador (Cliente)
O comprador consegue acessar a área de produtos, onde há uma simples interface que mostra o produto e o preço, 
ao executar alguma compra, o programa registra a venda com o nome do usuário e o horário no histórico de compras e debita no estoque.

### Gerente
O gerente tem sua área específica, que ao tentar acessar, o programa gera automáticamente um token aléatorio (UUID), e envia para o email registrado dentro do código.
A aba 'Gerente' tem diversas funções, como o cadastro de novos produtos, como também consegue verificar o histórico de compras.

* A API utilizada para envio de emails não está funcionando na presente data deste commit.
  
## Pandas DB

O pandas é uma biblioteca amplamente utilizada em Python para manipulação e análise de dados. Ela fornece estruturas de dados e funções para trabalhar de forma eficiente com dados estruturados, como tabelas ou arquivos CSV.
O pandas permite ler, escrever e manipular dados em diversos formatos, realizar limpeza e transformação de dados, lidar com valores ausentes, filtrar e ordenar dados, e realizar cálculos estatísticos.

- Pandas foi utilizado como banco de dados no projeto e se mostrou bastante efetivo, porém nada seguro por utilizar Planilhas e arquivos CSV.


