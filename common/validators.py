from django.core.exceptions import ValidationError
from common.messages import Messages
from product_service.settings import FILE_UPLOAD_MAX_SIZE, IMAGE_TYPES

def validate_image_file(file): 
    if file.content_type not in IMAGE_TYPES:
        raise ValidationError(Messages.INVALID_IMAGE_FORMAT.value)
    if file.size > FILE_UPLOAD_MAX_SIZE:
        raise ValidationError(Messages.FILE_MAX_SIZE_MESSAGE.value)
    else:
        return True
