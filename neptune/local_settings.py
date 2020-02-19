SECRET_KEY = '^jtfu5uo^)e_6)e#q+s0f=)c)@f_^nuh*b1lms!_1zbi0+3wy4'

ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neptune',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
