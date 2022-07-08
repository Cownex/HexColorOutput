from setuptools import setup, find_packages


setup(
    name='hex_color_output',
    version='1.1',
    license='MIT',
    author="Cownex",
    description="Color the output with Hex Color Codes.",
    author_email='contact@cownex.de',
    packages=find_packages('source'),
    package_dir={'': 'source'},
    long_description=open('readme.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/Cownex/HexOutput',
    keywords='python hex color terminal output color-output',
)