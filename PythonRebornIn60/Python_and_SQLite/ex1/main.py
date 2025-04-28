from sqlmodel import SQLModel
from dbproduct import (
    engine,
    add_product,
    list_all_products,
    find_product_by_name,
    delete_product,
    update_product_quantity,
)


def create_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()
    add_product("Rolex", "It's a watch", 1000, 3)
    add_product("Samsung", "It's a TV", 100, 4)
    add_product("Nothing", "It's a SmartPhone", 200, 2)

    list_all_products()

    find_product_by_name("Rolex")
    find_product_by_name("Apple") # Not Found

    update_product_quantity("Rolex", 8)

    delete_product("Rolex")
