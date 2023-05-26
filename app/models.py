from django.db import models


class Keyword(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="not complete")

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    status = models.CharField(max_length=20, default="not complete")

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        return self.name


class Info(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    link = models.URLField()
    reviews = models.IntegerField()
    screen_diagonal = models.CharField(max_length=10, null=True, blank=True)
    sim_card_count = models.CharField(max_length=10, null=True, blank=True)
    built_in_memory = models.CharField(max_length=10, null=True, blank=True)
    front_camera = models.CharField(max_length=20, null=True, blank=True)
    main_camera = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Infos"

    def __str__(self):
        return self.product_name
