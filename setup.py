from setuptools import setup

setup(
    name='sauce-demo-selenium-ui-tests',
    version='0.1',
    description='demo project for sauce labs ui tests building framework from '
                'scratch using selenium and python',
    author='ZS',
    author_email='s_zemmouri@esi.dz',
    install_requires=[
        'behave == 1.2.6',
        'robber == 1.1.5',
        'selenium == 4.6.0',
    ],
)
