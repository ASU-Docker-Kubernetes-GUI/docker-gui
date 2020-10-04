from flask import Blueprint

"""
app_router renders all of the frontend materials for this application.
Routes that are included are:
- / -                 renders the default homepage
- /create-container - renders the create container form
- /settings -         renders the settings page
- /images -           renders the images page

All of these methods will call their appropriate handler method
In the handlers directories
"""

client_router = Blueprint('app_router', __name__)


@client_router.route('/')
def render_homepage():
    return "rendering homepage"


@client_router.route('/create-container')
def render_create_container():
    return "create-container page"


@client_router.route('/settings')
def render_settings_page():
    return "rendering settings page"


@client_router.route('/images')
def render_images_page():
    return "rendering images page"

