FROM node:9-slim
WORKDIR /app_client
COPY package.json /app_client
RUN npm install
COPY . /app_client
CMD ["npm", "start"]