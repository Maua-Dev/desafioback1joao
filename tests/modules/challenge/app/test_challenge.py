
from src.modules.challenge_template.app.challenge import lambda_handler
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.challenge_repository_mock import ChallengeRepositoryMock

class Test_Challenge:
    def test_challenge(self):
        response = lambda_handler(HttpRequest(body="{}"), None)