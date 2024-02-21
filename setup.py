from setuptools import setup, find_packages

setup(
    name='PyPixDirectSDK',
    version='0.0.1a',
    packages=find_packages(),
    package_data={'PyPix': ['PyPix/*.m']},

    install_requires=[
        # List your dependencies here
        'matlabengine',
        'numpy',
        'opencv-python',
    ],
)
