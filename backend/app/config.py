import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # ทุกคนใช้เหมือนกัน
    SECRET_KEY = 'snake&fish'   

    # เปลี่ยนเป็นของตัวเองใน .env
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") 
    SQLALCHEMY_TRACK_MODIFICATIONS = False