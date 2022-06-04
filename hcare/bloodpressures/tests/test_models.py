import pytest

from hcare.bloodpressures.models import BloodPressure

pytestmark = pytest.mark.django_db


def test_glucose_get_absolute_url(bloodpressure: BloodPressure):
    assert bloodpressure.get_absolute_url() == f"/bloodpressures/{bloodpressure.id}/"
