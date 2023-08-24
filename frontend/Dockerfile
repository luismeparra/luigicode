# app(front-end)
FROM python:3.11-slim

#WORKDIR C:/Users/luis.mendez/luigicode
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn which
RUN pip3 install --no-cache-dir -r requirements.txt
RUN which uvicorn
#RUN apt-get update && apt-get install -y vim

EXPOSE 3000
CMD ["poetry", "run","uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "3000" , "--reload"]