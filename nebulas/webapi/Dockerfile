# start by pulling the python image
FROM python:3.8.5-alpine

COPY . /webapi
# switch working directory
WORKDIR /webapi

RUN pip install --upgrade pip
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["webapp.py" ]
