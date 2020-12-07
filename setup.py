import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='from_root',
    version='0.0.1',
    author='Eduard Konanau',
    author_email='aduard.kononov@gmail.com',
    description=(
        'Helps you forget about FileNotFoundError, Path().parent.parent.parent hell, working directory errors etc.'
    ),
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