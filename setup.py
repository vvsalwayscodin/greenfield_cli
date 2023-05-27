from setuptools import setup

setup(
    name='gnfd-cmd',
    version='0.1.0',
    py_modules=['./cmd/main.py'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'gnfd-cmd = main.py:gnfd',
        ],
    },
)
