from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    try:
        fetchedValue = redis.get("k1")
    except RedisError as err:
        fetchedValue = "Error getting value for k1: {0}".format(err)

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}<br/>" \
           "<b>k1:</b> {fetchedValue}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits, fetchedValue=fetchedValue)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
