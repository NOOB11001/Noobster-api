from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "mr_noobster"   # tumhari API key

@app.route('/search', methods=['GET'])
def search():
    key = request.args.get('key')
    mobile = request.args.get('mobile')

    # 🔐 API key check
    if key != API_KEY:
        return jsonify({
            "status": "error",
            "message": "Invalid API Key"
        }), 403

    if not mobile:
        return jsonify({
            "status": "error",
            "message": "Mobile number required"
        }), 400

    try:
        url = f"https://tfqdeadlo-inddataapi.hf.space/search?mobile={mobile}"
        res = requests.get(url)
        data = res.json()

        # 🧩 Final modified response
        return jsonify({
            "status": "success",
            "developer": "@mr_noobster",
            "channel": "@noob11001",
            "data": data
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Failed to fetch data"
        }), 500


if __name__ == "__main__":
    app.run()
