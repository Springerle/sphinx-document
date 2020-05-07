{{ cookiecutter.repo_name }}
=============================================================================

{{ cookiecutter.short_description }}.

.. contents:: **Contents**

:Repository:    {{ cookiecutter.repo_url }}#readme


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

    git clone "{{ cookiecutter.repo_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    tox -e docs

This will build the HTML documentation – to also open it in your browser,
just call ``tox`` without any arguments.

For this to work, you might also need to follow some `setup procedures`_
to make the necessary basic commands available on *Linux*, *Mac OS X*,
and *Windows*. On Windows, use either WSL or ‘git bash’ (MingW).

Also, the ``tox`` tool is expected on your ``PATH``, the simplest but not best way to install it is this:

.. code:: sh

    python3 -m pip install --user tox-venv

Alternatively, to get an *isolated* setup that can be easily uninstalled, use these commands:

.. code:: sh

    # Install into "~/.local/share/dephell/venvs/" and "~/.local/bin/"
    curl -L dephell.org/install | python3  # skip if you already have 'dephell'
    dephell jail install tox tox-venv

In either case, check for a successful installation by calling ``tox --version``.


Starting a Live-Reload Watchdog
-------------------------------

For a nicer user experience, you can also start a watchdog
that auto-rebuilds documentation and reloads the opened browser tab
on any change in your editor, when you save the text.

Just call ``tox -e live`` to start a new watchdog daemon
and wait for your browser to open the rendered HTML page.

To change the port of the webserver that is started in the background,
set the ``SPHINX_AUTOBUILD_PORT`` variable like this:

.. code:: sh

    export SPHINX_AUTOBUILD_PORT=8042

The default port is ``8880``.


Extension Setup Procedures
--------------------------

For some Sphinx extensions you have to set up the tools they're based upon.

sphinx.ext.graphviz
~~~~~~~~~~~~~~~~~~~

On Debian or Ubuntu Linux, install the ``graphviz`` package:

.. code:: sh

    apt install graphviz

Other distributions have similar packages, use your native package manager to install.

On macOS, use the `GraphViz Homebrew Formula`_.

On Windows, download one of the `GraphViz Windows packages`_, and add the installation
directory to the ``PATH`` after installing or unpacking.


sphinxcontrib.plantuml
~~~~~~~~~~~~~~~~~~~~~~

To install PlantUML, use these commands after you `downloaded plantuml.jar`_:

.. code:: sh

    mkdir -p ~/.local/share/java
    mv ~/Downloads/plantuml.jar $_


.. _`Sphinx document`: https://github.com/Springerle/sphinx-document#readme
.. _releases: {{ cookiecutter.repo_url }}/releases
.. _setup procedures: https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup
.. _PyInvoke: http://www.pyinvoke.org/
.. _`downloaded plantuml.jar`: https://plantuml.com/download
.. _`GraphViz Windows packages`: https://graphviz.gitlab.io/_pages/Download/Download_windows.html
.. _`GraphViz Homebrew Formula`: https://formulae.brew.sh/formula/graphviz
