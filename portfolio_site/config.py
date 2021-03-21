import os

class Config:
	SECRET_KEY = os.environ.get("SITE_SECRET_KEY")
