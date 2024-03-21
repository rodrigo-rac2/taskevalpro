FROM node:20.3.0

# Define o diretório de trabalho
WORKDIR /web

COPY . /web

# Limpa node_modules e package-lock.json e reinstala dependências
RUN rm -rf node_modules package-lock.json && npm install

# Constrói a aplicação
RUN npm run build

# Instala serve para servir a aplicação construída
RUN npm install -g serve

# Expõe a porta 3000
EXPOSE 3000

# Serve a aplicação
CMD ["serve", "-s", "dist", "-l", "3000"]
