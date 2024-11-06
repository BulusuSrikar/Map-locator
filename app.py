from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for user locations
locations = []

@app.route('/locations', methods=['GET', 'POST'])
def manage_locations():
    if request.method == 'POST':
        location = request.json
        locations.append(location)
        return jsonify(location), 201
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)
