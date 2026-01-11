from rest_framework.response import Response
from http import HTTPStatus


class ValidateRequest:
    """
    Validate content type
    1. json
    2. multipart/form-data

    """

    @staticmethod
    def validate_json(request):
        # validate content type json
        if request.headers.get("Content-Type") != "application/json":
            data = {
                "status": HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
                "Content-Type": request.headers.get("Content-Type"),
            }
            return Response(data=data, status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    @staticmethod
    def validate_formdata(request):
        # validate content type multipart/form-data
        if request.headers.get("Content-Type", "").startswith("multipart/form-data"):
            pass
        else:
            data = {
                "status": HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
                "Content-Type": request.headers.get("Content-Type"),
            }
            return Response(data=data, status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
