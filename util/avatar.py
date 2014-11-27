from django.core.files import File

import os
import random
import string


def StoreImage(image, field, fileName, sizeLimit=4*2**20):
    imageFileExt = os.path.splitext(image.name)[1]
    if image.size > sizeLimit:
        raise AvatarBigSize
    tempFileName = ''.join(random.choice(string.ascii_lowercase \
        + string.digits) for i in range(20))
    field.save(tempFileName + imageFileExt, image)

