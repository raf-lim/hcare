import pytest
from django.test import RequestFactory, client
from django.urls import reverse
from django.forms import DateTimeInput

from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils import timezone

from hcare.bloodpressures.views import BloodPressureCreateView


pytestmark = pytest.mark.django_db


class TestBloodPressureListView:

    def test_user_without_measurements(self, user):
        c = client.Client()
        c.force_login(user)
        response = c.get(reverse('bloodpressures:list'))
        assert 'object_list' in response.context
        assert response.context.get('object_list').count() == 0

    def test_user_with_measurements(self, bloodpressure):
        c = client.Client()
        c.force_login(bloodpressure.user)
        response = c.get(reverse('bloodpressures:list'))
        assert 'object_list' in response.context
        assert response.context.get('object_list').count() == 1

    def test_user_checks_other_user_measurements(self, bloodpressure, user):
        assert bloodpressure.user is not user
        c = client.Client()
        c.force_login(user)
        response = c.get(reverse('bloodpressures:list'))
        assert 'object_list' in response.context
        assert response.context.get('object_list').count() == 0


class TestBloodPressureCreateView:
    def test_get_form(self, request_factory: RequestFactory):
        view = BloodPressureCreateView()
        request = request_factory.get(reverse("bloodpressures:add"))
        view.setup(request)
        form = view.get_form()
        assert isinstance(form.fields['recorded'].widget, DateTimeInput)


def test_form_valid(self, user, request_factory):
    data = {'systolic': 140, 'diastolic': 105, 'pulse': 70, 'record_datetime': timezone.now()}
    request = request_factory.post(reverse("bloodpressures:add"), data=data)
    request.user = user
    session_middleware = SessionMiddleware()
    session_middleware.process_request(request)
    msg_middleware = MessageMiddleware()
    msg_middleware.process_request(request)
    response = BloodPressureCreateView.as_view()(request)
    user.refresh_from_db()
    assert response.status_code == 302
    bp = user.bloodpressure_set.last()
    assert bp.systolic == data.get('systolic')
    assert bp.diastolic == data.get('diastolic')
    assert bp.pulse == data.get('pulse')
    assert bp.recorded == data.get('recorded')
