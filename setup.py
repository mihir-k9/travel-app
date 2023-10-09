from setuptools import setup, find_packages

setup(
    name='travel-app',
    version='0.1',
    description='A small app where you can upload an image, and it will recommend tourist desitinations similar to the image.',
    author='Mihir Kulkarni',
    url='https://github.com/mihir-k9/travel-app/',

    packages=find_packages(),

    install_requires=[
        'time',
        'requests',
        'transformers',
        'backend',
        'torch',
        'torchaudio'
    ],
)
