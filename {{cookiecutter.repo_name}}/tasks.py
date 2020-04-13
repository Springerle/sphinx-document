# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
""" Project automation for Invoke.

    Copyright ©  {{ cookiecutter.year }} {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>
    Licensed according to the regulations of {{ cookiecutter.license }}.
"""
import os
import subprocess
import webbrowser

from invoke import *
##from rituals.easy import *  # pylint: disable=redefined-builtin

@task(help={
    'browse': "Open index page in browser tab",
})
def html(ctx, browse=False):
    """Render document and open in browser."""
    subprocess.check_call('sphinx-build -b html . target/html')

    if browse:
        index_html = os.path.abspath('target/html/index.html')
        if os.path.exists(index_html):
            webbrowser.open_new_tab(index_html)

##namespace.add_task(html)
