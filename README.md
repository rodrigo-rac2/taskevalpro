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
* **Front-end em React:**
    * Interface amigável e responsiva para uma melhor experiência do usuário.


**Instalação e Execução:**

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

5. Acesse a aplicação web em um navegador: http://localhost:5000

6. Se desejar, acesse a API em um navegador ou cliente HTTP:

* **Usuários:** http://localhost:5100/api/usuarios
* **Tarefas:** http://localhost:5100/api/tarefas
* **Avaliações:** http://localhost:5100/api/avaliacoes

## Usando a Coleção Postman para a API TaskEvalPro

Para facilitar o teste e a interação com a API TaskEvalPro, fornecemos uma coleção Postman que contém exemplos de solicitações para todos os endpoints disponíveis. Siga os passos abaixo para importar e usar a coleção em sua instância do Postman.

### Importando a Coleção para o Postman

1. Abra o Postman em seu computador.
2. No canto superior esquerdo, clique no botão `Import`.
3. Na janela de importação, vá até a aba `File` e clique em `Upload Files`.
4. Navegue até o diretório do projeto TaskEvalPro, encontre e selecione o arquivo `api/doc/postman-collection.json`.
5. Clique em `Open` para carregar o arquivo e, em seguida, em `Import` para adicionar a coleção ao seu Postman.

### Utilizando a Coleção

Após importar a coleção para o Postman, você verá uma lista de requests organizados por categorias, representando os diferentes endpoints da API TaskEvalPro. Cada request inclui um exemplo de corpo da solicitação (quando aplicável) e parâmetros de configuração. Siga os passos abaixo para enviar um request:

1. Expanda a coleção TaskEvalPro no painel lateral do Postman para ver os requests disponíveis.
2. Clique em um dos requests para abrir os detalhes.
3. Verifique e, se necessário, modifique os detalhes do request, incluindo headers, corpo da solicitação e parâmetros de URL.
4. Clique no botão `Send` para executar o request.
5. Observe a resposta recebida na parte inferior da janela do Postman.

### Dicas Importantes

- **Variáveis de Ambiente:** Para facilitar o uso da coleção em diferentes ambientes (desenvolvimento, teste, produção), considere configurar [variáveis de ambiente no Postman](https://learning.postman.com/docs/sending-requests/variables/). Isso permite que você altere facilmente a URL base da API e outros parâmetros importantes sem modificar cada request individualmente.

**Estrutura do Diretório do Projeto:**

```
taskevalpro/
├── api/
│   ├── app.py
│   ├── doc/
│   │   └── postman-collection.json
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── routes.py
│   └── models/
│       ├── avaliacao.py
│       ├── tarefa.py
│       └── usuario.py
├── web/
│   ├── Dockerfile
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   │   ├── assets/
│   │   │   └── react.svg
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   └── public/
├── postgres-data/
├── scripts/
│   ├── ddl.taskevalpro.sql
│   └── dml.taskevalpro.sql
├── docker-compose.yml
└── README.md
```

* `api/`: Contém os arquivos da API Flask.
* `api/doc/`: Coleção Postman com exemplos de requests para a API.
* `web/`: Contém os arquivos do front-end em React.
* `web/public/`: Arquivos estáticos e públicos do front-end, como o favicon e o logo, que podem ser acessados diretamente.
* `web/src/`: Código-fonte JavaScript/JSX do front-end.
* `postgres-data/`: Volume Docker para o banco de dados PostgreSQL.
* `scripts/`: Scripts SQL para criação e preenchimento inicial do banco de dados.
* `docker-compose.yml`: Define e inicia os serviços com Docker Compose.
* `README.md`: Este arquivo.

**Contribuições:**

Se você tiver sugestões ou encontrar algum problema, sinta-se à vontade para contribuir com o projeto.

**Observações:**

* A documentação da API está disponível no arquivo `api/doc/postman-collection.json`.
* Informações da licença MIT disponíveis no arquivo `LICENSE`.
