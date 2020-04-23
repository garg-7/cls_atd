from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView
from .forms import ImageForm


class HomeView(CreateView):
    template_name = "index.html"
    form_class = ImageForm
    success_url = '/attendance'

    # def form_valid(self, form):
    #     img = form.cleaned_data.get("upload_image")
    #     print(img)
    #     return super().form_valid(form)


class AttendanceView(TemplateView):
    template_name = "attendance.html"
