from setuptools import setup, find_packages

version = '2.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
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
        'collective.behavior.banner',
        'collective.formscaptcha',
        'collective.quickupload',
        'collective.z3cform.widgets',
        'eea.facetednavigation',
        'ftw.footer',
        'Pillow',
        'Plone',
        'plone.api',
        'plone.app.contenttypes [atrefs]',
        'plonetheme.onegov',
        'Products.PloneFormGen',
        'Products.PloneKeywordManager[Levenshtein]',
        'Products.RedirectionTool',
        'setuptools',
        'Solgema.fullcalendar',
        'wildcard.foldercontents',
        'z3c.jbot',
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
