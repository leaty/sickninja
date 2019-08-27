from setuptools import setup, find_packages

with open('README.md') as f:
	readme = f.read()

with open('LICENSE') as f:
	license = f.read()

setup(
	name='sickninja',
	use_scm_version=True,
	setup_requires=['setuptools_scm'],
	description='Stylesheet generator that uses sass and jinja2',
	long_description=readme,
	author='leaty',
	author_email='dev@leaty.net',
	url='https://github.com/leaty/sickninja',
	license=license,
	packages=find_packages(),
	scripts=['bin/sickninja']
	#entry_points = {
	#	'console_scripts': ['sickninja=sickninja.__main__:main']
	#}
)
