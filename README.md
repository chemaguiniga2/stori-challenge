# Stori Code Challenge
The current project sets to run a cron every 30 seconds that reads every file that is within an S3 bucket specified and process the information storaged in these files so that at the very end it builds an email with the summary and relevant information that is in these files.


## Prerequisites
- Docker

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

4. For receive the email to an specific address
```
Modify the env EMAIL_RECEIVERS in app/settings/base.py and re run the containers.
```

## Extra configurations
If the cron job schedule time wants to be set up to a diferent value then it needs to be changed at app/settings/base.py line 183:
```
CELERY_BEAT_SCHEDULE = {
    #
    # Run every 30 seconds
    #
    "process_sap_documents": {
        "task": "app.documents.tasks.process_csv_documents",
        "schedule": 30.0, # value to be modified
    }
}
```

If it is need to change the email address or add any other one we need to modify the following env:
IMPORTANT: Let's keep in mind that this env is a list.
```
EMAIL_RECEIVERS
```
