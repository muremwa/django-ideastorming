from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from authapp.views import login

from .models import Project
from .forms import NewProjectForm


"""
VIEW FROM PROJECT APP
"""

def index(request):
    return login(request)


@method_decorator(login_required, name='dispatch')
class ProjectNewView(CreateView):
    model = Project
    template_name = 'new_project.html'
    success_url = '/new-project/'
    form_class = NewProjectForm

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(ProjectNewView, self).get_form_kwargs(**kwargs)
        form_kwargs["user"] = self.request.user
        return form_kwargs

    def get_context_data(self, **kwargs):
        context = super(ProjectNewView, self).get_context_data(**kwargs)
        context['page'] = 'new-project'
        return context

#   ????
#    def form_valid(self, form):
#        form.save()
#        return super(NewProject, self).form_valid(form) 


   