from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,Mobile_number,password=None,**extra_fields):

        if not Mobile_number:
            raise ValueError("Mobile_number is required")

        Mobile_number=self.normalize_email(Mobile_number)
        user=self.model(Mobile_number=Mobile_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,Mobile_number,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)         
        extra_fields.setdefault('is_superuser',True)         
        extra_fields.setdefault('is_active',True)         
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Error'))

        return self.create_user(Mobile_number,password,**extra_fields)    