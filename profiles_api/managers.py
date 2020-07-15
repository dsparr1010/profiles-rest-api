from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles - specify functions that can be used to manipulate objects within the model that the manager is for"""

    def create_user(self, email, name, password=None):
        # if no password is given, it gives the value as None. Django looks for a password to hash and if it does not find one, will throw an error
        """Create new user profile"""
        if not email:
            raise ValueError("Must provide an email to create a profile")
        email = self.normalize_email(email)

        # crates a new model that the Manager is representing
        # by default self.model creates an instance of the class that the manager is for
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a superuser w given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

