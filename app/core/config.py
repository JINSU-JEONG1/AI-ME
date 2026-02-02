from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI-ME"
    API_STR: str = "/api"
    API_V1_STR: str = "/api/v1"

    # 실제 운영 시 변경
    # Database
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "ai-me"
    
    # 실제 운영 시 환경변수로 필수 주입
    # Security
    SECRET_KEY: str = "your-super-secret-key"  
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()
    

    