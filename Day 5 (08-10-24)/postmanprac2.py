from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (In-memory)
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
]

# Read (GET): Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Read (GET): Get a single item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Create (POST): Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Update (PUT): Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.get_json()
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        item.update(updated_item)
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Delete (DELETE): Delete an item by id
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    if items:
        return jsonify({"message": "Item deleted"}), 200
    else:        
        return jsonify({"error": "Item not found"}), 404

        


if __name__ == '__main__':
    app.run(debug=True)
