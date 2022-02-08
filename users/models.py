from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=True)
    is_tutor = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, age, gender, user_type, address, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not age:
            raise ValueError("Users must have an age")
        if not gender:
            raise ValueError("Users must have a gender")
        if not user_type:
            raise ValueError("Users must have a user type defined")
        if not address:
            raise ValueError("Users must have an address defined")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            age = age,
            gender = gender,
            user_type = user_type,
            address = address,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, age, gender, user_type, address, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            age = age,
            gender = gender,
            user_type = user_type,
            address = address,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    id = models.AutoField(int, null=False, primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=200, unique=True)
    username = models.CharField(verbose_name="username", max_length=100, unique=True)
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_student = models.BooleanField(default = False)
    is_tutor = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    age = models.IntegerField()
    gender = models.CharField(max_length = 15)
    user_type = models.CharField(max_length = 15)
    address = models.CharField(max_length = 300, default = 'None')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'age', 'gender', 'user_type', 'address']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    objects = MyAccountManager()