FROM python:3.10

WORKDIR /application
COPY requirements.txt /application/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /application/requirements.txt

COPY . /application

CMD bash -c "while true; do sleep 1; done"