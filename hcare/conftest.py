import pytest
from django.test import RequestFactory

from hcare.users.models import User
from hcare.users.tests.factories import UserFactory

from hcare.bloodpressures.models import BloodPressure
from hcare.bloodpressures.tests.factories import BloodPressureFactory

from hcare.glucoses.models import Glucose
from hcare.glucoses.tests.factories import GlucoseFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture
def bloodpressure() -> BloodPressure:
    return BloodPressureFactory()


@pytest.fixture
def glucose() -> Glucose:
    return GlucoseFactory()
