# Curso Básico Django

* Crear el entorno
    ```python3 -m venv .env``` 
* Activar el entorno
    ```source .env/bin/activate```
* Desactivar el entorno
    ```deactivate```

* Crear proyecto
    ``` django-admin startproject platzigram . ```

* Correr servidor
    ```python3 manage.py runserver```

* Importar y ejecutar debugger
    ```import pdb; pdb.set_trace()```

    * Headers: ```request.META```
    * Metodo: ```request.method```
    * Continuar ejecución: ```c```
    * Imprimir GET: ```request.GET['numbers']```
        * ```localhost:8000/hi/?numbers=10,2,4,50```
* Retornar JSON:
    * ```python
        from django.http import HttpResponse
        import json

        data = {
            'status': 'ok',
            'numbers': [1,2,3],
            'message': 'Cool!',
        }
        return HttpResponse(json.dumps(data, indent=4)  content_type='application/json')
        ```
* Datos desde una URL
    ```python
    # url.py

    path('hi/<str:name>/<int:age>', views.say_hi),

    # views.py

    def say_hi(request, name, age):
        return HttpResponse('Hi {} you have {} years old'.forma(name, age))

    # URL
    http://127.0.0.1:8000/hi/nildiert/27
    ```
* Crear app
    ``` python
    # Crear app
    python3 manage.py startapp name_app

    # settings.py

    INSTALLED_APPS = [
        ...

        'name_app'
    ]

    # urls.py
    from name_app import views as posts_views

    path('name_app/', posts_views.name_function)

    # posts.views.py

    def name_function:
        pass

    ```
* Crear html desde el back
    ```python
    posts = [
    {
        'name': 'Mont Black',
        'user': 'Yessica',
        'timestamp': datetime.now(),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Bogota',
        'user': 'Nildiert',
        'timestamp': datetime.now(),
        'picture': 'https://picsum.photos/200/200/?image=1037',
    },
    {
        'name': 'Otro',
        'user': 'Gilberto',
        'timestamp': datetime.now(),
        'picture': 'https://picsum.photos/200/200/?image=1038',
    },
    ]


    def list_posts(request):
    content = []
    for post in posts:
        content.append("""
                       <p><strong>{name}</strong></p>
                       <p><small>{user} - <i>{timestamp}</i></small></p>
                       <figure><img src="{picture}"></figure>
                       """.format(**post))
    return HttpResponse('<br>'.join(content))
    ```
* Render template
    ```python
    # views.py
    from django.shortcuts import render

    posts = [
        {
            'title': 'Mont Blanc',
            'user': {
                'name': 'Yésica Cortés',
                'picture': 'https://picsum.photos/60/60/?image=1027'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/800/600?image=1036',
        },
        {
            'title': 'Via Láctea',
            'user': {
                'name': 'Christian Van der Henst',
                'picture': 'https://picsum.photos/60/60/?image=1005'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/800/800/?image=903',
        },
        {
            'title': 'Nuevo auditorio',
            'user': {
                'name': 'Uriel (thespianartist)',
                'picture': 'https://picsum.photos/60/60/?image=883'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/500/700/?image=1076',
        }
    ]

    def list_posts(request):
        return render(request, 'feed.html', {'posts': posts})

    # feed.html

    {% for post in posts %}
        <div class="col-lg-4 offset-lg-4">
            <div class="media">
                <img src="{{ post.user.picture }}" alt="{{ post.user.name }}" class="mr-3 rounded-circle">
                <div class="media-body">
                    <h5 class="mt-0">{{ post.user.name }}</h5> 
                    {{ post.timestamp }}
                </div>
            </div>
            <img src="{{ post.photo }}" alt="{{ post.title }}" class="img-fluid mt-3 border rounder">
            <h6 class="ml-1 mt-1">{{ post.title }}</h6>
        </div>
    {% endfor %}
    ```

## ORM 

* Migraciones
    ```shell
    python3 manage.py migrate
    ```
* Crear modelo
    ```python
    # models.py

    from django.db import models


    class User(models.Model):

        email = models.EmailField(unique=True)
        password = models.CharField(max_length=100)

        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)

        bio = models.CharField(blank=True, max_length=100)

        birthdate = models.DateTimeField(blank=True, null=True)
    
        created = models.DateTimeField(auto_now_add=True)
        modified = models.DateTimeField(auto_now=True)
    
    
    ```

* Realizar cambios en las migraciones
    ```bash
    python3 manage.py makemigrations
    ```

* Cargar shell Django y agregar datos
    ```bash
    python3 manage.py shell
    ```

    ```shell
    (InteractiveConsole)
    >>> from posts.models import User
    >>> pablo = User.objects.create(
    ...     email='hola@gmail.com',
    ...     password='1234567',
    ...     first_name='Pablo',
    ...     last_name='Trinidad'
    ... )
    >>> pablo.email
    'hola@gmail.com'
    >>> pablo.pk
    1
    >>> pablo.email = 'pablo@gmail.com'
    >>> pablo.save()
    >>> pablo.created
    datetime.datetime(2020, 6, 9, 7, 42, 18, 32304, tzinfo=<UTC>)
    >>> pablo.modified
    datetime.datetime(2020, 6, 9, 7, 44, 49, 551718, tzinfo=<UTC>)
    >>> 

    ```
* Otra forma de agregar datos
    ```shell
    >>> arturo = User()
    >>> arturo.pk
    >>> arturo.email = 'arturo@platzi.com'
    >>> arturo.first_name = 'Arturo'
    >>> arturo.last_name = 'Martínez'
    >>> arturo.password = 'MSIComputer'
    >>> arturo.is_admin = True
    >>> arturo.save()

    # Borrar datos
    >>> arturo.delete()
    (1, {'posts.User': 1})

    ```

* Agregar varios datos
    ```python

    from datetime import date

    users = [
        {
            'email': 'cvander@platzi.com',
            'first_name': 'Christian',
            'last_name': 'Van der Henst',
            'password': '1234567',
            'is_admin': True
        },
        {
            'email': 'freddier@platzi.com',
            'first_name': 'Freddy',
            'last_name': 'Vega',
            'password': '987654321'
        },
        {
            'email': 'yesica@platzi.com',
            'first_name': 'Yésica',
            'last_name': 'Cortés',
            'password': 'qwerty',
            'birthdate': date(1990, 12,19)
        },
        {
            'email': 'arturo@platzi.com',
            'first_name': 'Arturo',
            'last_name': 'Martínez',
            'password': 'msicomputer',
            'is_admin': True,
            'birthdate': date(1981, 11, 6),
            'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        }
    ]

    from posts.models import User

    for user in users:
        obj = User(**user)
        obj.save()
        print(obj.pk)
    ```
    ```shell
    >>> from posts.models import User
    >>> user = User.objects.get(email='freddier@platzi.com')
    >>> user
    <User: User object (4)>
    >>> type(user)
    <class 'posts.models.User'>
    >>> user.pk
    4
    >>> user.first_name
    'Freddy'
    >>> user.password
    '987654321'

    # Traer todos los usuarios de platzi
    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com')
    >>> platzi_users
    <QuerySet [<User: User object (3)>, <User: User object (4)>, <User: User object (5)>, <User: User object (6)>]>

    ```
*  *Para retornar el string en vez del id*

    ```python
    

    # models.py
    # Agregamos el metodo

    def __str__(self):
        return self.email
    ```

    ```shell
    >>> from posts.models import User
    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com')
    >>> platzi_users
    <QuerySet [<User: cvander@platzi.com>, <User: freddier@platzi.com>, <User: yesica@platzi.com>, <User: arturo@platzi.com>]>
    ```
* Traer todos los usuarios
    ```shell
    >>> users = User.objects.all()
    >>> users
    <QuerySet [<User: pablo@gmail.com>, <User: cvander@platzi.com>, <User: freddier@platzi.com>, <User: yesica@platzi.com>, <User: arturo@platzi.com>]>
    ```
* Actualizar todos unos valores pedidos
    ```shell
    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com')
    >>> for u in platzi_users:
    ...    print(u.email, ':', u.is_admin)
    ...
    cvander@platzi.com : True
    freddier@platzi.com : False
    yesica@platzi.com : False
    arturo@platzi.com : True

    # Aquí actualizamos datos
    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com').update(is_admin=True)

    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com')
    >>> for u in platzi_users:
    ...     print(u.email, ':', u.is_admin)
    ... 
    cvander@platzi.com : True
    freddier@platzi.com : True
    yesica@platzi.com : True
    arturo@platzi.com : True
    ```

    [Django Queries](https://docs.djangoproject.com/en/3.0/topics/db/queries/)

* Crear usuario
    ```shell
    python3 manage.py shell
    ```
    ```shell
    >>> from django.contrib.auth.models import User
    >>> u = User.objects.create_user(username='yesika', password='admin123')
    >>> u
    <User: yesika>
    >>> u.pk
    1
    >>> u.username
    'yesika'
    >>> u.password
    'pbkdf2_sha256$180000$OEKjaHZCpDQi$FkyLQnFevfqc3VOD+ehBkWKhy9ZhUQa7NTW7ffH2DEk='
    >>> 

* Crear super usuario
    ```shell
    (.env) ➜  Platzi-gram python3 manage.py createsuperuser 

    Username (leave blank to use 'mrbizarro'): pablo
    Email address: p@gmail.com
    Password: 
    Password (again): 
    Superuser created successfully.

    ```
    * Registrar url admin
        ```python
        # urls.py
        from django.contrib import admin

        urlpatters = [
            path('admin/', admin.site.urls)
        ]

        ```
* Extender el modelo de Usuario (Relacionar Usuario con otra tabla)
[Documentación](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#extending-the-existing-user-model)


    * Crear nueva aplicación

        ```shell
        python3 manage.py startapp users
        ```

        ```python
        # users/apps.py

        class UsersConfig(AppConfig):
            name = 'users'
            verbose_name = 'Users'
        ```

        [Django Field Reference](https://docs.djangoproject.com/en/3.0/ref/models/fields/#onetoonefield)

        ```python
        # users/models.py
        from django.contrib.auth.models import User

        class Profile(models.Model):
            user = models.OneToOneField(User, on_delete=models.CASCADE)
    
            website = models.URLField(max_length=200, blank=True)
            biography = models.TextField(blank=True)
            phone_number = models.CharField(max_length=20, blank=True)
    
            picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    
            created = models.DateTimeField(auto_now_add=True)
            modified = models.DateTimeField(auto_now=True)
    
            def __str__(self):
                return self.user.username
        ```
        ```python
        # settings.py


        INSTALLED_APPS = [
            # DJango apps
            ...
            'users',
        ]
        ```

        ```bash

        # Si vas a guardar imagenes o archivos
        pip3 install pillow

        python3 manage.py makemigrations
        python3 manage.py migrate
        ```

        ```bash
        # Creamos super usuario

        python3 manage.py createsuperuser

        Username (leave blank to use 'mrbizarro'): nildiert
        Email address: n@gmail.com
        Password: 
        Password (again): 

        Superuser created successfully.
        ```

        Vamos a la url

        ```shell
        http://127.0.0.1:8000/admin/
        ```

    * Registrar el modelo

        ```python
        # users/admin.py

        from django.contrib import admin
        from users.models import Profile

        admin.site.register(Profile)
        ```
        ... Ahora puedo ir a esta url
        
        ```shell
        http://127.0.0.1:8000/admin/users/profile/
        ```

        También se puede registrar el modelo con decoradores:

        ```python
        from django.contrib import admin
        from users.models import Profile

        @admin.register(Profile)
        class ProfileAdmin(admin.ModelAdmin):

            # Esta linea muestra estos elementos en /admin
            list_display = ('user', 'phone_number', 'website', 'picture')

            # Convierte en links a /detail cada elemento
            list_display_links = ('pk', 'user',)

            # Crea un input editable para cada valor
            list_editable = ('phone_number', 'website', 'picture')

            search_fields = (
                'user__email',
                'user__username',
                'user__first_name', 
                'user__last_name',
                'phone_number'
            )

            # Añade filtros a la derecha
            list_filter = (
                'created', 
                'modified',
                'user__is_active',
                'user__is_staff'
            )
            
            # Agrupa los campos del formulario

    
            fieldsets = (
                # Primer elemento es la categoria
                ('Profile', {
                    'fields': (
                        ('user', 'picture'),),

                }),
                ('Extra info', {
                    'fields': (
                        ('website', 'phone_number'),
                        ('biography',)
                    )
                }),
                ('Metadata', {
                    'fields': (
                        ('created', 'modified')
                    )
                })
            )   
            
            readonly_fields = ('created', 'modified')         

        ```
        [Fieldsets documentación](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets)

        ```
        # Para este error, 
        FieldError at /admin/users/profile/2/change/
        'created' cannot be specified for Profile model form as it is a non-editable field. Check fields/fieldsets/exclude attributes of class ProfileAdmin.


        readonly_fields = ('created', 'modified')
        ```
    * Agregar el Profile al admin

        [StackedInline](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.StackedInline)

        ```python
        # admin.py

        from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
        from django.contrib.auth.models import User

        class ProfileInline(admin.StackedInline):
    
            model = Profile
            can_delete = False
            verbose_name = 'profiles'
    
        class UserAdmin(BaseUserAdmin):
            inlines = (ProfileInline,)

            # Listamos los campos que se van a ver
            list_display = (
               'username',
               'email',
               'first_name',
               'last_name',
               'is_active',
               'is_staff'
            )
    
        admin.site.unregister(User)
        admin.site.register(User, UserAdmin)
        ```
* Relaciones

    **[Relationship fields](https://docs.djangoproject.com/en/3.0/ref/models/fields/#module-django.db.models.fields.related)**

    * Crear modelo ```Posts```


        ```python

        from django.db import models
        from django.contrib.auth.models import User

        class Post(models.Model):
    
            user = models.ForeignKey(User, on_delete=models.CASCADE)
    
            profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

            ...
        ```

        ```shell
        python3 manage.py makemigrations 
        python3 manage.py migrate
        ```
    * Visualizar imagenes

        [MEDIA_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_ROOT)

        ```python
        # urls.py
        from django.conf.urls.static import static
        from django.conf import settings

        urlpatterns = [
            ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        

        ```

        ```python

        # settings.py
        
        ...
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        MEDIA_URL = '/media/'
        ```

* Crear templates
    ```python
    # settings.py
    TEMPLATES = [
        {'DIRS': [os.path.join(BASE_DIR, 'templates')]}
    ]
    ```

    En el directorio base creo la carpeta ```templates``` y dentro los templates de cada aplicación

    * Agregamos carpeta ```static``` en la raiz y configuramos en ```settings.py```

    [STATICFILES_FINDERS](https://docs.djangoproject.com/en/3.0/ref/settings/#staticfiles-finders)

    ```python
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]
    ```
* Sistema de autenticación
    ### login
    [Authentication in Web requests](https://docs.djangoproject.com/en/3.0/topics/auth/default/#authentication-in-web-requests)
   

    ```python
    # urls.py

    from users import views as users_views
    urlpatterns = [
    ...
    path('users/login/', users_views.login_view, name='login'),
    ] 
    ```

    ```python
    # users/views.py
    from django.contrib.auth import authenticate, login
    from django.shortcuts import render, redirect

    def login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
        
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('feed')
            else:
                return render(request, 'users/login.html', {'error': 'Invalid username and password'})
        return render(request, 'users/login.html')
    ```

    ```html
    <!-- users/login.html -->

    {% extends "users/base.html" %}


        {% block head_content %}
        <title>Platzigram sign in</title>
        {% endblock %}

        {% block container %}
            {% if error %}
                <p style="color: red">{{ error }}</p>
            {% endif %}
            <form method="POST" action="{% url "login" %}">
                {% csrf_token %}
                <input type="text" placeholder="Username" name="username">
                <input type="password" placeholder="Password" name="password">
                <button type="submit">Sign in</button>
            </form>
        {% endblock %}
    ```
* Redirigir si no esta logueado
     [The login_required decorator](https://docs.djangoproject.com/en/3.0/topics/auth/default/#the-login-required-decorator)
     ```python
     # settings.py
     ...
     LOGIN_URL = '/users/login/'
     ```

     ```python
     # posts/views.py
     from django.contrib.auth.decorators import login_required

    @login_required
    def list_posts(request):
        ...

     ```
    ### logout

    [How to log a user out](https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-out)
    ```python
    # urls.py
    path('users/logout/', users_views.logout_view, name='logout'),
    ```

    ```python
    # users/views.py
    from django.contrib.auth import authenticate, login, logout
    from django.contrib.auth.decorators import login_required
    ...
    @login_required
    def logout_view(request):
        logout(request)
        return redirect('login')
    ```
    ```html
    <!-- templates/nav.html -->
    <li class="nav-item nav-icon">
        <a href="{% url "logout" %}">
        <i class="fas fa-sign-out-alt"></i>
        </a>
    </li>
    ```
    ### signup
    [Creating users](https://docs.djangoproject.com/en/3.0/topics/auth/default/#creating-users)

    ```python
    # urls.py
    path('users/signup/', users_views.signup, name='signup'),
    ```

    ```python
    # users/views.py
    from django.contrib.auth.models import User
    from users.models import Profile
    ```

    ```python
    # users/views.py
    from django.db.utils import IntegrityError
    from django.contrib.auth.models import User
    from users.models import Profile

    def signup(request):

        if request.method == 'POST':
            username = request.POST['username']
            passwd = request.POST['passwd']
            passwd_confirmation = request.POST['passwd_confirmation']
        
            if passwd != passwd_confirmation:
                return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
            try:
                user = User.objects.create_user(username=username, password=passwd)
            except IntegrityError:
                return render(request, 'users/signup.html', {'error': 'Username is already in use'})
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
        
            profile = Profile(user=user)
            profile.save()
        
            return redirect('login')
        
        return render(request, 'users/signup.html')    

    ```
    ```html
    {% extends "users/base.html" %}


    {% block head_content %}
        <title>Platzigram sign up</title>
    {% endblock %}

    {% block container %}

        {% if error %}
            <p class="alert alert-danger">
            {{ error }}
            </p>
        {% endif %}

        <form action="{% url 'signup' %}" method="POST">
            {% csrf_token %}

            <div class="form-group">
                <input type="text" class="form-control" placeholder="Username" name="username" required="true">
            </div>

            <div class="form-group">
                <input type="password" class="form-control" placeholder="Password" name="passwd" required="true">
            </div>

            <div class="form-group">
                <input type="password" class="form-control" placeholder="Password confirmation" name="passwd_confirmation" required="true">
            </div>

            <div class="form-group">
                <input type="text" class="form-control" placeholder="First name" name="first_name" required="true">
            </div>

            <div class="form-group">
                <input type="text" class="form-control" placeholder="Last name" name="last_name" required="true">
            </div>

            <div class="form-group">
                <input type="text" class="form-control" placeholder="Email address" name="email" required="true">
            </div>        

            <button class="btn btn-primary btn-block mt-5">Register</button>
        </form>
    {% endblock %}    
    ```
* Middleware

    [Documentación](https://docs.djangoproject.com/en/3.0/topics/http/middleware/#middleware)

    ```python
    # urls.py
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
    ```
    ```python
    # users/views.py
    def update_profile(request):
        return render(request, 'users/update_profile.html')
    ```

    ```html
    # templates/users/update_profile.html
    df 
    ssdf
    ```

    ```python
    # platzigram/middleware.py

    from django.shortcuts import redirect

    class ProfileCompletionMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call_(self, request):
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                return redirect('update_profile')
            
        response = self.get_response(request)
        return response    
    ```

    ```python
    # platzigram/settings.py
    MIDDLEWARE = [
        ...
        'platzigram.middleware.ProfileCompletionMiddleware'
    ]

    ```
        




