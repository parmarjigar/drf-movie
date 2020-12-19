from django.db import models


class Cast(models.Model):
    actor_name = models.CharField(max_length=100, name="actor_name")

    def __str__(self):
        return self.actor_name


SERIES = "Series"
MOVIE = "Movie"
MEDIA_TYPE = (
    (SERIES, "Series"),
    (MOVIE, "Movie")
)


class Media(models.Model):
    name = models.CharField(max_length=50, name="name")
    genre = models.CharField(max_length=50, name="genre")
    cast = models.ManyToManyField("Cast", related_name="media")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE)
    media_file = models.ForeignKey("MediaFile", on_delete=models.CASCADE,
                                   null=True, blank=True, related_name="file")

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __str__(self):
        return f"{self.name.title()} - {self.media_type}"


class MediaFile(models.Model):
    name = models.CharField(max_length=100, name="name")
    desc = models.TextField(name="description")
    thumbnail = models.ImageField(name="thumbnail")
    video_url = models.FileField(upload_to="videos/", name="video_url")

    class Meta:
        verbose_name = "Media File"
        verbose_name_plural = "Media Files"

    def __str__(self):
        return self.name



