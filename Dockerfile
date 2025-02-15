FROM python:3.9

WORKDIR /app

COPY questao3 /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]