from flask import jsonify
import werkzeug.http


def error_response(status_code, message=None):
    payload = {'error': werkzeug.http.HTTP_STATUS_CODES.get(status_code, 'UNKNOWN ERROR')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code

    return response
