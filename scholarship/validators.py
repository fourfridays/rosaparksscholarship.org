import magic

from django.core.exceptions import ValidationError


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError("File too large. Size should not exceed 2 MiB")


def validate_document_file_extension(content):
    try:
        # read only a small chunk or a large file could nuke the server
        file_content_type = magic.from_buffer(content.read(1024), mime=True).split('/')[0]
    finally:
        pass

    content_type = content.content_type.split('/')[0]

    if content_type in [
        "application",
    ] and file_content_type in ["application"]:
        pass
    else:
        raise ValidationError("File type is not supported")
    return content
