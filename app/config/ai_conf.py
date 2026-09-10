from pydantic import BaseModel


class AIConfig(BaseModel):
    base_url: str = "http://ai:11434/v1"
    api_key: str = "ollama"
