import time
from flask import Flask
import sem_search

app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.route('/upload_doc', methods=['POST', 'GET'])
@cross_origin()
def handle_doc():
    #if request.method == 'POST':
        data = request.json.get("file")
        if not data:
            return jsonify({"error": "No file provided!"}), 400
        print("this is data", data)
        text_data = data
        results = sem_search(text_data)
        return jsonify({"message": "Received Successfully!", "results": results})
    #else:
    #    return jsonify({"message": "GET request received."})

@app.route("/", methods=["GET"])
def send_results():
    return ["test", "test2"]

@app.route("/", methods=["GET"])
def test_endpoint():
    return "Server is active!"

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    return {'time': sem_search(text)}
