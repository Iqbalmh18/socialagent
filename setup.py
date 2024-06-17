from setuptools import setup

setup(
    name='socialagent',
    version='0.1',
    description='socialagent is a Python module designed for generating user agents specific to social media platforms under Meta (formerly Facebook).',
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
    python_requires='>=3.8',
)
