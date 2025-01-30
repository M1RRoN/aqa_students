from utils.api_utils import ApiUtils
from .helpers.group_helper import GroupHelper
from .helpers.student_helper import StudentHelper
from .model.group_request import GroupRequest
from .model.group_response import GroupResponse
from .model.student_request import StudentRequest
from .model.student_response import StudentResponse
from services.general.base_service import BaseService


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def create_group_and_student(self, group_request: GroupRequest, student_request: StudentRequest) -> StudentResponse:
        self.create_group(group_request)
        return self.create_student(student_request)

    def create_random_group(self):
        raise NotImplementedError