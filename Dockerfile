FROM python:3.9

COPY ./requirements.txt /home/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/requirements.txt

WORKDIR /home/app

COPY ./app /home/app

# cache binaries
RUN prisma generate
