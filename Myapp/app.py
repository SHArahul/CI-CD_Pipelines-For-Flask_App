import os
from flask import Flask

app = Flask(__name__)

def get_greeting():
    """Return greeting message based on environment."""
    env = os.getenv("ENV", "dev")  # default is 'dev' for staging
    if env == "test":
        return "Hello, CI_CD from Flask"  # for pytest
    return f"Hello, CI_CD from Flask ({env}) "

@app.route('/')
def hello():
    return get_greeting()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)