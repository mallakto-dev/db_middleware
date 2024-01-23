# db_middleware

## 1. Installing packages

`sudo apt install python3`
if needed


### install PIP

`sudo apt install python3-pip`

### install dependencies

`pip install -r requirements.txt`


## 2. Preparing database

### install postgreSQL

```
\# Create the file repository configuration:
sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

\# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

\# Update the package lists:
sudo apt-get update

\# Install the latest version of PostgreSQL.
\# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```


### create postgres user

It should match with your linux username

`sudo -u postgres createuser --createdb <username>`


### create database

`createdb <database_name>`

### create table

`psql -d <database_name> -f database.sql`

### set password for your user

`psql <database_name>`

`ALTER ROLE <username> WITH PASSWORD '<password>'`

`\q`

## 3. Preparing gunicorn server


### install gunicorn

`sudo apt install gunicorn`


### create .env file:

`touch .env`

### add variables:

`nano .env`

```
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
```


## Run Server

### To run server:

`gunicorn -w 5 -b 127.0.0.1:8000 app:app`
