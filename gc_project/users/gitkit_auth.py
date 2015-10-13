from django.contrib.auth import login, logout
from .models import User

from os import path

from identitytoolkit import gitkitclient


def create_gitkit_instance():
    server_config_json = path.join(
        path.dirname(path.realpath(__file__)),
        'gitkit-server-config.json')
    return gitkitclient.GitkitClient.FromConfigFile(server_config_json)


def signin_or_signup_based_on_gitkit(request):
    """
        Gitkit creates a google cookie that this function validates,
        if okay, signin or signup user on Django and return the request object
        If not able to signin, return None
    """
    gtoken_cookie = request.COOKIES.get("gtoken")
    if gtoken_cookie:
        gitkit_instance = create_gitkit_instance()
        gitkit_user = gitkit_instance.VerifyGitkitToken(gtoken_cookie)
        if gitkit_user:
            #print("Welcome " + gitkit_user.email + "! Your user info is: " + str(vars(gitkit_user)))
            user = User.objects.filter(email=gitkit_user.email).first()
            if not user:
                user = User.objects.create_user(email=gitkit_user.email)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return True
        else:
            return False
    else:
        return False
