# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neutone_sdk']

package_data = \
{'': ['*']}

install_requires = \
['SoundFile>=0.10.3,<0.11.0',
 'jsonschema>=4.4.0,<5.0.0',
 'librosa',
 'matplotlib',
 'numpy==1.22.1',
 'pytorch-lightning>=1.5.10,<2.0.0',
 'torch==1.10.2',
 'torchinfo']

setup_kwargs = {
    'name': 'neutone-sdk',
    'version': '0.1.0',
    'description': 'SDK for wrapping deep learning models for deployment in Neutone',
    'long_description': '# neutone-sdk\nSDK for wrapping deep learning models for deployment in Neutone\n',
    'author': 'Qosmo',
    'author_email': 'info@qosmo.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/QosmoInc/neutone-sdk.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

