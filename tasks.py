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
import subprocess
from pathlib import Path
from contextlib import contextmanager

from invoke import *
#from rituals.easy import task, Collection, pushd
#from rituals.util import antglob, notify
#from rituals.acts.documentation import namespace as _docs


SPHINX_AUTOBUILD_PORT = os.environ.get("SPHINX_AUTOBUILD_PORT", "8880")


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
    subprocess.check_call(["bash", "-c", "fuser -uk " + SPHINX_AUTOBUILD_PORT + "/tcp 2>/dev/null"
	" || kill $(ps auxwww | egrep sphinx[-]autobuild | awk '{print $1;}') 2>/dev/null"
	" || :"])
    Path("new-document").exists() and shutil.rmtree("new-document")
    subprocess.check_call([sys.executable, "-m", "cookiecutter", "--no-input", "."])
    with pushd('new-document'):
        assert os.path.exists('index.rst'), "document index is missing!"
        subprocess.check_call([sys.executable, "-m", "tox", "-e", "docs"])
        assert os.path.exists('build/_html/index.html'), "HTML index is missing!"
