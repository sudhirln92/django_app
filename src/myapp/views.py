from rest_framework.response import Response
from http import HTTPStatus
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from utils.filehandler import FileHandler
from utils.validate_request import ValidateRequest
from .myfunction.mainApp import MainApp
import logging

logger = logging.getLogger("django_logs")
config = FileHandler().read_json(file_name="config.json", mode="r", add_path="config")

# Create your views here.
class TestView(APIView):
    def get(self, request):
        return Response(data={"hello": "world"})

    def post(self, request, **kwargs):
        return Response(data={"hello": "world"})


class WebhookView(APIView):
    """
    API with JWT toke authetication
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(data={"hello": "world"})

    def post(self, request):
        # validate request
        ValidateRequest.validate_json(request)

        data = request.data
        logger.info(f"received data {str(request.data)}")

        # function
        res_data = MainApp(**config).pipeline(data)
        if res_data:
            return Response(status=HTTPStatus.OK)
        else:
            logger.info(f"invalid phone number")

        return Response(status=HTTPStatus.ALREADY_REPORTED)
