from flask import Flask, request, jsonify,render_template
app = Flask(__name__)

# Sample in-memory data storage
data_store = []

# GET method to retrieve data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store), 200

# POST method to add data
@app.route('/submit', methods=['POST'])
def post_data():
    data = request.get_json()

    api_input = data.get('apiInput')
    filters = data.get('filters')

    # Process the data as needed
    print("Received API Input:", api_input)
    print("Received Filters:", filters)

    # Respond back to the client
    response = {
        "status": "success",
        "data": {
            "apiInput": api_input,
            "filters": filters
        }
    }

    return jsonify(response)
@app.route("/")
def main():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)
