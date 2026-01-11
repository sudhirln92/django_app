from django.utils import timezone
from django.db import connection
import requests
import logging
import json

from ..serializers import ExternaltokenSerializer
from ..models import Externaltoken

logger = logging.getLogger("django_logs")


class BaseApi:
    """
    Methods:
        authentication
        parse content
    param:
        auth_api
        baseUrl
        token_api_name
    """

    def __init__(self, baseUrl, auth_api, token_api_name, **kwargs) -> None:
        self.baseUrl = baseUrl
        self.auth_api = auth_api
        self.token_api_name = token_api_name

    def check_available_token(self, api_name):
        """
        Check available token and expire time
        """
        with connection.cursor() as cursor:
            # query
            query = f"""
            SELECT token_json
            FROM tobiAdaptor_externaltoken
            WHERE (julianday('now') - updated_at) < expires_in
            AND api_name = '{api_name}' ;
            """

            # cursor
            cursor.execute(query)
            rows = cursor.fetchall()

            if len(rows) == 0:
                return None
            else:
                logger.info("Existing token is used")
                token_json = json.loads(rows[0][0])
                return token_json

    def store_token(self, token, api_name, expires_in):
        # store token
        data = {
            "api_name": api_name,
            "token_json": token,
            "expires_in": expires_in,
            "updated_at": timezone.now(),
        }

        token_data = Externaltoken.objects.filter(api_name=api_name)
        if token_data.count() == 0:
            # store new token
            serial = ExternaltokenSerializer(data=data)
            if serial.is_valid():
                serial.save()
                logger.info("ExternaltokenSerializer successed to save")
            else:
                logger.info("ExternaltokenSerializer failed to save")
        else:
            # update new token
            token_data.update(**data)
            logger.info("updated existing token")

    def auth(self):
        # authenticate_brand_embassy
        url = self.auth_api["api"].format(baseUrl=self.baseUrl)
        headers = self.auth_api["headers"]
        data = self.auth_api["data"]

        # check available valid token
        token = self.check_available_token(api_name=self.token_api_name)
        if token == None:
            # no valid token avaliable
            # post
            res_data = requests.post(url, data=data, headers=headers)

            token = self.parse_content(res_data, f"auth {self.token_api_name}")

            # save access token and time
            self.store_token(token, self.token_api_name, token["expires_in"])

        return token

    def prepare_request_param(
        self, api, api_param, method, data=None, headers=None, log_msg=""
    ):
        # format api
        url = api.format(**api_param)

        res_data = requests.request(method=method, url=url, data=data, headers=headers)

        # parse content
        res_data = self.parse_content(data, log_msg)

        return res_data

    def parse_content(self, data, msg=""):
        # parse content
        content = data.content
        content = json.loads(content)

        if data.status_code < 310:
            logger.info(f"API {msg} status code: {data.status_code}")
        else:
            logger.error(
                f"API {msg} status code: {data.status_code} content: {content}"
            )

        return content
