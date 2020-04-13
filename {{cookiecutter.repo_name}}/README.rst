{{ cookiecutter.repo_name }}
=============================================================================

{{ cookiecutter.short_description }}.

.. contents:: **Contents**

:Repository:    {{ cookiecutter.github_url }}#readme


Overview
--------

This is a `Sphinx document`_ that allows to write *documentation as code* and
have a copy of the text and all images in version control (git),
meaning there is a full history of all changes, and collaboration by several authors
or an author and multiple reviewers is relatively easy.

The source of the main document can be found in ``index.rst``.


Contributing to This Document
-----------------------------

As a contributing author, to **create a working directory** for this project, call these commands:

.. code:: sh

    git clone "{{ cookiecutter.github_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    command . .env --yes
    invoke docs -bw

For this to work, you might also need to follow some `setup procedures`_
to make the necessary basic commands available on *Linux*, *Mac OS X*,
and *Windows*.

The last command **starts a watchdog that auto-rebuilds documentation** and reloads the
opened browser tab on any change in your editor, when you save the text.

Call ``invoke docs -k`` to **kill the watchdog process.**


.. _`Sphinx document`: https://github.com/Springerle/sphinx-document#readme
.. _releases: {{ cookiecutter.github_url }}/releases
.. _setup procedures: https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup
.. _PyInvoke: http://www.pyinvoke.org/
