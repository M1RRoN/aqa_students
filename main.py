from faker import Faker

from logger.logger import Logger

faker = Faker()

logger = Logger(__name__)

username = faker.user_name()
password = faker.password(
    length=20,
    special_chars=True,
    digits=True,
    upper_case=True,
    lower_case=True
)
