FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r backend/requirements.txt
RUN pip install -r frontend/requirements.txt

EXPOSE 8000
EXPOSE 8501