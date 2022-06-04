import pytest

from hcare.glucoses.models import Glucose

pytestmark = pytest.mark.django_db


def test_glucose_get_absolute_url(glucose: Glucose):
    assert glucose.get_absolute_url() == f"/glucoses/{glucose.id}/"
