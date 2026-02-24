from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    return jsonify({
        "response_type": "in_channel",
        "attachments": [
            {
                "title": "Грубое и надменное общение с клиентами",
                "title_link": "https://ваш-сайт.ru/article",
                "text": "Ознакомьтесь со статьёй.",
                "image_url": "https://ваш-сайт.ru/image.jpg"
            }
        ]
    })

if __name__ == "__main__":
    app.run()
