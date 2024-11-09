
# Desafio SN_AMBIENTAL 2024

 Desenvolver uma API REST para o gerenciamento de pedidos de um restaurante. A API permitirá que os usuários possam registrar os pedidos de clientes em um balcão de atendimento. 

## Antes de iniciar precisamos fazer as configurações iniciais

Neste projeto foi utilizado as seguintes tecnologias: Django Ninja e MySQL

Ao baixar o projeto deverá ser utilizados esses comandos:

```
Criando o ambiente virtual: python -m venv venv

Ative o ambiente virtual: venv/Scripts/activate

Instalando o poetry: pip install poetry

Instalando todas os pacotes: poetry install
```

Na pasta **core** no arquivo **settings.py** atualize os dados para conectar com o banco de dados MySQL

```
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'localhost',  # IP do banco
        'PORT': '3306',  # Porta padrão do MySQL
    }
}
```

Depois de configurar faça as devidas migrações:

```
Fazendo as migrações: python manage.py makemigrations

Aplicando as migrações: python manage.py migrate
```

Depois de realizar devidas migrações, poderá utilizar esse codigo para povoar o banco de dados com usuarios de teste

```
Comando para povoar as tabelas: python manage.py populate_db
```

## Ligando o servidor

Depois de todas as configurações desse projeto, pode ligar o servidor para utilizar, usando esse comando:

```
Iniciando o servidor: python manage.py runserver
```

_Importante: Precisa ligar o seu servidor de banco de dados para funcionar_

## Acessando as rotas

Depois de iniciar o servidor, você poderar ver as rotas e usar as mesmas, acessando o docs:

- 127.0.0.1/docs

_Caso esteja rodando no seu servidor local_


## Relizando os testes

Foi feito nesse projeto um teste para cada rota da API e para realizar os teste, utilize esses comandos:

```
Testes das rotas do usuario: pytest usuario/tests.py

Testes das rotas dos pedidos: pytest pedido/tests.py

Teste das rotas de itens: pytest itens_pedidos/tests.py
```

Com isso serão testadas todas as rotas possiveis e realizado os testes possiveis

## Banco de Dados em DDL

Esse é o banco de dados em DDL

```
- Criando o banco de dados

CREATE DATABASE desafiosn;

- Selecionando a database 

USE DATABASE desafiosn;

- Criando as tabelas

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    total DECIMAL(12, 2) NOT NULL,
    status VARCHAR(15) NOT NULL,
    data_pedido DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE itens_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    nome VARCHAR(90) NOT NULL,
    descricao VARCHAR(130),
    preco DECIMAL(12, 2) NOT NULL,
    categoria VARCHAR(20) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);

- Inserindo nas tabelas

INSERT INTO usuario (nome, email, senha) VALUES 
('João Silva', 'joao.silva@email.com', 'senha123'),
('Maria Oliveira', 'maria.oliveira@email.com', 'senha456'),
('Pedro Santos', 'pedro.santos@email.com', 'senha789'),
('Ana Costa', 'ana.costa@email.com', 'senha321');

INSERT INTO pedido (usuario_id, total, status, data_pedido) VALUES 
(1, 150.00, 'pendente', '2023-10-01'),
(2, 200.50, 'entregue', '2023-10-02'),
(3, 300.00, 'em_preparacao', '2023-10-04'),
(4, 120.00, 'a_caminho', '2023-10-05');

INSERT INTO itens_pedido (pedido_id, nome, descricao, preco, categoria) VALUES 
(1, 'Refrigerante', 'Refrigerante de cola', 5.00, 'bebida'),
(2, 'Torta de Limão', 'Sobremesa de limão', 15.00, 'sobremesa'),
(3, 'Salada Caesar', 'Salada com frango grelhado', 30.00, 'salada'),
(4, 'Bolo de Chocolate', 'Bolo de chocolate com cobertura', 20.00, 'sobremesa');

```


## Considerações finais

As partes que eu achei mais dificeis de implementar foram:

- A parte de autenticação, visto que, eu utilizei AbstractUser para autenticar com o email e senha feita no banco de dados, antes dava uma confusão por conta do username, já que, quando criava duas contas, a segunda não era criada por conta do username que era povoado como vazio. Por isso, utilizei um arquivo o **signals.py**, para instanciar um username diferente para cada usuario criado.

- Utilizei apps diferentes para cada entidade, organizando eles e juntando todas as rotas na pasta **core**, no arquivo **api.py** ele controla todas as rotas que foram cadastradas nos apps.

- Utilizei o pytest para criar todos os testes de cada aplicativo, rodando totalmente bem e funcional.

- Não utilizei docker nesse projeto, mas tentei ao maximo atender todas os requerimentos que foram possiveis.


_FIM DO PROJETO_