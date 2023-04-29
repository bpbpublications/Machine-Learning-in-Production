# STEP 1: Install base image. Optimized for Python
FROM python:3.7-slim-buster

# STEP 2: Upgrading pip
RUN pip install --upgrade pip

# STEP 3: Copiying all the files to app directory
COPY . /app

# STEP 4: Set working directory to previously added app directory
WORKDIR /app

# STEP 5: Giving permissions to python file
RUN chmod +x train.py

# STEP 6: Install required pyhton dependencies from requirements file
RUN pip install -r requirements.txt

# STEP 7: Run train.py file
ENTRYPOINT ["python"]

CMD ["train.py"]