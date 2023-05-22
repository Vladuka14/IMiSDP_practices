import re
import requests
import json
import string

id = 41450002//ldd
# Запрос страницы из базы данных api и форматирование в объект словаря python
vacancy = requests.get("https://api.hh.ru/vacancies/" + str(id)).json()
print(vacancy)
