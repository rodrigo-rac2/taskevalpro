FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Adiciona o diretório pai ao PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY . .

CMD [ "python", "app.py" ]
