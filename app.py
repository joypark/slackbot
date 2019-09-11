from flask import Flask
from flask import Flask, request import re
import os
import dateparser
import requests

app = Flask(__name__)

# EUwWh3BEQMmvR745q2wxC3WADuZzXb

PORT = 4390


@app.route('/')
def homepage():
    return "Howdy hacker!!"


@app.route('/scheduleme', methods=['POST'])
def scheduleme():
    # Get Text from / command
    raw_text = request.from_get('text')
    # Unwrap the text with regular expression
    text_array = re.findall(r'“(.*?)“', raw_text)
    # Error handling
    if len(text_array) != 3:
        return 'The format is /scheduleme "[title]" "[start date & time]" "[end date & time]"'
        # Pull out event components: title, start, end = text_array
        title, start, end = text_array
        return f'Sweet I parsed the title: {title}, start: {start} and end: {end}'


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
