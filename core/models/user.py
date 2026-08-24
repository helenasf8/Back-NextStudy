"""
Database models.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from uploader.models import Image


class UserManager(BaseUserManager):
    """Manager for users."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""

    email = models.EmailField(max_length=255, unique=True, verbose_name=_('email'), help_text=_('Email'))
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('name'), help_text=_('Username'))

    foto = models.ForeignKey(
        Image,
        related_name='user_foto',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    bio = models.TextField(blank=True, default='')

    OBJETIVO_CHOICES = [
        ('MELHORAR_NOTAS', 'Melhorar notas'),
        ('VESTIBULAR', 'Passar em vestibular'),
        ('APRENDER', 'Aprender algo novo'),
        ('CONSTANCIA', 'Manter constância'),
    ]
    objetivo = models.CharField(max_length=20, choices=OBJETIVO_CHOICES, blank=True, default='')

    materia_favorita = models.ForeignKey(
        'core.Materia',
        related_name='usuarios_favoritos',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    HORARIO_CHOICES = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite'),
        ('MADRUGADA', 'Madrugada'),
    ]
    melhor_horario = models.CharField(max_length=15, choices=HORARIO_CHOICES, blank=True, default='')

    meta_diaria_minutos = models.PositiveIntegerField(default=60)

    TEMA_CHOICES = [
        ('AZUL', 'Azul'),
        ('ROXO', 'Roxo'),
        ('VERDE', 'Verde'),
        ('LARANJA', 'Laranja'),
        ('ROSA', 'Rosa'),
        ('CIANO', 'Ciano'),
    ]
    tema_cor = models.CharField(max_length=10, choices=TEMA_CHOICES, default='AZUL')

    is_active = models.BooleanField(
        default=True, verbose_name=_('Usuário está ativo'), help_text=_('Indica que este usuário está ativo.')
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Usuário é da equipe'),
        help_text=_('Indica que este usuário pode acessar o Admin.'),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Meta options for the model."""

        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'