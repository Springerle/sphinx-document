{{ cookiecutter.repo_name }}
=============================================================================

{{ cookiecutter.short_description }}.

.. contents:: **Contents**

:Repository:    {{ cookiecutter.github_url }}#readme


Overview
--------

**TODO**


Contributing
------------

As a controbuting author, to **create a working directory** for this project, call these commands:

.. code:: sh

    git clone "{{ cookiecutter.github_url }}.git"
    cd "{{ cookiecutter.repo_name }}"
    command . .env --yes
    invoke docs -bw

For this to work, you might also need to follow some `setup procedures`_
to make the necessary basic commands available on *Linux*, *Mac OS X*,
and *Windows*.

The last command **starts a watchdog that auto-rebuilds documentation** and reloads the
opened browser tab on any change.
Call ``invoke docs -k`` to kill the watchdog process.


References
----------

**Tools**

-  `PyInvoke`_


Acknowledgements
----------------

…

.. _releases: {{ cookiecutter.github_url }}/releases
.. _setup procedures: https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup
.. _PyInvoke: http://www.pyinvoke.org/
