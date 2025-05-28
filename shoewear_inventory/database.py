
from shoewear_inventory.models.base import init_db


def initialize_database():
    init_db()
    print("✅ Database initialized with tables.")