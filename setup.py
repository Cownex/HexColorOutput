from setuptools import setup, find_packages


setup(
    name='hex_color_output',
    version='1.0.3',
    license='MIT',
    author="Cownex",
    description="Hexcolor print",
    author_email='contact@cownex.de',
    packages=find_packages('source'),
    package_dir={'': 'source'},
    url='https://github.com/Cownex/HexOutput',
    keywords='python hex color terminal output color-output',
)