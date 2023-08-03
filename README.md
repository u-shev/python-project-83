### Hexlet tests and linter status:
[![Actions Status](https://github.com/u-shev/python-project-83/workflows/hexlet-check/badge.svg)](https://github.com/u-shev/python-project-83/actions)
[![Python CI](https://github.com/u-shev/python-project-83/actions/workflows/pyci.yml/badge.svg)](https://github.com/u-shev/python-project-83/actions/workflows/pyci.yml)
<a href="https://codeclimate.com/github/u-shev/python-project-83/maintainability"><img src="https://api.codeclimate.com/v1/badges/1775077c13e52a6fdd9d/maintainability" /></a>

<h3> <a href="https://app-0xws.onrender.com/">Page Analyzer</a> – это сайт, который анализирует указанные страницы на SEO-пригодность.</h3>

<h3>Установка</h3>
<p>Для корректной работы нужны версии python 3.8.1 и poetry 1.4.2, также нужно установить PostrgreSQL.</p>
<h4>Клонирование репозитария</h4>
<p>git clone git@github.com:u-shev/python-project-83.git
cd python-project-83</p>
<h4>Создание базы данных</h4>
<p>whoami<br>
{username}<br>
sudo -u postgres createuser --createdb {username}<br>
createdb {databasename}<br>
psql {databasename} < database.sql</p>
<h4>Секретные ключи</h4>
<p>Создать в директории page_analyzer .env файл для переменных окружения со следующей информацией:<br>
DATABASE_URL=postgresql://{username}:{password}@{host}:{port}/{databasename}<br>
SECRET_KEY='{your secret key}'</p>
<h4>Установка зависимостей</h4>
<p>make install</p>
<h4>Разработка и локальное использование</h4>
<p>make dev</p>
<h4>Команды для деплоя</h4>
<p>make build<br>
make start</p>
