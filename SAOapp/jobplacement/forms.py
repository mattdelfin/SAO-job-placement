from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import JobPlacementAdminUser, StudentUser

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = JobPlacementAdminUser
        fields = ("email",)

class AdminUserChangeForm(UserChangeForm):

    class Meta:
        model = StudentUser
        fields = ("email",)
