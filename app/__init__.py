"""
Do not load view at the top because they pull controllers which need db to be set up
"""
import os
from fastapi import FastAPI

def create_app():
    print('create_app...')
    app = FastAPI()
    from app import database
    print('db is set up')
    return app
