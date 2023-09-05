from django.http import JsonResponse
from django.views.generic import CreateView, TemplateView
from user.forms import RegistrationForm

class UserView(CreateView):
    form_class = RegistrationForm
    template_name = "user/index.html"

    def post(self, request, *args, **kwargs):
        user = RegistrationForm(request.POST)
        if request.method == "POST":
            if user.is_valid():
                user.save()
                return JsonResponse({'response':'success'}, status=200)
        return JsonResponse(user.errors, status=400)

class UserDetail(TemplateView):
    template_name = "user/user_info.html"
