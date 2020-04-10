import setuptools


with open('README.rst', 'rt') as readme_file:
    long_desc = readme_file.read()

setuptools.setup(
    name='uth',
    use_autover=True,
    description='Unit test helpers',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    url='https://github.com/janneronkko/uth',
    author='Janne Rönkkö',
    author_email='janne.ronkko@iki.fi',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Testing',
    ],
    keywords='unittest mock patch',
    py_modules=['uth'],
    python_requires='>=3.4',
    setup_requires=[
        'setuptools_autover',
    ],
)
