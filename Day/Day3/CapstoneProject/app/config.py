from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "it_servicedesk"
    
    App_name: str = "IT Service Desk App API"
    #Information about the app, like version, description, contact info, etc. can be added here as well
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
#Shared settiings Objecte that all other files can import and use
settings = Settings()