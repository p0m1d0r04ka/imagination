from setuptools import setup, find_packages
from os.path import join, dirname

DESCRIPTION = 'Спаммер для ВК'
LONG_DESC = DESCRIPTION

setup(
    name='vk-spammer',
    version='1.2.2.3',
    author='p0m1d0r41k',
    author_email='forse373@gmail.com',
    url='https://github.com/p0m1d0r04ka/imagination',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    long_description=LONG_DESC,
    entry_points={
        'console_scripts':
            ['vk-spammer=core.spam:main']
    },
    install_requires=[
        'vk'
    ]
)
