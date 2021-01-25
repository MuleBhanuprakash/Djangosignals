from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_save, post_init, post_delete
from django.core.signals import request_started, request_finished, got_request_exception


@receiver(user_logged_in, sender=User, weak=True, dispatch_uid=None)
def login_success(sender, request, user, **kwargs):
    print("log in successful........ please continue!")
    print('sender:', sender)
    print('request:', request)
    print('user:', user)
    print(f'kwargs: {kwargs}')


# user_logged_in.connect(login_success, sender=User, weak=True, dispatch_uid=None)

@receiver(user_logged_out, sender=User, weak=True, dispatch_uid=None)
def logout_success(sender, request, user, **kwargs):
    print("logged out successful........ thank you!")
    print('sender:', sender)
    print('request:', request)
    print('user:', user)
    print(f'kwargs: {kwargs}')


@receiver(user_login_failed, sender=User, weak=True, dispatch_uid=None)
def login_failed(sender, credentials, request, **kwargs):
    print("login failed! please login with correct details.")
    print('sender:', sender)
    print('credentials:', credentials)
    print('request:', request)
    print(f'kwargs: {kwargs}')


@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("this is pre save method")
    print('sender:', sender)
    print('instance:', instance)
    print(f'kwargs: {kwargs}')


@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("This is post save method")
        print('New record')
        print('sender:', sender)
        print('instance:', instance)
        print('created:', created)
        print(f'kwargs: {kwargs}')
    else:
        print("This is post save method")
        print('update')
        print('sender:', sender)
        print('instance:', instance)
        print('created:', created)
        print(f'kwargs: {kwargs}')


@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("request started")
    print("sender:", sender)
    print("environ:", environ)
    print(f'kwargs: {kwargs}')


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("request ended")
    print("sender:", sender)
    print(f'kwargs: {kwargs}')


@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    print("request interrupted due to exception")
    print("sender:", sender)
    print("request:", request)
    print(f'kwargs:{kwargs}')
