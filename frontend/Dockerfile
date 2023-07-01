# frontend/Dockerfile

# Node.js 18イメージを指定
FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "serve"]
