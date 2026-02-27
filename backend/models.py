from pydantic import BaseModel
from typing import Optional

class BrandRequest(BaseModel):
    industry: str
    keywords: str
    tone: str = "Professional"
    language: str = "en"

class ContentRequest(BaseModel):
    brand_description: str
    tone: str = "Professional"
    content_type: str = "product_description"
    language: str = "en"

class SentimentRequest(BaseModel):
    text: str
    brand_tone: str = "Professional"

class ColorRequest(BaseModel):
    tone: str
    industry: str

class ChatRequest(BaseModel):
    message: str

class LogoRequest(BaseModel):
    brand_name: str
    industry: str
    keywords: str

class SummarizeRequest(BaseModel):
    text: str

class CompetitorRequest(BaseModel):
    brand_name: str
    industry: str
    target_audience: str
    unique_value: str

class BrandVoiceRequest(BaseModel):
    brand_name: str
    industry: str
    values: str
    audience: str
    tone: str = "Professional"
