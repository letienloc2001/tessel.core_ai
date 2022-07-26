import json

from flask import Blueprint, request, current_app
from flask.wrappers import Response

from itertools import chain

classification_bp = Blueprint('classification_bp', __name__)


@classification_bp.route("/anti_spoofing", methods=["POST"])
def verify_anti_spoofing_image() -> Response:
    """
    Controller Anti-Spoofing Image

    Returns:
        object: response object containing anti-spoofing information.
    """
    
    input_json = request.get_json()

    if "images" not in input_json or not input_json["images"]:
        return current_app.response_class(
            response={},
            status=409,
            mimetype='application/json',
        )
        
    images = input_json['images']

    nested_result = current_app.models["ANTI_SPOOFING_CLASSIFICATION"](images)
    result = list(chain(*nested_result))
    
    prediction = []
    for value in result:
        prediction.append({
            "image_id": "IMAGE_ID",
            "is_spoof_image": int(value[0]),
        })

    return current_app.response_class(
        response=json.dumps(prediction),
        status=200,
        mimetype='application/json',
    )

@classification_bp.route("/train_anti_spoofing", methods=["POST"])
def train_anti_spoofing() -> Response:
    """
    Train anti-spoofing model

    Returns:
        response object containing anti-spoofing training information.
    """

    input_json = request.get_json()

    # Check whether 'dataset' and 'configuration' in json
    if any([x not in input_json or not input_json[x] for x in ('dataset', 'configuration')]):
        return current_app.response_class(
            response={'🤡 Lack of information in json.'},
            status=409,
            mimetype='application/json',
        )

    data_set = input_json['dataset']
    configuration = input_json['configuration']

    trained_model_path = current_app.models["ANTI_SPOOFING_CLASSIFICATION"].train(data_set, configuration)

    return current_app.response_class(
        response={f'🚀 Training Completed. Best checkpoint at: "{trained_model_path}"'},
        status=200,
        mimetype='application/json',
    )
