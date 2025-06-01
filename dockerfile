FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# script que espera a que la DB este lista
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# la DB esta lista antes de correr migraciones y levantar el servidor
CMD ["/wait-for-it.sh", "db:5432", "--", "sh", "-c", "flask db upgrade && flask run --host=0.0.0.0"]
