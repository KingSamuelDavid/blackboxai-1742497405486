from flask import Flask, request, jsonify
import os
from tasks import image_to_video

app = Flask(__name__)

@app.route('/image2video', methods=['POST'])
def convert_images_to_video():
    request_data = request.json
    result = image_to_video(request_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)