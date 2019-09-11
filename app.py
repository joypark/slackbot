from flask import Flask, request
import re
import dateparser
import requests
import os

# EUwWh3BEQMmvR745q2wxC3WADuZzXb
app = Flask(__name__)
PORT = 4390


@app.route('/')
def homepage():
    return "Howdy hacker!!"


@app.route('/scheduleme', methods=['POST'])
def scheduleme():
    # Get Text from / command
    raw_text = request.form.get('text')
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
