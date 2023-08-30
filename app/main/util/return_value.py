def return_value_200(message, data=None):
    return get_response_obj(200, message, data)


def return_value_201(message, data=None):
    return get_response_obj(201, message, data)


def return_value_400(message):
    return get_response_obj(400, message)


def return_value_401(message):
    return get_response_obj(401, message)


def return_value_500(message):
    return get_response_obj(500, message)


def get_response_obj(status, message, data=None):
    resp = {
        "status": status,
        "message": message
    }

    if data:
        resp['data'] = data

    return resp, status
