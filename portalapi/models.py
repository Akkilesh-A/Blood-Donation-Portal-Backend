from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from xid import XID


class Scope(models.Model):
    """
    Model representing a scope for role-based access control.

    Attributes:
        entity (str): The model involved in the scope.
        action (str): The activity (e.g., create, view, update, destroy) in the viewset.
        level (str): The hierarchical level determining data access.
        scope (str): The complete scope in the format "entity.action.level".
        slug (AutoSlugField): A unique slug automatically generated from the scope.

    Methods:
        __str__: Returns the string representation of the scope.
        save: Overrides the default save method to automatically generate the scope if not provided.

    Usage:
        Each instance of this model represents a specific scope for role-based access control.

    Example:
        scope_instance = Scope(entity='ModelName', action='create', level='public')
        scope_instance.save()
    """

    entity = models.CharField(max_length=100)
    action = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=100, blank=True)
    scope = models.CharField(max_length=100, blank=True)
    slug = AutoSlugField(populate_from="scope", unique=True)

    def __str__(self):
        return self.scope

    def save(self, *args, **kwargs):
        if self.scope is None:
            self.scope = f"{self.entity}.{self.action}.{self.level}"
        super().save(*args, **kwargs)


# # Create your models here.
class Role(models.Model):
    """
    A model representing a user role in the system
    Attributes:
        name (str): The name of the role.
        tags (TaggableManager): A manager for handling tags (scopes) associated with the role.
        modified_date (datetime): The date and time when the role was last modified.

    Methods:
        __str__: Returns a human-readable string representation of the role.

    Example:
        role = Role.objects.create(name='Admin')
        role.tags.add('read', 'write', 'delete')
        role.save()
        print(role)  # Output: "Admin"
    """

    name = models.CharField(max_length=100)
    scopes = models.ManyToManyField(Scope)
    modified_date = models.DateTimeField(auto_now=True, editable=True)
    is_public_role = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        if self.is_public_role:
            return "Public: " + self.name
        return "Private: " + self.name


class BloodType(models.Model):
    blood_type = models.CharField(max_length=100)
    compatible_with = models.CharField(max_length=100)

    def __str__(self):
        return self.blood_type


class User(AbstractUser):
    id = models.CharField(
        max_length=100,
        primary_key=True,
        default=XID().string(),
        unique=True,
        editable=False,
    )
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    contact = PhoneNumberField(blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_contact_verified = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    house_no = models.CharField(
        max_length=300, null=True, help_text="House No/House Name/Street Name"
    )
    state = models.CharField(max_length=255, null=True)
    pin_code = models.CharField(
        max_length=500,
        validators=[
            RegexValidator(
                "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$", message="Enter a Valid PIN Code"
            )
        ],
        null=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = XID().string()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    @property
    def display_address(self):
        my_address = f"{self.house_no}, {self.state}, {self.pin_code}"
        return my_address
