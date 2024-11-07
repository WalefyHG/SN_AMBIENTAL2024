## Desafio SN_AMBIENTAL

### Antes de iniciar todo o processo deve-se fazer esses passos antes de tudo (Configurações Iniciais):

- Crie um ambiente virtual utilizando o seguinte comando: python -m venv venv

- Utilizei o poetry para gerenciamento de pacotes do meu projeto

## Para instalar tudo basta rodar os seguintes comandos: 

- Utilizando esse comando: venv/Scripts/activate, para ativar o ambiente virtual

- E para instalar todas as dependencias utilize: poetry install

## Configurando o Core(Nucleo) do meu projeto:

- Utilizando esse comando: **django-admin startproject core .** Para criar o nucleo do projeto, onde serão configuradas boa parte do projeto, como: Banco de dados, servidores, urls, entre outras coisas...

## Criando meus "APPS"

Para criação dos apps do projeto: utilizei esses comandos:

- python manage.py startapp usuario
- python manage.py startapp pedido
- python manage.py startapp itens_pedidos

Utilizando eles para moldar a estrutura de cada tabela do banco de dados e redirecionar suas rotas

## Banco de dados:
* Sequencia do codigo em DDL do banco de dados feito em mysql:

- CREATE DATABASE desafiosn;

- CREATE TABLE usuario(
    id int AUTO_INCREMENT not null PRIMARY KEY,
    email varchar(255) not null UNIQUE,
    senha varchar(255) not null
);

- CREATE TABLE pedido(
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    usuario_id int,
    total decimal(12,2) NOT null,
    status varchar(15) NOT null,
    data_pedido date not null,
    FOREIGN KEY(usuario_id) REFERENCES usuario(id)
);
    
- CREATE TABLE itens_pedido(
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    pedido_id int,
    nome varchar(90) not null,
    descricao varchar(130) not null,
    preco decimal(12,2) not null,
    categoria varchar(20) not null,
    FOREIGN KEY(pedido_id) REFERENCES pedido(id)
    );
