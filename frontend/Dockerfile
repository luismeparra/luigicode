# app(front-end)
FROM python:3.11-slim

WORKDIR C:/Users/luis.mendez/luigicode
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y vim

EXPOSE 8000
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]