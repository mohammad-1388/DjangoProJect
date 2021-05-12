from django.db import models


class Setting(models.Model):
    """
        The Model Represent A site settings
    """
    selected = models.BooleanField('فعال')
    name_template = models.CharField('نام قالب', max_length=255)
    title = models.CharField('نام سایت', max_length=255)
    description = models.TextField('توضیحات')

    def __str__(self):
        return str(self.name_template) + " | " + str(self.title)

    def __unicode__(self):
        return self.__str__()
