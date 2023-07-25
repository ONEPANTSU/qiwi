# Отбор на стажирвоку #FRESHQIWI 2023 Backend
___
🥝 Консольная утилита, которая выводит курсы валют ЦБ РФ 
за определенную дату. Для получения курсов используется 
официальный API ЦБ РФ https://www.cbr.ru/development/sxml/.

## Interface
```commandline
python currency_rates.py --code=USD --date=2022-10-08
```

## Params
- `code` - код валюты в формате ISO 4217
- `date` - дата в формате YYYY-MM-DD

## Output
```commandline
USD (Доллар США): 61,2475
```

## Installation
1. Клонирование репозитория: 
```commandline
git clone https://github.com/ONEPANTSU/Qiwi.git
```
2. Установка зависимостей:
```commandline
pip install -r requirements.txt
```
3. Использование интерфейса:
```commandline
python currency_rates.py --code=USD --date=2022-10-08
```