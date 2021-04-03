import pytest

from aeroplane.schemas import PageSchema
from aeroplane.models import Page


@pytest.fixture(scope="function")
def page():
    return Page.objects.create(
        title="Hello World",
        slug="hello-world",
        content="Hello world, welcome to the site!",
    )


@pytest.mark.django_db
def test_model_schema(page):
    schema = PageSchema.from_django(page)
    assert schema.dict() == {
        "id": page.id,
        "title": page.title,
        "slug": page.slug,
        "content": page.content,
        "revisions": page.revisions,
        "created_at": page.created_at,
        "updated_at": page.updated_at,
    }
    assert schema.schema() == {
        "title": "PageSchema",
        "description": "Page(id, title, slug, content, revisions, created_at, updated_at)",
        "type": "object",
        "properties": {
            "id": {"title": "Id", "description": "id", "type": "integer"},
            "title": {
                "title": "Title",
                "description": "The unique title of the page displayed to the public.",
                "maxLength": 255,
                "type": "string",
            },
            "slug": {
                "title": "Slug",
                "description": "The unique slug identifier used in URL addresses.",
                "maxLength": 255,
                "type": "string",
            },
            "content": {"title": "Content", "description": "content", "type": "string"},
            "revisions": {
                "title": "Revisions",
                "description": "revisions",
                "anyOf": [
                    {"type": "string", "format": "json-string"},
                    {"type": "object"},
                    {"type": "array", "items": {}},
                ],
            },
            "created_at": {
                "title": "Created At",
                "description": "created_at",
                "type": "string",
                "format": "date-time",
            },
            "updated_at": {
                "title": "Updated At",
                "description": "updated_at",
                "type": "string",
                "format": "date-time",
            },
        },
        "required": ["title", "slug", "content", "created_at", "updated_at"],
    }
