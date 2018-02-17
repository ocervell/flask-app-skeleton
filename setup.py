from setuptools import setup

setup(
    name='flask-app-boostrap',
    version='0.1',
    py_modules=['flaskb'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        flaskb=flaskb:cli
    ''',
)
