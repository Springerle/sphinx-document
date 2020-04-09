# fake minimal setup for Invoke

project = dict(
    name = 'sphinx-document',
    version = '1.1',
    author='jhermann',
    author_email='jh@web.de',
    license='CC0',
    packages = [],
    url='https://github.com/Springerle/sphinx-document',
    description='A cookiecutter template to create standalone Sphinx documents.',
)

if __name__ == '__main__':
    import setuptools
    setuptools.setup(**project)
