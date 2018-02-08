from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {}
        errors = str(exc)
        #for field, value in response.data.items():
        #    errors += "\n {} : {}".format(field, " ".join(value))

        response.data['error_message'] = errors
        response.data['error'] = True
        response.data['status_code'] = response.status_code
    else:
        response = Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response.data = {}
        errors = str(exc)
        response.data['error_message'] = errors
        response.data['error'] = True
        response.data['status_code'] = response.status_code

        #response.data['exception'] = str(exc)

    return response