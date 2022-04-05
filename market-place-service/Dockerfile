# pull the python image
FROM python:3.9.5-slim-buster

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# copy every content from the local file to the image
COPY . /app

ENTRYPOINT ["python"]

CMD ["run.py"]
