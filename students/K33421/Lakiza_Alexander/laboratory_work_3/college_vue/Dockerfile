FROM node:12

ENV front_dir=/home/alexanderkakiza/pyfiles/ITMO_ICT_WebDevelopment_2021-2022_sem_2/students/K33422/Lakiza_Alexander/laboratory_work_3/college_vue

WORKDIR $front_dir

COPY package*.json ./

RUN npm install

#COPY . .

COPY . .

RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]
