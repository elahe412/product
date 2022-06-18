from django.core.exceptions import ValidationError
from common.messages import Messages
from product_service.settings import FILE_UPLOAD_MAX_SIZE

def validate_file_size(file):
    filesize= file.size
    
    if filesize > FILE_UPLOAD_MAX_SIZE:
        raise ValidationError(Messages.FILE_MAX_SIZE_MESSAGE.value)
    else:
        return file
