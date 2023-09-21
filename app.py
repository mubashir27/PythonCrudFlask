from flask import Flask, request, jsonify

app = Flask(__name__)

# GET API
@app.route('/api/resource', methods=['GET'])
def get_resource():
    # Logic to retrieve resource data
    data = {"message": "This is a GET request."}
    return jsonify(data)

# POST API
@app.route('/api/resource', methods=['POST'])
def create_resource():
    # Logic to create a new resource
    data = {"message": "This is a POST request."}
    return jsonify(data), 201  # 201 Created status code

# PUT API
@app.route('/api/resource/<int:id>', methods=['PUT'])
def update_resource(id):
    # Logic to update an existing resource with the specified ID
    data = {"message": f"This is a PUT request for resource {id}"}
    return jsonify(data)

# DELETE API
@app.route('/api/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    # Logic to delete the resource with the specified ID
    data = {"message": f"This is a DELETE request for resource {id}"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
