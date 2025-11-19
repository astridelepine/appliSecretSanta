FROM python:3.13

COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD uvicorn api:app --host 0.0.0.0 --port 8080




