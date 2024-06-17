from setuptools import setup

setup(
    name='socialagent',
    version='0.1',
    description='The "socialagent" Python module enables the generation of user agents for various Meta (formerly Facebook) platform applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Moh Iqbal Hidayat',
    author_email='iqbalmh18.dev@email.com',
    url='https://github.com/iqbalmh18/socialagent',
    packages=['socialagent'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)