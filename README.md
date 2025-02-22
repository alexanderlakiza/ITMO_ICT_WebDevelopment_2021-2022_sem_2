# ITMO_ICT_WebDevelopment_2021-2022_sem_2
Репозиторий для реализации дистанционного обучения по дисциплине "СРЕДСТВА ВЕБ-ПРОГРАММИРОВАНИЯ".

[Учебный журнал]() по дисциплине. Тут доступна информация о сроках сдачи работ, о текущей успеваемости студентов и описаны все материалы необходимые для реализации курса.

Составляющие финальной оценки:
- 60 баллов - лабы.
- 10 баллов - тесты.
- 10 баллов - дисскусии на практиках (1+ доклад за семестр (оценка складывается из доклада 50% + активности на занятиях 50%)).
- 20 - экзамен.
При выполнении всех лаб по дисциплине в срок - экзамен-автомат.

### Лекция 1.1 - Концепции разработки веб сервисов.
Конспект с лекции [тут](https://docs.google.com/document/d/1H-SEVzy52Lcf3jHsvxn7aYW7yCR3ElzXorwrDo7onfQ/edit#heading=h.ry5wvaly4o7e).

# Лабораторная работа 1. Контейниризация и оркестрация.

### 1. Контейниризация средствами Docker.

Отчет по работе необходимо выполнить в mkdocs.

#### Изучить:
- [Изучаем Docker, часть 1: основы](https://habr.com/ru/company/ruvds/blog/438796/)
- [Изучаем Docker, часть 2: термины и концепции](https://habr.com/ru/company/ruvds/blog/439978/)
- [Изучаем Docker, часть 3: файлы Dockerfile](https://habr.com/ru/company/ruvds/blog/439980/) - **!!! Самый важный мануал на данном этапе**
- [Изучаем Docker, часть 5: команды](https://habr.com/ru/company/ruvds/blog/440660/)

#### Задание:
1. Написать Dockerfile для запуска бэкенд части проекта из курса "Web-программирование". 
2. Выполнить следующие действия:
- Изменить модель БД Django
- Зайти в контейнер и выполнить миграции (https://www.mousedc.ru/learning/565-komanda-docker-konteyner/)

### 2. Оркестрация средствами Docker-compose.

#### Изучить:
- [Использование Docker Compose](https://docs.microsoft.com/ru-ru/visualstudio/docker/tutorials/use-docker-compose)
- [Руководство по Docker Compose для начинающих](https://habr.com/ru/company/ruvds/blog/450312/)

#### Задание:
1. Реализовать работу в оркестре всех сервисов из 3 и 4 работы из курса "Web-программирование".
2. Выполнить команды необходимые для того, чтобы добавить нового пользователя в БД Postgres. С попощью пользователя должна быть возможность подключиться к БД из приложения для работы с БД (Valentina DB).

### 3. Работа с web-серверами.
Лекция на данную тему пройдет 10 марта. Задание будет дополнено.

# Лабораторная работа 2. Возможности Django REST Framework.

Срок выполнения работы: 28.04.2022

### 2.1 Фильтры

#### Изучить:
- [мануал по фильтрации](https://django.fun/docs/django-rest-framework/ru/3.12/api-guide/filtering/)
- [тоже может помочь в понимании](https://overcoder.net/q/24014/django-rest-framework-%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D0%BE-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%B0%D0%BC-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0)
- [пример использования проверки авторизованности юзера](https://www.delftstack.com/howto/django/django-check-logged-in-user/)
- [Документация django-filter](https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html)

#### Задание 2.1.1

  **Необходимо согласовать список фильтров с преподавателем перед выполнением задания. Задание выполняется на основе ЛР из предыдущего семестра или нового проекта (при желании)**

Реализвать в ручную следующие фильтры (в ручную значит, что Вам необходимо передать в url параметры, далее переопределть метод list или get_queryset, c целью взять параметры из url-адреса, выполнить с ними запрос и вернуть responce пользователю):
- принимает параметр из url-адреса и выводит отфильтрованные данные.  (GET, ListAPIView)
- принимает 2 параметра из url-адреса и выводит отфильтрованные данные. (GET, ListAPIView)
- принимает 2 параметра из url-адреса и выводит отфильтрованные данные, если пользователь авторизован и неотфильтрованные, если не авторизован. (GET, ListAPIView)

Список фильтров и код их исполнения необходимо описать в mkdocs на странице с названием "2.1.1 Ручные фильтры"

#### Задание 2.1.2

  **Необходимо согласовать список фильтров с преподавателем перед выполнением задания. Задание выполняется на основе ЛР из предыдущего семестра или нового проекта (при желании)**

Реализвать в ручную следующие фильтры (Необходимо использовать библиотеку django-filters:
- сортировка по дате, поиск, поиск по полям из связной таблицы
- сортировка в диапазоне цен, дат или каких-либо других числовых значений

Список фильтров и код их исполнения необходимо описать в mkdocs на странице с названием "2.1.2 Автоматические фильтры"

### 2.2 Пагинация

#### Изучить:

- [Исходный код DRF](https://github.com/encode/django-rest-framework/blob/master/rest_framework/pagination.py#L191) - необходимо изучить и разобраться, как работает код
- [Настройка и использование стандартной пагинации DRF](https://www.django-rest-framework.org/api-guide/pagination/)

#### Задание 2.2.1

Настроить пагинацию для любых списков в Вашем проекте.

#### Задание 2.2.2

Написать и применить метод пагинации, который, кроме обычного вывода вернет количество страниц пагинации и номер текущей страницы  ([Это поможет](https://www.django-rest-framework.org/api-guide/pagination/#example))

Код и пример вывода описать в mkdocs на странице с названием "2.2.2 Кастомная пагинация"

### 2.3. Загрузка файлов 

#### Изучить:

#### Задание 2.3.1

### 2.4. сигналы

#### Изучить:

#### Задание 2.4.1


### Сдача работы
Необходимо описать все этапы работы в документации mkdocs. Ссылку загрузить в markdown файл в своей папке в репозитории дисциплины.

Срок сдачи: **17.03.2022** (включительно). Вес работы в баллах – 15. После срока сдачи максимальный бал 10.
