Aplicativo de Estoque MVC
Este repositório contém um aplicativo de controle de estoque desenvolvido em arquitetura MVC, utilizando um banco de dados local. A API foi desenvolvida em Python e o frontend em HTML, 
com o código sendo criado por Caio Henrique Andrade e Denilson Rosestolato.

##Contribuidores
Caio Henrique Andrade
Denilson Rosestolato


##Funcionalidades

Cadastro de Produtos: Permite adicionar novos produtos ao estoque, especificando nome, quantidade disponível.
Consulta de Produtos: Visualização detalhada dos produtos cadastrados, possibilitando a busca por nome
Atualização de Estoque: Capacidade de alterar a quantidade disponível de produtos, seja para adicionar novas unidades ou registrar vendas/saídas.
Relatórios: Geração de relatórios de estoque atualizado, histórico de movimentações, entre outros.

Model (Modelo): Responsável pela manipulação dos dados do estoque. interação com o banco de dados local.

View (Visualização): Interface gráfica em HTML para interação do usuário.

Controller (Controlador): Lida com as requisições do usuário e coordena as interações entre o modelo e a view.

Tecnologias Utilizadas
Backend (Python): Desenvolvimento da API utilizando Python para o processamento das requisições e manipulação dos dados.

Frontend (HTML): Implementação da interface de usuário em HTML, com CSS para estilização básica e JavaScript para interações dinâmicas (se aplicável).

Banco de Dados Local: Utilização de um banco de dados local SQLite para armazenamento persistente dos dados de estoque.



##Como Executar o Projeto
Requisitos:

Python3
Ambiente virtual (recomendado).
Configuração:

Clone este repositório para sua máquina local.
Crie um ambiente virtual e ative-o.
Instale as dependências do projeto listadas no arquivo requirements.txt.
Execução:

Navegue até o diretório do projeto.
Execute o arquivo iniciar.py e depois rode o index.html

##Acesso:

Atraves do live server, sera possivel fazer as requisições da api direto no sistema

##Documentação:

para acessa a documentação acesse localhost:5000/docs
