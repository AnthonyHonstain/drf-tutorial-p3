import json
from django.http import HttpResponse

from drfauth.models import Token


def json_response(response_dict, status=200):
    # TODO - this is not very secure, need to revisit this again in the future.
    response = HttpResponse(json.dumps(response_dict), content_type="application/json", status=status)
    # These are important for Django to play nice with CORS.
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


def token_required(func):
    def inner(request, *args, **kwargs):
        # Why do we have special logic for 'OPTIONS' ??
        if request.method == 'OPTIONS':
            return func(request, *args, **kwargs)

        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
        if auth_header is not None:
            tokens = auth_header.split(' ')
            if len(tokens) == 2 and tokens[0] == 'Token':
                token = tokens[1]
                try:
                    request.token = Token.objects.get(token=token)
                    return func(request, *args, **kwargs)
                except Token.DoesNotExist:
                    return json_response({'error': 'Token not found'}, status=401)

        return json_response({'error': 'Invalid Header'}, status=401)
    return inner