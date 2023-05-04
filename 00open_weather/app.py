import streamlit as st
import os
from dotenv import load_dotenv
import requests

load_dotenv('.env')
api_key : str = os.getenv('API_KEY')
api_key