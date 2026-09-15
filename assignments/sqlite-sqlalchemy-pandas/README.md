# 📘 Atividade: Persistência de Dados com SQLite, SQLAlchemy e pandas

## 🎯 Objetivo

Construa um programa Python que armazene registros de livros em um banco SQLite usando SQLAlchemy e transforme os dados em análises com pandas. Ao final, você terá um fluxo reproduzível que vai da criação das tabelas à geração de um relatório em CSV.

## 📝 Tarefas

### 🛠️ Modelar o Banco de Dados

#### Descrição
Configure a conexão com um banco SQLite local e complete o modelo `Book` no código inicial. O modelo deve representar o catálogo de livros fornecido no arquivo `books.csv`.

#### Requisitos
O programa concluído deve:

- Criar o arquivo de banco `library.db` sem depender de um servidor externo
- Definir uma tabela `books` usando SQLAlchemy ORM
- Usar `id` como chave primária e armazenar título, autor, ano, gênero e disponibilidade
- Definir tipos adequados para todas as colunas
- Criar as tabelas automaticamente quando o programa for executado


### 🛠️ Inserir e Consultar Registros

#### Descrição
Leia o arquivo `data.csv` e implemente as funções que inserem livros no banco e consultam o catálogo. Evite duplicar registros quando o programa for executado mais de uma vez.

#### Requisitos
O programa concluído deve:

- Carregar os registros de `books.csv` com pandas
- Inserir os livros no banco dentro de uma transação SQLAlchemy
- Impedir ou identificar a inserção duplicada de um mesmo livro
- Implementar uma consulta que retorne apenas livros disponíveis
- Implementar uma consulta que filtre livros por gênero
- Fechar ou confirmar a sessão corretamente após cada operação


### 🛠️ Analisar os Dados com pandas

#### Descrição
Converta o resultado das consultas em DataFrames e produza indicadores sobre o catálogo. As análises devem usar os dados armazenados no banco, e não o CSV diretamente.

#### Requisitos
O programa concluído deve:

- Ler os livros do SQLite para um DataFrame usando pandas
- Calcular a quantidade de livros por gênero
- Calcular a quantidade e a média do ano de publicação por autor
- Identificar o gênero com mais livros disponíveis
- Tratar corretamente resultados vazios e valores ausentes


### 🛠️ Gerar um Relatório Reproduzível

#### Descrição
Organize o programa em funções e gere um relatório final para que outra pessoa possa repetir o processo do zero. Compare os resultados antes e depois de uma atualização no banco.

#### Requisitos
O programa concluído deve:

- Separar conexão, criação de tabelas, carga de dados, consultas e análise em funções
- Executar o fluxo completo a partir de um único ponto de entrada
- Exportar o resumo por gênero para `genre-summary.csv`
- Exibir no terminal pelo menos três indicadores calculados
- Documentar no código como apagar o banco e executar o fluxo novamente
- Produzir os mesmos resultados quando executado duas vezes com o mesmo CSV