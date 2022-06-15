FROM python:3.8.12

ENV app_dir=/home/alexanderkakiza/pyfiles/ITMO_ICT_WebDevelopment_2021-2022_sem_2/students/K33422/Lakiza_Alexander/laboratory_work_3

WORKDIR $app_dir

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
