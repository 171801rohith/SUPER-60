from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_name: str = Field(index=True)
    description: str | None
    price: float
    quantity: int = Field(default=0)