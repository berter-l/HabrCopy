from uuid import uuid4

from app.services import session, ENDPOINT_URL, BUCKET_NAME, REGION_NAME


async def upload_file_to_s3(file: bytes, file_path: str):
    async with session.client(
        "s3", endpoint_url=ENDPOINT_URL, region_name=REGION_NAME
    ) as s3_client:

        await s3_client.put_object(Body=file, Bucket=BUCKET_NAME, Key=file_path)

    return file_path


async def build_file_path(post_id: int):
    file_path = f"posts/{post_id}/{uuid4()}"
    return file_path

