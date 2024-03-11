-- Tabela de Usuários
CREATE TABLE Usuarios (
    ID SERIAL PRIMARY KEY,
    Nome_Usuario VARCHAR(100) NOT NULL,
    Senha VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    Papel VARCHAR(20) NOT NULL
);

-- Tabela de Tarefas
CREATE TABLE Tarefas (
    ID SERIAL PRIMARY KEY,
    Titulo VARCHAR(100) NOT NULL,
    Descricao TEXT,
    Prazo TIMESTAMP,
    Prioridade INT,
    Status VARCHAR(20) DEFAULT 'Pendente',
    ID_Criador INT,
    ID_Responsavel INT,
    FOREIGN KEY (ID_Criador) REFERENCES Usuarios(ID),
    FOREIGN KEY (ID_Responsavel) REFERENCES Usuarios(ID)
);

-- Tabela de Avaliações
CREATE TABLE Avaliacoes (
    ID SERIAL PRIMARY KEY,
    Criterios_Avaliacao TEXT,
    Pontuacao INT,
    Comentarios TEXT,
    ID_Tarefa_Avaliada INT,
    ID_Avaliador INT,
    Data_Avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Tarefa_Avaliada) REFERENCES Tarefas(ID),
    FOREIGN KEY (ID_Avaliador) REFERENCES Usuarios(ID)
);

-- Tabela de Projetos
CREATE TABLE Projetos (
    ID SERIAL PRIMARY KEY,
    Titulo VARCHAR(100) NOT NULL,
    Descricao TEXT,
    Data_Inicio TIMESTAMP,
    Data_Termino TIMESTAMP
);
