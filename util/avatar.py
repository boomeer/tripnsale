from django.core.files import File

import os
import random
import string


class AvatarBigSizeErr(Exception):
    pass


def StoreImage(image, field, fileName="", sizeLimit=4*2**20):
    imageFileExt = os.path.splitext(image.name)[1]
    if image.size > sizeLimit:
        raise AvatarBigSizeErr
    filePath = ''.join(random.choice(string.ascii_lowercase \
        + string.digits) for i in range(20)) + imageFileExt
    field.save(filePath, image)
    return filePath

