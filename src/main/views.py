import glob
import os
from subprocess import call

from django.views.generic import TemplateView, CreateView
from django_countries import settings

from .models import ClassImage
from .forms import ImageForm
# from .MTCNN_extract_faces import extract_faces


class HomeView(CreateView):
    template_name = "index.html"
    form_class = ImageForm
    success_url = '/attendance'

    def form_valid(self, form):
        # extract_faces()
        return super().form_valid(form)


class AttendanceView(TemplateView):
    template_name = "attendance.html"

    # def get(self, request, *args, **kwargs):
    #     media_path = settings.MEDIA_ROOT
    #     file_path = os.path.join(media_path, "class")
    #     for file in glob.glob(file_path + "**/*", recursive=True):
    #         #extract_faces()
    #         ClassImage.objects.all().delete()
    #         # os.remove(file)
    #     context = self.get_context_data(**kwargs)
    #     return self.render_to_response(context)
