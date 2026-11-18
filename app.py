from flask import Flask

app = Flask(__name__)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/release-check/<int:failed_tests>")
def release_check(failed_tests):
    return {"failed_tests": failed_tests, "can_release": failed_tests == 0}
