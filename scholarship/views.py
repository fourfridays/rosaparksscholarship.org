from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from users.models import User
from formtools.wizard.views import SessionWizardView
from scholarship.forms import EmploymentHistoryForm
from page.storage_backends import PrivateMediaStorage


class ScholarshipView(LoginRequiredMixin, SessionWizardView):
    template_name = "scholarship/index.html"
    form_list = [EmploymentHistoryForm]
    file_storage = PrivateMediaStorage()

    def done(self, form_list, **kwargs):
        employment_history_form = form_list[0]
        if employment_history_form.cleaned_data:
            employment_history = employment_history_form.save(commit=False)
            employment_history.user = User.objects.get(email=self.request.user)
            employment_history.save()
        return HttpResponse("Form Submitted")
