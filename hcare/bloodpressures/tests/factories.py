import random
from datetime import datetime
import factory
from factory.fuzzy import FuzzyDateTime
from pytz import UTC

from hcare.users.tests.factories import UserFactory


class BloodPressureFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'bloodpressures.BloodPressure'

    user = factory.SubFactory(UserFactory)
    systolic = factory.LazyAttribute(lambda x: random.randint(90, 250))
    diastolic = factory.LazyAttribute(lambda x: random.randint(60, 120))
    pulse = factory.LazyAttribute(lambda x: random.randint(70, 200))
    recorded = factory.LazyAttribute(lambda x: FuzzyDateTime(
        datetime(2021, 1, 1, tzinfo=UTC)).fuzz()
    )
