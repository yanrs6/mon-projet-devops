from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Mon projet DevOps</title>
    </head>
    <body>
        <h1>Mon premier projet DEVOPS !</h1>
        <p>Mon application Flask fonctionne.</p>
        <p>Prochaine étape : Docker et CI/CD.</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
