import os
from django.utils import timezone
from uuid import uuid4
try:
    from io import BytesIO as StringIO  # python 3
except ImportError:
    from StringIO import StringIO  # python 2


def random_name_upload_to(model_instance, filename):
    dirpath = set_directory(model_instance, filename)
    random_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return dirpath + '/' + random_name + extension


def own_name_upload_to(model_instance, filename):
    dirpath = set_directory(model_instance, filename)
    return dirpath + '/' + filename


def set_directory(model_instance, filename):
    app_label = model_instance.__class__._meta.app_label
    model_cls_name = model_instance.__class_.__name__.lower()
    dirpath_format = app_label + '/' + model_cls_name + '/%Y/%m/%d'
    dirpath = timezone.now().strftime(dirpath_format)
    return dirpath
