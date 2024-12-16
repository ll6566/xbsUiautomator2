from setuptools import setup, find_packages

setup(
    name='xbsUiautomator2',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'uiautomator2==2.16.25',
    ],
    author='65',
    author_email='18974710587@163.com',
    description='rewrite uiautomator2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ll6566/xbsUiautomator2',
    python_requires='>=3.0.0',
)
