from pydantic import BaseModel


class S3Config(BaseModel):
    endpoint_url: str = "https://s3.cloud.ru"
    region_name: str = "ru-central-1"
    aws_secret_access_key: str = ""
    key_id: str = ""
    tenant_id: str = ""
    bucket_name: str = ""
