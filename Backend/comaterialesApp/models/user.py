from django.db import models # VAMOS A HEREDAR DE ESTA LIB MODELS
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager # PERMISOS Y ADMINISTRACION DEL MODELO
from django.contrib.auth.hashers import make_password #LIBRERI PARA CODIFICAR LA PASSWORD
#ESTAS IMPORTACIONS SON NECESARIAS PARA LA CREACION DEL MODELO USUARIO, SON PROPIAS DE DJANGO


class UserManager(BaseUserManager): # CLASE MANAGER QUE HEREDA DE BaseUserManager
    def create_user(self,email, username, password=None,bandera = False):#METODO PARA CREAR UN USUARIO
        #Creates and saves a user with the given username and password.
        if not email:
            raise ValueError('Users must have an email')
        email= self.normalize_email(email)
        user = self.model(email=email,username = username)
        user.set_password(password)
        if(bandera==True):
            return user
        else:
            user.save(using=self._db)
            return user
    
    def create_superuser(self,email, username, password): # esto solo crea un admin 
    
        user = self.create_user(email=email,username=username,password=password,bandera=True)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin): #CLASE QUE HEREDA DE DOS CLASES
    # SE CREA EL MODELO DE EL USUARIO QUE IRÁ A BASE DE DATOS
    id = models.BigAutoField(primary_key=True) # ID LLAVE PRIMARIA
    username = models.CharField('Username', max_length = 15, unique=True) #NOMBRE DE USUARIO
    password = models.CharField('Password', max_length = 256) # contraseña dada por usuario
    type_document = models.CharField('typeDocument', max_length = 30,default='Cédula') # TIPO DE DOCUMENTO
    document = models.CharField('Document', max_length = 30, default='') # Numero del documento
    name = models.CharField('Name', max_length = 30) # NOMBRE DEL USUARIO
    email = models.EmailField('Email', max_length = 100,unique=True) # email del usuario
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def save(self, **kwargs):
        if(self.is_staff == False):
            some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
            self.password = make_password(self.password, some_salt)
        super().save(**kwargs)