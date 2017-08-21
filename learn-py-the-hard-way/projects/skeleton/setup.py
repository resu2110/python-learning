try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = [
	'description':'project name goes here',
	'author':'name of the dickhead',
	'url':'URL to get this prj'
	'download_url':'where to download?'
	'author_email':'the e-mail of the dick head'
	'version': '0.1'
	'install_requires':['nose'],
	'packages':['NAME'],
	'scripts':[],
	'name':'projectname'
]

setup(**config)
