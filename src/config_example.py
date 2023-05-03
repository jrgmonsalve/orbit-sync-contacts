from typing import Dict
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
    hubspot: Dict = {
        "api_key": "demo"
        }
    clickup: Dict = {
        "token": "demo", 
        "list_id": "demo"
        }



settings = Settings()