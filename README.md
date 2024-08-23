# Installation

1. Setup .env file, example:
```angular2html
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=

POSTGRES_DB_TEST=
POSTGRES_TEST_USER=
POSTGRES_TEST_PASSWORD=
DB_TEST_HOST=
DB_TEST_PORT=
```

2. ```docker compose up -d --build```

By this url you can reach the docs: ```http://0.0.0.0:5000/api/docs/```

To run tests: ```docker-compose exec app pytest tests```