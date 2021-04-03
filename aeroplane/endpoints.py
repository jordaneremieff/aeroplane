from typing import List
from datetime import datetime

from fastapi import APIRouter

from aeroplane.models import Page
from aeroplane.schemas import PageSchema, PageRevisionSchema

router = APIRouter()


@router.post("/pages", response_model=PageSchema)
def create_page(page: PageRevisionSchema):
    page = Page.objects.create(**page.dict())

    return PageSchema.from_django(page)


@router.get("/pages", response_model=List[PageSchema])
def list_pages():
    return PageSchema.from_django(Page.objects.all(), many=True)


@router.put("/pages/{id}", response_model=PageSchema)
def update_page(id: int, page_data: PageRevisionSchema):
    page = Page.objects.get(id=id)

    # Save the content fields for the current page to the revision history
    revision_schema = PageRevisionSchema.from_django(page)
    timestamp = str(datetime.now().timestamp())
    page.revisions[timestamp] = revision_schema.dict()

    # Update the page object with the new data
    for k, v in page_data.dict().items():
        setattr(page, k, v)
    page.save()

    return PageSchema.from_django(page).dict()
