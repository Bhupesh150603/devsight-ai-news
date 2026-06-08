import os

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
MONGO_URI = os.environ.get('MONGO_URI')
DB_NAME = 'blog_automation'
COLLECTION_NAME = 'articles'

NEWS_SOURCES = [
    # Ai news 
    'https://news.mit.edu/topic/artificial-intelligence2',
    'https://techcrunch.com/category/artificial-intelligence/',
    'https://spectrum.ieee.org/topic/artificial-intelligence/',
    'https://thenewstack.io/ai/',
    
    
]

TIMEFRAME_HOURS = 24
