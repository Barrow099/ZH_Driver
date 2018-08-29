from setuptools import setup


setup(
    name='ZH_Driver',
    version='1.0.0',
    packages=['zh_driver'],
    url='http://barrow099.hu',
    license='Copyright (C) 2018',
    author='Barrow099',
    author_email='',
    description='Arduino ZH Driver',
    entry_points = {
              'console_scripts': [
                  'zh-driver = zh_driver:main',
              ],
          },
)
