from setuptools import setup, find_packages

version = '3.0a1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='pysv.policy',
    version=version,
    description="Policy for the pysv website",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='',
    author='Python Software Verband',
    author_email='info@python-verband.org',
    url='https://github.com/pysv/pysv_policy',
    license='gpl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['pysv'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Pillow',
        'Plone',
        'plone.api',
        'Products.CMFPlone',
        'Products.PFGDataGrid',
        'Products.PloneFormGen',
        'Products.PloneKeywordManager[Levenshtein]',
        'Products.RedirectionTool',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
