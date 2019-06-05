import setuptools

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='comments',
    version='1.0.0',
    packages=setuptools.find_packages(),
    install_requires=['urllib3', 'certifi'],
    url='https://github.com/AmanoTeam/comments',
    author='Amano Team',
    author_email='contact@amanoteam.ml',
    description='Python wrapper for the https://comments.bot API',
    long_description=readme,
    long_description_content_type='text/markdown'
)
