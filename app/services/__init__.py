from .posts import get_all_posts_title
import aioboto3
import asyncio
from app.config.conf import settings

AWS_SECRET_ACCESS_KEY = settings.s3_conf.aws_secret_access_key

TENANT_ID = settings.s3_conf.tenant_id

REGION_NAME = settings.s3_conf.region_name

ENDPOINT_URL = settings.s3_conf.endpoint_url

BUCKET_NAME = settings.s3_conf.bucket_name

AWS_ACCESS_KEY_ID = settings.s3_conf.key_id

session = aioboto3.Session(
    aws_access_key_id=f"{TENANT_ID}:{AWS_ACCESS_KEY_ID}",
    aws_secret_access_key=f"{AWS_SECRET_ACCESS_KEY}",
)
