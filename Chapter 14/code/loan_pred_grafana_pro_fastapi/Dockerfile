FROM python:3.7-slim-buster

ENV PYTHONPATH "${PYTHONPATH}:src/"

WORKDIR /app/

COPY . .

RUN chmod +x /app

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

# Expose the port that uvicorn will run the app on
ENV PORT=8000
EXPOSE 8000

RUN pip install --upgrade pip

RUN pip install --upgrade -r requirements.txt --no-cache-dir

CMD ["/start.sh"]
