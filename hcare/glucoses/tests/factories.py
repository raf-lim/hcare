import random
from datetime import datetime
import factory
from factory.fuzzy import FuzzyDateTime
from pytz import UTC

from hcare.users.tests.factories import UserFactory


class GlucoseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'glucoses.Glucose'

    user = factory.SubFactory(UserFactory)
    glucose = factory.LazyAttribute(lambda x: random.randint(60, 350))
    recorded = factory.LazyAttribute(lambda x: FuzzyDateTime(
        datetime(2021, 1, 1, tzinfo=UTC)).fuzz()
    )

