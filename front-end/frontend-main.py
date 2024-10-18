from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://backend-service:5000/api/data')  # Use the backend service name
    data = response.json()
    return render_template('index.html', message=data['message'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
