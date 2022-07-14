from setuptools import setup, find_packages

setup(
    name='hex_color_output',
    version='1.1.5',
    license='MIT',
    author="Cownex",
    description="Output Terminal Color with HexCodes!",
    author_email='contact@cownex.de',
    packages=find_packages('source'),
    package_dir={'': 'source'},
    url='https://github.com/Cownex/HexColorOutput',
    keywords='python hex color terminal output color-output',
)
