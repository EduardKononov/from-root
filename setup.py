import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

# TODO(ekon): `poetry build`
#             `poetry publish`
setuptools.setup(
    name='from-root',
    version='1.0.2',
    author='Eduard Konanau',
    author_email='aduard.kononov@gmail.com',
    description='Forget about working directory errors',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/EduardKononov/from-root',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
