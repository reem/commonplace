try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'My Commonplace',
    'author': 'Jonathan Reem',
    'url': 'info url',
    'download_url': 'https://github.com/reem/commonplace',
    'author_email': 'jonathan.reem@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['commonplace'],
    'scripts': ['Main'],
    'name': 'projectname'
}

setup(**config)
