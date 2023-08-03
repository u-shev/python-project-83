#!/usr/bin/env bash

from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


make install && psql -a -d $DATABASE_URL -f database.sql