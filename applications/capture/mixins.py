from django.http import JsonResponse


class AjaxFormMixin:
    def get(self, *args, **kwargs):
        return JsonResponse({}, status=400)

    def mail_object(self):
        raise NotImplementedError

    def form_valid(self, form):
        self.object = form.save()
        self.mail_object()
        return JsonResponse({})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)
