# Сайт магазина авторского вина "Новое русское вино".

## Подготовка к запуску скрипта
Для начала, необходимо проверить установлен ли pip.
В командной строке вбейте команду
```
pip --version
```
Должна вывестись версия pip, если нет, то его необходимо установить с помощью curl или wget
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
или
```
wget https://bootstrap.pypa.io/get-pip.py
```
После загрузки скрипта запустите его с помощью пайтон
```
python get-pip.py
```
Если pip уже установлен и вы хотите его обновить до последней версии, выполните следующую команду:
```
python -m pip install --upgrade pip
```
## Подготовка к запуску скрипта - установка необходимых модулей
Необходимо перейти в директорию, где находится скрипт. В этой дериктории находится файл ```requirements.txt```
Перейти в директорию можно следующей командой:
```
cd C:\ваш\путь
```
Вместо C:\ваш\путь укажите фактический путь.
Далее введите следующую команду для установки необходимых модулей
```
pip install -r requirements.txt
```

## Запуск скрипта
- Скачайте код
Вы можете скачать репозиторий по ссылке на GitHub: [ссылка на скрипт](https://github.com/Andrey9045/lesson14.1)

## Подготовка и запуск скрипта
Для работы со скриптом необходимо создать .xlsx фаил(уже созданый фаил есть в репозитории), который будет выглядеть следующим образом:
![Фото](https://raw.githubusercontent.com/Andrey9045/photo/refs/heads/main/1.png)
Запустить скрипт можно двумя способами.
Первый способ, запуск скрипта прописав путь к .xlsx файлу в качестве аргумента
![Фото](https://raw.githubusercontent.com/Andrey9045/photo/refs/heads/main/2.png)
Второй способ, хранение пути к .xlsx файлу в переменной окружения
1) Необходимо создать переменную окружения с путем файла, в командной строке введите следующую команду
```
set WINE_FILEPATH=С:\wine3.xlsx
```
Вместо ```C:\wine3.xlsx``` введите фактический путь до вашего .xlsx файла.
2) Теперь иожете запускать скрипт при помощи переменной окружения
```
python main.py %WINE_FILEPATH%
```
## Что сделает скрипт
Скрипт автоматически посчитает "Сколько лет ваш бизнес с нами". Изменив слово "лет" на подходящее под числительное.
Скрипт прочтет ваш .xlsx файл, сформирует на его основе список словарей. Далее скрипт передаст ваш список словарей в шаблон, на основе котого сформируется index.html.
## Открываем сайт 
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
- Или же открыть index.html в браузере

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
