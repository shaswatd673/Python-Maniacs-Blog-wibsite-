from django.apps import AppConfig

#BlogConfig inherits from Appconfig 
#We will copy this BlogConfig to the INSTALLED_APPS setting
#in the setting.py file in project directory
class BlogConfig(AppConfig):
    name = 'blog'
