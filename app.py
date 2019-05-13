from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, request
import os
import boto3

app = Flask(__name__)

#from models import Result
@app.route('/', methods=['GET', 'POST'])
def index():
    #VARIAVEIS
    errors = []
    results = {}
    sqs = boto3.client('sqs', region_name='us-east-2')
    queue_url = 'SQS_QUEUE_URL'

    if request.method == "POST":
        string = request.form['string']
        #r = requests.post('http://',string)
        #soup = BeautifulSoup(r.content, 'lxml')
        try:
            response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={''},
            MessageBody=(string))
        except:
            errors.append(
                "Erro."
            )

    return render_template('index.html', errors=errors, results=results)

if __name__ == "__main__":
    app.run(debug='false',host='0.0.0.0')
