from setuptools import find_packages, setup
with open('VERSION') as fh:
    version = fh.readline()

setup(
    name='sub_entity_analysis',
    packages = find_packages('src'),
    package_dir={"":"src"},
    version=version,
    description='Api to generate times series with GeosysPy and compare them between each other ',
    author='EarthDaily Agro',
)
