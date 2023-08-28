### Hexlet tests and linter status:
[![Actions Status](https://github.com/u-shev/python-project-83/workflows/hexlet-check/badge.svg)](https://github.com/u-shev/python-project-83/actions)
[![Python CI](https://github.com/u-shev/python-project-83/actions/workflows/pyci.yml/badge.svg)](https://github.com/u-shev/python-project-83/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/1775077c13e52a6fdd9d/maintainability)](https://codeclimate.com/github/u-shev/python-project-83/maintainability)

### [Page Analyzer](https://app-0xws.onrender.com) – это сайт, который анализирует указанные страницы на SEO-пригодность.

### Установка
Для корректной работы нужны версии python 3.8.1 и poetry 1.4.2, также нужно установить PostrgreSQL.
#### Клонирование репозитария
```
git clone git@github.com:u-shev/python-project-83.git
cd python-project-83
```  
#### Создание базы данных
```
whoami
{username}
sudo -u postgres createuser --createdb {username} 
createdb {databasename}
psql {databasename} < database.sql
```  
#### Секретные ключи
Создать в директории page_analyzer .env файл для переменных окружения со следующей информацией:  
DATABASE_URL=postgresql://{username}:{password}@{host}:{port}/{databasename}  
SECRET_KEY='{your secret key}'
#### Установка зависимостей
```make install```  
#### Разработка и локальное использование
```make dev```  
#### Команды для деплоя
```
make build    
make start
```  
