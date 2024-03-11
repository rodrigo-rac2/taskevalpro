## TaskEvalPro: Uma API para gerenciamento de tarefas e avaliações de usuários

**TaskEvalPro** é uma aplicação que fornece uma API completa para gerenciar tarefas e avaliações de usuários. A API é fácil de usar e pode ser integrada em diversos tipos de projetos.

**Recursos:**

* **Gerenciamento de tarefas:**
    * Crie, edite e exclua tarefas.
    * Defina prioridades e prazos.
    * Acompanhe o progresso e muito mais.
* **Avaliações de usuários:**
    * Colete feedback de usuários sobre tarefas, produtos ou serviços.
    * Analise os resultados e identifique áreas de melhoria.
* **API RESTful:**
    * A API fornece endpoints para todos os recursos da aplicação.
    * Facilitando a integração com outros sistemas.

**Instalação:**

**Pré-requisitos:**

* Docker
* Docker Compose

**Etapas:**

1. Clone o repositório TaskEvalPro:

```
git clone https://github.com/rodrigo-rac2/taskevalpro.git
cd taskevalpro
```

2. Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente:

```
# Variáveis de ambiente
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=taskevalpro
```

3. Inicie os serviços com Docker Compose:

```
docker-compose up --build
```

4. Aguarde a inicialização dos serviços.

5. Acesse a API em um navegador ou cliente HTTP:

* **Usuários:** http://localhost:5100/api/usuarios
* **Tarefas:** http://localhost:5100/api/tarefas
* **Avaliações:** http://localhost:5100/api/avaliacoes

**Documentação da API:**

Consulte a documentação completa da API em: [https://developer.box.com/reference/resources/task/](https://developer.box.com/reference/resources/task/)

**Estrutura do Diretório do Projeto:**

```
taskevalpro/
├── api/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── routes.py
│   └── models.py
├── postgres-data/
├── scripts/
│   ├── ddl.taskevalpro.sql
│   └── dml.taskevalpro.sql
├── docker-compose.yml
└── README.md
```

* `api/`: Contém os arquivos da API Flask.
* `postgres-data/`: Volume Docker para o banco de dados PostgreSQL.
* `scripts/`: Scripts SQL para criação e preenchimento inicial do banco de dados.
* `docker-compose.yml`: Define e inicia os serviços com Docker Compose.
* `README.md`: Este arquivo.

**Contribuições:**

Se você tiver sugestões ou encontrar algum problema, sinta-se à vontade para contribuir com o projeto.

**Observações:**

* A documentação da API está disponível em um link externo.
* Adapte a formatação à sua preferência e ao público-alvo do projeto.

**Espero que este README.md formatado em markdown seja útil para você!**
