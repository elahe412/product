from enum import Enum

class Messages(Enum):
    INVALID_IMAGE_FORMAT = "Images must be in jpeg,png,jpg,svg format"
    FILE_MAX_SIZE_MESSAGE = "The maximum file size that can be uploaded is 5MB"