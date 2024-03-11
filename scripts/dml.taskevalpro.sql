-- Populando a tabela de usuários
INSERT INTO Usuarios (Nome_Usuario, Senha, Email, Papel) VALUES ('usuario1', 'senha1', 'usuario1@example.com', 'aluno');
INSERT INTO Usuarios (Nome_Usuario, Senha, Email, Papel) VALUES ('usuario2', 'senha2', 'usuario2@example.com', 'professor');
INSERT INTO Usuarios (Nome_Usuario, Senha, Email, Papel) VALUES ('usuario3', 'senha3', 'usuario3@example.com', 'administrador');

-- Populando a tabela de tarefas
INSERT INTO Tarefas (Titulo, Descricao, Prazo, Prioridade, Status, ID_Criador, ID_Responsavel) VALUES ('Tarefa 1', 'Descrição da Tarefa 1', '2024-03-20', 1, 'Pendente', 1, 1);
INSERT INTO Tarefas (Titulo, Descricao, Prazo, Prioridade, Status, ID_Criador, ID_Responsavel) VALUES ('Tarefa 2', 'Descrição da Tarefa 2', '2024-03-25', 2, 'Pendente', 2, 2);

-- Populando a tabela de avaliações
INSERT INTO Avaliacoes (Criterios_Avaliacao, Pontuacao, Comentarios, ID_Tarefa_Avaliada, ID_Avaliador) VALUES ('Critérios 1', 5, 'Bom trabalho!', 1, 2);
INSERT INTO Avaliacoes (Criterios_Avaliacao, Pontuacao, Comentarios, ID_Tarefa_Avaliada, ID_Avaliador) VALUES ('Critérios 2', 4, 'Pode melhorar.', 2, 3);

-- Populando a tabela de projetos
INSERT INTO Projetos (Titulo, Descricao, Data_Inicio, Data_Termino) VALUES ('Projeto 1', 'Descrição do Projeto 1', '2024-03-01', '2024-04-01');
INSERT INTO Projetos (Titulo, Descricao, Data_Inicio, Data_Termino) VALUES ('Projeto 2', 'Descrição do Projeto 2', '2024-03-10', '2024-04-10');
