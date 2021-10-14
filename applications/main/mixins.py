class StaffQuerysetMixin:
    def get_queryset(self):
        if self.request.user.is_staff:
            self.queryset = self.model.objects.all()
        return super().get_queryset()
