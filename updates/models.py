from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json

# Create your models here.


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        list_value = list(self.values("id", "user", "content", "image"))
        # # qs = self
        # # data_list = []
        # # for obj in qs:
        # #     stuct = json.loads(obj.serialize())
        # #     data_list.append(stuct)
        # # return json.dumps(data_list)
        return json.dumps(list_value)

    # # the data returned from this is not near to the API form
    # # so it need to be done the ABOVE way
    # # def serialize(self):
    # #     qs = self
    # #     return return serialize("json", [self], fields=("user", "content", "image"))


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):

        try:
            image = self.image.url
        except:
            image = ""

        data = {
            "id": self.id,
            "user": self.user.username,
            "content": self.content,
            "image": image
        }
        data = json.dumps(data)
        return data

        # # json_data = serialize("json", [self], fields=("user", "content", "image"))
        # # stuct = json.loads(json_data)
        # # data = json.dumps(stuct[0]['fields'])
        # # return data

        # # the data returned from this is not near to the API form
        # # so it need to be done the ABOVE way
        # # return serialize(
        # #     "json", [self], fields=("user", "content", "image"))
