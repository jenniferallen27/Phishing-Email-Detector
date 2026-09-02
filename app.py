from flask import Flask, render_template, request
import re
from urlib.parse import urlparse

app = Flask(__name__)

# detection functions
# check for urgency, credential words, and threats
# check for urls and analyze
# check sender address
# create score percentage

# connect to flask