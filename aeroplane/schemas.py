from typing import Optional

from djantic import ModelSchema

from aeroplane.models import Page


class PageCreateUpdateSchema(ModelSchema):

    slug: Optional[str] = None

    class Config:
        model = Page
        include = ["title", "content"]


class PageSchema(ModelSchema):
    class Config:
        model = Page
