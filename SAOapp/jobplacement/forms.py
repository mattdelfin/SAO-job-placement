from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AdminUser, StudentUser

class AdminUserCreationForm(UserCreationForm):
    class Meta:
        model = AdminUser
        fields = ("email",)

class AdminUserChangeForm(UserChangeForm):

    class Meta:
        model = StudentUser
        fields = ("email",)
