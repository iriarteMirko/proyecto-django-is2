from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError

class UsuarioManager(BaseUserManager):
    def create_user(self, codigo, email, nombre, apellidos, password=None, es_estudiante=False, es_profesor=False):
        if not codigo:
            raise ValueError('El usuario debe tener un código.')
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico.')
        if not nombre:
            raise ValueError('El usuario debe tener un nombre.')
        if not apellidos:
            raise ValueError('El usuario debe tener apellidos.')
        
        user = self.model(
            codigo=codigo,
            email=self.normalize_email(email),
            nombre=nombre,
            apellidos=apellidos,
            es_estudiante=es_estudiante,
            es_profesor=es_profesor
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, codigo, email, nombre, apellidos, password=None):
        user = self.create_user(
            codigo=codigo,
            email=self.normalize_email(email),
            nombre=nombre,
            apellidos=apellidos,
            password=password
        )   
        user.es_administrador = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    codigo = models.CharField('Código', max_length=8, unique=True)
    email = models.EmailField('Correo electrónico', max_length=25, unique=True)
    nombre = models.CharField('Nombre', max_length=20)
    apellidos = models.CharField('Apellidos', max_length=20)
    imagen = models.ImageField('Imagen', upload_to='usuarios/', default='usuarios/default-avatar.jpg')
    activo = models.BooleanField('Activo', default=True)
    es_estudiante = models.BooleanField('Estudiante', default=False)
    es_profesor = models.BooleanField('Profesor', default=False)
    es_administrador = models.BooleanField('Administrador', default=False)
    slug = models.SlugField(max_length=100, unique=False, blank=True)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'codigo'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellidos']
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.codigo
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.nombre} {self.apellidos}')
        super(Usuario, self).save(*args, **kwargs)
    
    def clean(self):
        if self.es_estudiante and self.es_profesor:
            raise ValidationError('Un usuario no puede ser estudiante y profesor al mismo tiempo.')
    
    def has_perm(self, perm, obj=None):
        return self.es_administrador
    
    def has_module_perms(self, app_label):
        return self.es_administrador
    
    @property
    def is_active(self):
        return self.activo
    
    @property
    def is_student(self):
        return self.es_estudiante
    
    @property
    def is_teacher(self):
        return self.es_profesor
    
    @property
    def is_staff(self):
        return self.es_administrador