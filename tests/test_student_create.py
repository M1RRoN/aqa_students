import random

import requests

from logger.logger import Logger

from faker import Faker

from main import logger
from services.auth.auth_service import AuthService
from services.auth.helpers.user_helper import UserHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.model.base_student import DegreeEnum
from services.university.model.group_request import GroupRequest
from services.university.model.student_request import StudentRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestStudent:
    def test_student_create(self, university_api_utils_admin):
        logger.info("### Steps 1. Create group")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group)

        logger.info("### Steps 1. Create student")
        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice([option for option in DegreeEnum]),
                                 phone=f"+7{faker.random_number(digits=10, fix_len=True)}",
                                 group_id=group_response.id)
        student_response = university_service.create_student(student_request=student)

        assert student_response.group_id == group_response.id, \
            f"Wrong group id. Actual: '{student_response.group_id}', but expected: '{group_response.id}'"

    def test_me(self, auth_api_utils_admin):
        auth_service = AuthService(api_utils=auth_api_utils_admin)
        me_response = auth_service.get_me()

        assert me_response.status_code == 200, f"Wrong status code. Actual: '{me_response.status_code}', but expected: {requests.status_codes.codes.ok}"
