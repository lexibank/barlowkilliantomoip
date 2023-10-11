from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='lexibank_barlowkilliantomoip',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['lexibank_barlowkilliantomoip'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'lexibank.dataset': [
            'barlowkilliantomoip=lexibank_barlowkilliantomoip:Dataset',
        ]
    },
    install_requires=[
        'pylexibank>=3.4.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
