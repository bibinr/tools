"""
Call http://127.0.0.1/process using postman.
Any data posted is passed on to the postProcess method
"""

from flask import Flask, Response, request
from threading import Thread
import requests


app = Flask(__name__)


@app.route("/postprocess")
def postprocess():
    """
    Method can take the request and do some action.
    Typically this would act as the more time consuming action
    """
    print request.values
    return "Success"


def callPostProcess(payload):
    """
    This method takes the data from the original request and passes it on
    Helps break the synchronous operation
    """
    requests.post("http://127.0.0.1:5000/postprocess", data=payload)


@app.route("/process", methods=['GET', 'POST'])
def process():
    """
    Takes the original request, passes on the request to act asynchrounously
    and responds to caller
    """
    data = request.values
    t = Thread(target=callPostProcess, args=data)
    t.start()
    response = Response(status=200)
    return response


if __name__ == "__main__":
    app.run()
