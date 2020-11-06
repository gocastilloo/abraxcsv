# Abraxas

Test: API with spatial database.
## Getting Started

These instructions will cover usage information and for the docker container 

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Instructions to run 
Once you've **cloned the git repo**, everything will happen in your terminal.
Make sure docker-compose file is here, you can list with command ```ls```
**Open your command line in the directory of this file**
Then:

    docker-compose build
Once the volume is build:

    docker-compose up
If you get an error with ```web_1``` service, don't worry, we will work in another shell with Django
**Open** another window shell  and we will kill Django from there, so we can debug better.
In the **second shell** window type:

    docker rm -f abraxas_web_1
Then, we will apply the migrations to the file:

    docker-compose run --rm --service-ports web python manage.py makemigrations
We will apply those migrations to the database:

    docker-compose run --rm --service-ports web python manage.py migrate
And now, we will run Django

    docker-compose run --rm --service-ports web


#### Useful Links
The base URL will be:
`localhost:8000/api/v1`
##### Then you can add the following path:
If you want to list the datasets:
* `/datasets` 

If you want to list the rows in the dataset:
* `/rows`

If you want to POST and GET in just one path
* `/all_data`

All of this links you can access in the base URL, hope you enjoy it.
## Built With

* Django v3.1.3
* Django REST Framework v3.12.1
* Postgres
* Postgis


## Authors

* **Hugo Castillo** - [Abraxcsv](https://github.com/abraxcsv)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

