FROM node:18 AS build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm cache clean --force && npm install
COPY . ./
RUN npm run build

EXPOSE 4173
CMD npm run preview -- --port=4173 --host

