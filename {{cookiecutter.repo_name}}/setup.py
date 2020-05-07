# fake minimal setup for Invoke

project = dict(
    name = '{{ cookiecutter.project_name }}',
    version = '{{ cookiecutter.version }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    license='{{ cookiecutter.license }}',
    packages = [],
    url='{{ cookiecutter.repo_url }}#readme',
    description='{{ cookiecutter.short_description }}',
)

if __name__ == '__main__':
    import setuptools
    setuptools.setup(**project)
