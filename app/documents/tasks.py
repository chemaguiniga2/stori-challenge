import logging
import boto3
import pandas as pd
import io

from celery import shared_task
from django.conf import settings

from app.documents.utils import process_transactions
from app.emails import send_stori_email

logger = logging.getLogger(__name__)


@shared_task
def process_csv_documents() -> None:
    s3 = boto3.resource("s3")
    bucket=s3.Bucket(settings.AWS_BUCKET_NAME)
    df = []
    for file in bucket.objects.all():
        logger.info(file)
        obj = s3.Object(settings.AWS_BUCKET_NAME,file.key)
        data=obj.get()['Body'].read()
        df = pd.read_csv(io.BytesIO(data), header=0, delimiter=",", low_memory=False)
        df = df.values.tolist()
    try:
        processed_file = process_transactions(df)
    except Exception as e:
        logger.info(f"Couldn't process the file: {e}")
        return

    send_stori_email(processed_file)

    logger.info("Email sent")
