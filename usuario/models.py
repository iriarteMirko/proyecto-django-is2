from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, apellidos, password=None, usuario_estudiante=False, usuario_profesor=False):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico.')
        if not nombre:
            raise ValueError('El usuario debe tener un nombre.')
        if not apellidos:
            raise ValueError('El usuario debe tener apellidos.')
        
        user = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellidos=apellidos,
            usuario_estudiante=usuario_estudiante,
            usuario_profesor=usuario_profesor
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nombre, apellidos, password):
        user = self.create_user(
            email=email,
            nombre=nombre,
            apellidos=apellidos,
            password=password
        )
        user.usuario_administrador = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    email = models.EmailField('Correo electrónico', max_length=100, unique=True)
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=100)
    usuario_activo = models.BooleanField('Usuario activo', default=True)
    usuario_estudiante = models.BooleanField('Usuario estudiante', default=False)
    usuario_profesor = models.BooleanField('Usuario profesor', default=False)
    usuario_administrador = models.BooleanField('Usuario administrador', default=False)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellidos']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.usuario_administrador
    
    def has_module_perms(self, app_label):
        return self.usuario_administrador
    
    @property
    def is_active(self):
        return self.usuario_activo
    
    @property
    def is_student(self):
        return self.usuario_estudiante
    
    @property
    def is_teacher(self):
        return self.usuario_profesor
    
    @property
    def is_staff(self):
        return self.usuario_administrador