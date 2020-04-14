{{ cookiecutter.repo_name }}
=============================================================================

{{ cookiecutter.short_description }}.

.. contents:: **Contents**

:Repository:    {{ cookiecutter.github_url }}#readme


Overview
--------

This is a `Sphinx document`_ that allows to write *documentation as code* and
have a copy of the text and all images in version control (git).
That means there is a full history of all changes, and collaboration by several authors
or an author and multiple reviewers is relatively easy.

The source of the main document is contained in ``index.rst``.


Contributing to this Document
-----------------------------

As a contributing author, to **create a working directory** for this document, call these commands:

.. code:: sh

    git clone "{{ cookiecutter.github_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    tox -e docs

This will build the HTML documentation – to also open it in your browser,
just call ``tox`` without any arguments.

For this to work, you might also need to follow some `setup procedures`_
to make the necessary basic commands available on *Linux*, *Mac OS X*,
and *Windows*. On Windows, use either WSL or ‘git bash’ (MingW).

Also, the ``tox`` tool is expected on your ``PATH``, the simplest way to install it is this:

.. code:: sh

    python3 -m pip install --user tox-venv

Alternatively, to get an *isolated* setup that can be easily uninstalled, use these commands:

.. code:: sh

    # Install into "~/.local/share/dephell/venvs/" and "~/.local/bin/"
    curl -L dephell.org/install | python3
    dephell jail install tox tox-venv

In either case, check for a successful installation by calling ``tox --version``.


.. not-yet

    The last command **starts a watchdog that auto-rebuilds documentation** and reloads the
    opened browser tab on any change in your editor, when you save the text.

    Call ``invoke docs -k`` to **kill the watchdog process.**


.. _`Sphinx document`: https://github.com/Springerle/sphinx-document#readme
.. _releases: {{ cookiecutter.github_url }}/releases
.. _setup procedures: https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup
.. _PyInvoke: http://www.pyinvoke.org/
