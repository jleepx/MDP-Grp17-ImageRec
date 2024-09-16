from flask import Flask, jsonify, request
from flask_cors import CORS
from ultralytics import YOLO
import os
app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/status', methods=['GET'])
def status():
    """
    This is a health check endpoint to check if the server is running
    :return: a json object with a key "result" and value "ok"
    """
    return jsonify({"result": "ok"})


@app.route('/image', methods=['POST'])
def image_predict():
    """
    This is the main endpoint for the image prediction algorithm
    :return: a json object with a key "result" and value a dictionary with keys "obstacle_id" and "image_id"
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file to the upload folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    model =YOLO('yolov8weights.pt')
    results  = model(source=filepath, show=True,conf=0.4,save=True )
    response_data = []
    for result in results:
        response_data.append({
            "obstacle_id": result.names[result.boxes.cls[0].item()],  # The class name
            "image_id": file.filename  # Image ID can be the filename
        })
    return jsonify({"result": response_data})

    ## Week 8 ## 
    #signal = constituents[2].strip(".jpg")
    #image_id = predict_image(filename, model, signal)

    ## Week 9 ## 
    # We don't need to pass in the signal anymore
    

    # Return the obstacle_id and image_id
    #result = {
    #    "obstacle_id": obstacle_id,
    #    "image_id": image_id
    #}
    #return jsonify(result)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
