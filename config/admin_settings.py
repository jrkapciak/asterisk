import os

from django.contrib import admin

env = os.environ.get("ENVIRONMENT")
version = os.environ.get("GITHUB_SHA", "")
admin.site.site_header = f"Site - {env.upper()} | {version}"
admin.site.site_title = env
admin.autodiscover()
