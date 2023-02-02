# python-ddd-architecture-for-php-devs

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Intro

The project was made for PHP (Symfony) developers like me, who were curious if it's possible to make something similar using Python and its libraries.

I feel like there are a lot of programmers who wanted to try Python. But they were back to PHP after encountering Django.

## TODO 

- Design Level Event Storming diagrams  
- Make an aggregate, ~~figure out some domain context and implement~~
- Command-Handler, though queues as well - like Messenger in Symfony 
- Implementation of Domain Events https://udidahan.com/2009/06/14/domain-events-salvation/
- Implementation of a read model (CQRS)
- ~~Show how to write tests (pytest)~~
- ~~Static analysis tools (mypy)~~
- ...
- Invite to cooperation :) 

## Domain description and requirements 

The system allows clients to subscribe to the gym (60EUR per month).

Requirements:  
- registration new clients
- active clients will be billed monthly automatically 
  - billing is processed every first day of the month 
- the system can apply bonuses
  - percents or amounts
  - if the client has a birthday in the current month, the customer is entitled to a percentage discount (50%)
  - for new clients will have amount discount (20EUR)
  - if the client is employed in the gym, is entitled to a free subscription (100%)

Examples:  
- John has a birthday in February, he should pay 50% less 
- Charlotte is new at the gym, her first payment will be 20EUR less 
- Emma works at the gym, and have a subscription, have a free subscription 
- Emma as a gym employee also has to:
  - generate monthly reports
  - filter users by name, surname, and email, and check if the subscription is active

## Stack

- Python 3.10
- FastAPI
- PostgreSQL

## Setup

1. Install dependencies:

```bash
$ poetry install
```

If you don't have poetry yet: https://python-poetry.org/docs/

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
