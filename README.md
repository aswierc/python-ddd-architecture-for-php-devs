# python-ddd-architecture-for-php-devs

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Intro

The project was made for PHP (Symfony) developers like me, who were curious if it's possible to make something similar using Python and its libraries.

I feel like there are a lot of programmers who wanted to try Python. But they were back to PHP after encountering Django.

## TODO 

- Make an aggregate, figure out some domain context and implement
- Design Level Event Storming diagrams  
- Command-Handler, though queues as well - like Messenger in Symfony 
- Implementation of Domain Events https://udidahan.com/2009/06/14/domain-events-salvation/
- Implementation of a read model (CQRS)
- Show how to write tests (pytest) and static analysis tools (mypy)
- ...
- Invite to cooperation :) 

## Stack

- Python 3.9
- FastAPI
- PostgreSQL

## Setup

1. Install dependencies:

```bash
$ poetry install
```
## Running app locally

1. Run `docker-compose up -d`
2. Go to `app.py` and run the app

## Tests


```bash
$ poetry run pytest
```

or

```bash
$ make tests
```
