# sphinx-document

A cookiecutter template that creates
a standalone Sphinx document for specifications, architecture documentation, etc.

 ![CC0 licensed](http://img.shields.io/badge/license-CC0-red.svg)


## Features

 * :heavy_check_mark: Support for Linux, MacOS, and Windows.
 * :heavy_check_mark: Environment management and command automation using ``tox``.
 * :heavy_check_mark: Watchdog / live-reload for a frictionless authoring experience.
 * :construction: Preconfigured extensions for graphs, diagrams, and charts.


## Usage

Creating a new document is as easy as this:

```sh
cookiecutter "https://github.com/Springerle/sphinx-document"
```

You'll get asked a few questions, the project directory is created in the current working directory based on your input.
Commit the new project *unchanged* into a new git repository directly after that, before you build it or change anything – this is important to make later updates easier.

If you use this often (more than once), it makes sense to copy manifest values as requested by ``cookiecutter.json``, like your name, to the ``default_context`` of your ``~/.cookiecutterrc``. This saves a lot of typing on project creation, and reduces typos.
See the [Cookiecutter documentation](https://cookiecutter.readthedocs.io/) for details on how to use the tool.

If you don't have ``cookiecutter`` installed yet, use these commands:

```sh
# Install into "~/.local/share/dephell/venvs/" and "~/.local/bin/"
curl -L dephell.org/install | python3  # skip if you already have 'dephell'
dephell jail install cookiecutter
```

It is a quick way to get a setup that can be easily removed or updated later on.


## Related Projects

* [Diagrams as Code](https://github.com/jhermann/jhermann.github.io/wiki/Diagrams-as-Code) – Wiki page that collects tools for creating visuals that are based on textual representations.
* [Crashedmind/docdac](https://github.com/Crashedmind/docdac#readme) –  Documentation-Of-Code / Documentation-As-Code.
