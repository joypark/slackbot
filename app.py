from flask import Flask

app = Flask(__name__)

# EUwWh3BEQMmvR745q2wxC3WADuZzXb

PORT = 4390


@app.route('/')
def homepage():
    return "Howdy hacker!!"


@app.route('/scheduleme', methods=['POST'])
def scheduleme():
    return 'I would like to schedule that, but I haven"'"t quite figured out how..."
    return x21 = input('What would you like to show now?')
    return print(x21, 'is good')

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
