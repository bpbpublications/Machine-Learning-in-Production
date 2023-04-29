# FROM python:3.7-slim-buster

ARG REPO=692601447418.dkr.ecr.us-west-2.amazonaws.com

FROM ${REPO}/python:3.7

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

ENV PYTHONPATH "${PYTHONPATH}:app/src/"

COPY . /app

RUN chmod +x /app

# expose the port that uvicorn will run the app on
ENV PORT=8000
EXPOSE 8000

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

CMD ["./start.sh"]
