from flask import render_template, request, redirect, url_for, send_file
from app import app
import logging #change logging status of wekzeug

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def getNavbar(route=None):
    """
    getNavbar(route): returns a navbar dictionary useful for passing to html\n
    route : the routing of the page, used to highlight the active page
    """
    navbar=[
        {
            "link": "/academics",
            "name": "Academics",
            "active": "",
        },
        {
            "link": "/skills",
            "name": "Skills",
            "active": "",
        },
        {
            "link": "/projects",
            "name": "Projects",
            "active": "",
        },
        {
            "link": "/volunteering",
            "name": "Volunteering",
            "active": "",
        },
        {
            "link": "/rocketry",
            "name": "Rocketry",
            "active": "",
        },
        {
            "link": "/sports",
            "name": "Sports",
            "active": "",
        }, 
    ]

    if route:
        for item in navbar:
            if item["link"] in request.path:
                item["active"] = "active"
    
    return navbar


@app.route('/', methods=['GET', 'POST'])
def home():
    sites = [
        {
            "name": "File Share",
            "image": "uploader.png",
            "href": "http://upload.armstronglabs.net",
            "desc": "A from-scratch, simple to use, file transfer server",
        },
        {
            "name": "Gitea",
            "image": "gitea.png",
            "href": "http://gitea.armstronglabs.net",
            "desc": "A private, open source code repository",
        },
        {
            "name": "Shinobi",
            "image": "shinobi.png",
            "href": "http://shinobi.armstronglabs.net",
            "desc": "A network stream manager, and analysis platform",
        },
        {
            "name": "Bit Warden",
            "image": "vault.png",
            "href": "http://vault.armstronglabs.net",
            "desc": "An open source password manager",
        },        
    ]


    return render_template("main.html", navbar=getNavbar(), sites=sites)

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
