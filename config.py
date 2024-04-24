from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    app_name: str = "Full Stack To Do App"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "ignore"

# Crear una instancia de Settings que será usada en toda la aplicación
settings = Settings()
