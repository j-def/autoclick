from django.shortcuts import render, HttpResponse
from django.http import StreamingHttpResponse
import requests
import time
import socket
import gunicorn

# Create your views here.

def discordlogin(request):
    if request.method == "GET":
        code = request.GET["code"]
        valid = False

        DISCORD_API = "https://discordapp.com/api"
        CLIENT_ID = '708208719720218707'
        CLIENT_SECRET = 'c1e8ZZhPKgSRz31SwqIo37BwFLCsM1jI'
        REDIRECT_URI = 'http://kuaiaio.link/login'

        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'scope': 'guilds'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post('%s/oauth2/token' % DISCORD_API, data=data, headers=headers)
        json = r.json()


        access_token = json["access_token"]

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        r = requests.get("%s/users/@me" % DISCORD_API, headers=headers)
        json = r.json()
        user = json["id"]
        print(user)

        r = requests.get("%s/users/@me/guilds" % DISCORD_API, headers=headers)
        json = r.json()
        for guild in json:
            guildid = guild["id"]
            if guildid == "704874046864752701":
                valid = True

        if valid == True:
            request.session['username'] = user
            return render(request, "redirect-home.html")
        if valid == False:
            return render(request, "invalid-user.html")

def connected(request):
    return render(request, "redirect-home-connected.html")

def discordtest(request):
    try:
        user = request.session['username']
    except:
        user = "N/A"
    return HttpResponse(user)

def logout(request):
    try:
        del request.session['username']
        return HttpResponse("Logged out")
    except:
        return HttpResponse("Error Logging out. Likely not logged in")

def rddd(request):
    return render(request, "rddd.html")

def rdd(request):
    if request.method == "GET":
        pw = request.GET["pw"]
        if pw == "fnsvv78V7v78fefg9fuhgfsdfsdf343as1e345dfsfcvx8r":
            import os
            os.rename("templates/homepage.html","templates/homepages.html")
            return HttpResponse("Correct PW")
        else:
            return HttpResponse("Incorrect PW")

def home(request):
    try:
        user = request.session['username']
        try:
            keywords = request.session["keywords"]
        except:
            keywords = ""
        return render(request, "homepage.html", {"keywords":keywords})
    except:
        return render(request, "redirect-login.html")
