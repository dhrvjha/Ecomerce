FROM python:3.9-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /tmp/requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc  libc-dev linux-headers
RUN apk add --update --no-cache libpq-dev
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN apk del .tmp
RUN echo 'all requirements installed'

# RUN mkdir /admin
COPY ./.pg_service.conf /etc/postgresql/
COPY ./admin /admin
COPY ./scripts /scripts
RUN chmod +x /scripts/*

WORKDIR /admin

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

USER user
COPY ./.pg_service.conf ~/
CMD [ "entrypoint.sh" ]
