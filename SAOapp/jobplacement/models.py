from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission, Group

from .managers import AdminUserManager, StudentUserManager
# Create your models here.

class JobPlacementAdminUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=10, primary_key=True, blank=False, null=False)
    email = models.EmailField(_("email address"), unique = True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
 
    objects = AdminUserManager()

    def __str__(self):
        return self.email
    
        #define reverse accessor for GROUP
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        related_name="admin_user_groups"  # Specify a related_name to resolve the clash
    )
        #define reverse accessor for Permission
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        related_name="admin_user_permissions"  # Specify a related_name to resolve the clash
    )

class StudentUser(AbstractBaseUser, PermissionsMixin):
        # student login credentials
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

        # student info
    email = models.EmailField(_("email address"), unique = True)
    studID = models.PositiveIntegerField(primary_key=True)
    lrn = models.PositiveBigIntegerField(null=False, blank=False)
    firstname = models.CharField(max_length=50, blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=False, null=False)
    middlename = models.CharField(max_length=50, null=True, blank=True)
    #degree = models.ForiegnKey(DegreeModel, null=True, blank=True, on_delete=models.CASCADE)
    yearlvl = models.PositiveIntegerField(default="1", null=False)
    sex = models.CharField(max_length=1, default="M", null=False)
    contact = models.CharField(max_length=11, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = StudentUserManager()

        #define reverse accessor for GROUP
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        related_name="student_user_groups"  # Specify a related_name to resolve the clash
    )
        #define reverse accessor for Permission
    user_permissions = models.ManyToManyField(
    Permission,
    verbose_name=_("user permissions"),
    blank=True,
    related_name="student_user_permissions"  # Specify a related_name to resolve the clash
    )

    class Meta:
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return self.email
    
class OJTHiring(models.Model):
    pass

class OJTRequirements(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE) # Change to Students Model
    non_disclosure = models.BooleanField(default=False)
    biodata = models.BooleanField(default=False)
    parents_consent = models.BooleanField(default=False)
    application_letter = models.BooleanField(default=False)
    medical = models.BooleanField(default=False)
    moa = models.BooleanField(default=False)
    endorsement = models.BooleanField(default=False)

    def __str__(self):
        return self.student.email

class Seminar(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, default="")
    theme = models.CharField(max_length=150, null=False, default="")
    date_of_event = models.DateField(null=False, default="")

    def __str__(self):
        return self.title

# class SeminarAttendance(models.Model):
#     student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
#     seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
#     attended = models.BooleanField(default=False)

#     def __str__(self):
#         return self.attended

class SeminarAttendance(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE) # Change to studentModel
    seminar = models.ForeignKey(Seminar, null=True, on_delete=models.SET_NULL)
    attended = models.BooleanField(default=False)

