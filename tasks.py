# pylint: disable=wildcard-import, unused-wildcard-import, bad-continuation
# pylint: disable=superfluous-parens, redefined-builtin, unused-import
""" Project automation for Invoke.
"""
# CC0 1.0 Universal / No rights reserved.
#
# For more information, please see the included LICENSE file or
# <http://creativecommons.org/publicdomain/zero/1.0/>

import os
import sys
import shlex
import shutil
from contextlib import contextmanager

from invoke import *
#from rituals.easy import task, Collection, pushd
#from rituals.util import antglob, notify
#from rituals.acts.documentation import namespace as _docs


@contextmanager
def pushd(path):
    """ A context that enters a given directory and restores the old state on exit.

        The original directory is returned as the context variable.
    """
    saved = os.getcwd()
    os.chdir(path)
    try:
        yield saved
    finally:
        os.chdir(saved)


@task
def test(ctx):
    """Perform integration tests."""
    ctx.run("rm -rf new-document ; cookiecutter --no-input .")
    with pushd('new-document'):
        assert os.path.exists('index.rst'), "document index is missing!"
        ctx.run("tox -e docs")
        assert os.path.exists('build/_html/index.html'), "HTML index is missing!"
