try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = [
	'description':'automated testing example',
	'author':'Minh Dinh',
	'url':'URL to get this prj'
	'download_url':'where to download?'
	'author_email':'the e-mail of the dick head'
	'version': '0.1'
	'install_requires':['nose'],
	'packages':['ex47'],
	'scripts':[],
	'name':'automate testing example'
]

setup(**config)
