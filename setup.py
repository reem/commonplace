try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'My Commonplace',
    'author': 'Jonathan Reem',
    'url': 'info url',
    'download_url': 'download url',
    'author_email': 'jonathan.reem@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
