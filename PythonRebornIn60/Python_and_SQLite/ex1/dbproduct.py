from sqlmodel import Session, create_engine, select
from modelsProduct import Product

sql_url = "sqlite:///productDB.db"
engine = create_engine(sql_url, echo=True)


def add_product(name: str, description: str | None, price: float, quantity: int):
    with Session(engine) as session:
        product = Product(
            product_name=name, description=description, price=price, quantity=quantity
        )
        session.add(product)
        session.commit()
        session.refresh(product)
        print("=" * 100)
        print("Product added successfully:", product)
        print("=" * 100)


def list_all_products():
    with Session(engine) as session:
        query = select(Product)
        products = session.exec(query).all()

        print("=" * 100)
        for product in products:
            print(product)
        print("=" * 100)


def find_product_by_name(name: str):
    with Session(engine) as session:
        query = select(Product).where(Product.product_name == name)
        products = session.exec(query).all()
        if not products:
            print("=" * 100)
            print("Product Not Found")
            print("=" * 100)
        else:
            print("=" * 100)
            for product in products:
                print(product)
            print("=" * 100)


def update_product_quantity(name: str, new_quantity: int):
    with Session(engine) as session:
        query = select(Product).where(Product.product_name == name)
        product = session.exec(query).first()
        if not product:
            print("=" * 100)
            print("Product Not Found")
            print("=" * 100)
        else:
            product.quantity = new_quantity
            session.add(product)
            session.commit()
            session.refresh(product)
            print("=" * 100)
            print("Product updated successfully:", product)
            print("=" * 100)


def delete_product(name: str):
    with Session(engine) as session:
        query = select(Product).where(Product.product_name == name)
        product = session.exec(query).first()
        if not product:
            print("=" * 100)
            print("Product Not Found")
            print("=" * 100)
        else:
            session.delete(product)
            session.commit()
            print("=" * 100)
            print("Product deleted successfully")
            print("=" * 100)
