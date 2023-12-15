from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()

    # Implement your data processing logic here
    # Example: Return the received data as is
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

