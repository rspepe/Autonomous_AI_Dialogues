# frontend/Dockerfile

# Node.js 19イメージを指定
FROM node:19

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "serve"]
