import os

from os.path import join, dirname
from dotenv import load_dotenv

path = join(dirname(__file__), '.env')
load_dotenv(path)

