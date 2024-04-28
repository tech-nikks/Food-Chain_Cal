from flask import Flask, request, jsonify
from streamlit_app import get_nutritional_values

app = Flask(__name__)

@app.route('/api/get_nutritional_values', methods=['GET'])
def get_nutritional_values_route():
    dish_name = request.args.get('dish_name')
    nutritional_info = get_nutritional_values(dish_name)
    return jsonify(nutritional_info)

if __name__ == '__main__':
    app.run(debug=True)
