from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = 'dfbhr-v2-assets'
    default_acl = 'private'
    file_overwrite = True
    custom_domain = False
