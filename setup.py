#!/usr/bin/env python

from setuptools import setup, find_packages

import provider

setup(
    name='django-oauth2-provider',
    version=provider.__version__,
    description='edX fork of django-oauth2-provider',
    long_description=open('README.mkd').read(),
    author='sprintly',
    author_email='ops@sprint.ly',
    url='https://github.com/sprintly/django-oauth2-provider',
    packages=find_packages(exclude=('tests*',)),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        'shortuuid>=0.4.3,<1.0.0'
    ],
    include_package_data=True,
    zip_safe=False,
)
