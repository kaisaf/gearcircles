from django.contrib.auth import login, logout
from .models import User

from os import path

from identitytoolkit import gitkitclient


def signin_or_signup_based_on_gitkit(request):
    """
        Gitkit creates a google cookie that this function validates,
        if okay, signin or signup user on Django and return the request object
        If not able to signin, return None
    """
    gtoken_cookie = request.COOKIES.get("gtoken")
    if gtoken_cookie:
        server_config_json = path.join(
            path.dirname(path.realpath(__file__)),
            '/users/gitkit-server-config.json')
        gitkit_instance = gitkitclient.GitkitClient.FromConfigFile(server_config_json)
        gitkit_user = gitkit_instance.VerifyGitkitToken(gtoken_cookie)
        if gitkit_user:
            print("Welcome " + gitkit_user.email + "! Your user info is: " + str(vars(gitkit_user)))
            user = User.objects.filter(email=gitkit_user.email).first()
            if not user:
                user = User.objects.create_user(email=gitkit_user.email, name=gitkit_user.name)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return True
        else:
            return False
    else:
        return False
        
        