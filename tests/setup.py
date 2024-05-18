from setuptools import setup, find_packages

setup(
    name='automate-tasks',
    version='1.0.0',
    description='A Python package that automates common tasks such as file management, web scraping, and email handling.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dom557/automate-tasks',
    author='Abahazem(dom)',
    author_email='kingmohaemed@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'secure-smtplib',
        'soupsieve',
        'urllib3',
        'idna',
        'charset-normalizer',
        'certifi'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
