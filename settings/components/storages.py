from settings.components.base import env

AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME', default='')

if AWS_STORAGE_BUCKET_NAME:
    AWS_S3_REGION_NAME = env.str('AWS_S3_REGION_NAME', default='us-east-1')
    AWS_S3_ENDPOINT_URL = env.str('AWS_S3_ENDPOINT_URL', default='') or None
    AWS_S3_CUSTOM_DOMAIN = env.str('AWS_S3_CUSTOM_DOMAIN', default='') or None
    AWS_DEFAULT_ACL = None
    AWS_S3_FILE_OVERWRITE = False
    AWS_QUERYSTRING_AUTH = env.bool(
        'AWS_QUERYSTRING_AUTH',
        default=not bool(AWS_S3_CUSTOM_DOMAIN),
    )

    _s3_options = {
        'bucket_name': AWS_STORAGE_BUCKET_NAME,
        'region_name': AWS_S3_REGION_NAME,
        'default_acl': AWS_DEFAULT_ACL,
        'file_overwrite': AWS_S3_FILE_OVERWRITE,
        'querystring_auth': AWS_QUERYSTRING_AUTH,
    }
    if AWS_S3_ENDPOINT_URL:
        _s3_options['endpoint_url'] = AWS_S3_ENDPOINT_URL
    if AWS_S3_CUSTOM_DOMAIN:
        _s3_options['custom_domain'] = AWS_S3_CUSTOM_DOMAIN

    STORAGES = {
        'default': {
            'BACKEND': 'storages.backends.s3.S3Storage',
            'OPTIONS': {**_s3_options, 'location': 'media'},
        },
        'staticfiles': {
            'BACKEND': 'storages.backends.s3.S3Storage',
            'OPTIONS': {**_s3_options, 'location': 'static'},
        },
    }
