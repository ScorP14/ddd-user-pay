from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Base(BaseSettings):
    model_config = SettingsConfigDict()


class PostgreSQL(Base):
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: str


class Constants(Base):
    # postgresql: PostgreSQL()
    sale_for_password: str = Field(default="oiaSASD921nSADuiasbd8921hSADon")


@lru_cache(1)
def get_constant():
    return Constants()
