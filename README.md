# Stori Code Challenge

## How to run in local environment

1. Build docker images
```
docker-compose build
```

2. Run db and backend containers
```
docker-compose up -d
```

3. Raise containers
```
docker-compose up
```

3. Apply migrations once containers are up
```
docker-compose run --rm app python manage.py migrate
```

4. Poblate DB
```
docker-compose run app python manage.py loaddata data_dump.json
```

