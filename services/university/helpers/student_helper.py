import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"
    ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT, json_data=json)
        return response