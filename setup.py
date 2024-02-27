import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setuptools.setup(
    name='scatspectra',
    version='1.1.1',
    author='Rudy Morel',
    author_email='rmorel@flatironinstitute.org',
    description=
    'Analysis and generation of time-series with Scattering Spectra',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/RudyMorel/scattering_spectra',
    package_data={'': ['*.csv']},
    license='MIT',
    install_requires=reqs,
    packages=setuptools.find_packages())
