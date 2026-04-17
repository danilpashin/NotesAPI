import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path, override=True)

def get_db_url():
    user = os.getenv("APP_DB_USER")
    password = os.getenv("APP_DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = 5432
    name = os.getenv("DB_NAME")
    return f"postgresql://{user}:{password}@{host}:{port}/{name}?sslmode=disable"

DATABASE_URL = get_db_url()