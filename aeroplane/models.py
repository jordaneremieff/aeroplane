from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Page(models.Model):
    title = models.CharField(
        verbose_name=_("title"),
        max_length=255,
        help_text=_("The unique title of the page displayed to the public."),
    )
    slug = models.SlugField(
        verbose_name=_("slug"),
        allow_unicode=True,
        max_length=255,
        help_text=_("The unique slug identifier used in URL addresses."),
    )
    content = models.TextField()
    revisions = models.JSONField(default=dict, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pages"
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        constraints = [
            models.UniqueConstraint(fields=["slug"], name="unique_slug"),
            models.UniqueConstraint(fields=["title"], name="unique_title"),
        ]
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["-updated_at"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
