from pydantic import BaseModel, Field
from pydantic_category_model import CategoryModel


class ShoesModel(BaseModel):
    category: CategoryModel
    name: str
    slug: str
    image_path: str
    description: str
    price: str
    updated: bool
    available: bool
    created: bool