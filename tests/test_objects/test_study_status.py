import aiohttp
import pytest

from aioalfacrm import crud_objects
from aioalfacrm import models
from aioalfacrm.core import AuthManager, ApiClient
from . import add_auth_request

STUDY_STATUS_RESPONSE = {
    'page': 0,
    'total': 1,
    'count': 1,
    'items': [
        {
            'id': 1,
            'name': 'Name',
            'is_enabled': 1,
        },
    ]
}


@pytest.fixture
def auth_manager():
    session = aiohttp.ClientSession()
    yield AuthManager(
        email='test@test.test',
        api_key='api-key',
        hostname='demo.s20.online',
        session=session,
    )


@pytest.fixture
def api_client(auth_manager: AuthManager):
    yield ApiClient(
        hostname='demo.s20.online',
        branch_id=1,
        auth_manager=auth_manager,
        session=auth_manager._session,  # noqa
    )


@pytest.mark.asyncio
async def test_study_status(api_client, aresponses):
    add_auth_request(aresponses)
    aresponses.add('demo.s20.online', '/v2api/1/study-status/index', 'POST', STUDY_STATUS_RESPONSE)

    study_status_object = crud_objects.StudyStatus(
        api_client=api_client,
        model_class=models.StudyStatus,
    )

    study_statuses = await study_status_object.list()

    assert len(study_statuses) == 1
    study_status = study_statuses[0]

    assert study_status.id == 1
    assert study_status.name == 'Name'
    assert study_status.is_enabled is True
