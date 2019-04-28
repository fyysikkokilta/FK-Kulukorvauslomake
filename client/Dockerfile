FROM node:8-alpine

WORKDIR /opt/kuluclient
COPY . .

RUN apk add npm

CMD npm i && npm run serve
