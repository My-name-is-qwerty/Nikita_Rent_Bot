from dataclasses import dataclass
from environs import Env

@dataclass
class DataBase:
    path: str

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    data_base: DataBase


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('TOKEN_API')), data_base=DataBase(path=env('PATH')))