from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://localhost:5000/api/data')  # Adjust the service name as needed
    data = response.json()
    return render_template('index.html', message=data['message'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
