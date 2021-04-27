# устанавливаем ноде
FROM node

# устанавливаем рабочую папку
WORKDIR /app

# устанавливаем переменную  PATH 
ENV PATH /app/node_modules/.bin:$PATH

# копируем в папку зависимости а затем устанавливаем ихs
COPY package.json /app/package.json
RUN npm install

# копируем проект в рабочуюю папку
COPY . /app

# запускаем проект
# CMD npm run serve