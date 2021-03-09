import os

import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://8ecda28343c4405baff033abfd2cd9f1@o540140.ingest.sentry.io/5658103",
    integrations=[BottleIntegration()]
)

from bottle import route, run

@route("/success")
def success():
    return "HTTP 200 OK"
    

@route("/fail")
def fail():
    raise RuntimeError("There is an error!")  
    return  


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
    