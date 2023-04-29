FROM python:3.7-slim-buster

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

ENV PYTHONPATH "${PYTHONPATH}:app/src/"

COPY . /app

RUN chmod +x /app

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

CMD ["./start.sh"]
