import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups/"
    ENDPOINT = f"{ENDPOINT_PREFIX}"

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ENDPOINT, json_data=json)
        return response
