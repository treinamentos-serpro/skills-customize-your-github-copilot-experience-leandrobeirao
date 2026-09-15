# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a construir uma API REST com FastAPI, usando modelos Pydantic, rotas HTTP, validação de dados e tratamento de erros. Ao final, você terá uma API de livros que pode ser explorada pela documentação interativa gerada pelo framework.

## 📝 Tarefas

### 🛠️ Criar e Executar a API

#### Descrição
Configure o ambiente do projeto, instale FastAPI e Uvicorn e execute o código inicial. Depois, explore as páginas `/docs` e `/redoc` no navegador.

#### Requisitos
O programa concluído deve:

- Instalar `fastapi` e `uvicorn` no ambiente virtual do projeto
- Iniciar a aplicação com `uvicorn starter-code:app --reload`
- Exibir uma resposta JSON em `GET /health`
- Disponibilizar a documentação interativa em `/docs`


### 🛠️ Modelar e Validar Livros

#### Descrição
Complete o modelo `Book` para representar os dados de um livro. Use os recursos do Pydantic para validar os campos recebidos pela API.

#### Requisitos
O programa concluído deve:

- Definir um modelo `Book` com `title`, `author`, `year` e `available`
- Exigir que `title` e `author` não sejam vazios
- Validar `year` como um número entre 0 e o ano atual
- Usar `available` com valor padrão `True`
- Retornar status `422` quando o corpo da requisição for inválido


### 🛠️ Implementar Rotas CRUD

#### Descrição
Implemente as operações principais para criar, consultar, atualizar e remover livros. Os dados podem permanecer em memória durante a execução da aplicação.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` para listar todos os livros
- Implementar `GET /books/{book_id}` para buscar um livro por identificador
- Implementar `POST /books` para criar um livro e retornar status `201`
- Implementar `PUT /books/{book_id}` para atualizar um livro existente
- Implementar `DELETE /books/{book_id}` para remover um livro e retornar status `204`
- Gerar identificadores únicos para os livros criados


### 🛠️ Tratar Erros e Testar a API

#### Descrição
Torne a API previsível para quem a consome e teste os principais cenários usando a documentação do FastAPI ou um cliente HTTP.

#### Requisitos
O programa concluído deve:

- Retornar status `404` quando o identificador de um livro não existir
- Retornar mensagens JSON claras para erros de recurso não encontrado
- Definir códigos de status e respostas coerentes nas rotas
- Testar pelo menos um caso de sucesso e um caso de erro para cada operação CRUD
- Registrar no README exemplos de requisições e respostas para `POST`, `GET` e `DELETE`