from setuptools import setup, find_packages

setup(
    name='PyPixDirectSDK',
    version='0.0.2',
    packages=find_packages(),
    package_data={'PyPix': ['PyPix/*']},

    install_requires=[
        # List your dependencies here
        'matlabengine',
        'numpy',
        'opencv-python',
    ],
)
