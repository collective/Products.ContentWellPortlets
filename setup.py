from setuptools import setup, find_packages
import os

version = '4.3.0.dev0'


setup(
    name='Products.ContentWellPortlets',
    version=version,
    description="A Plone product that enables you to add portlets to the "
                "central column in a page",
    long_description=open("README.txt").read() + "\n" +
                open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone portletmanager',
    author='WebLion',
    author_email='support@weblion.psu.edu',
    url='http://weblion.psu.edu',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFPlone>=4.0b1'
    ],
    extras_require=dict(
        test=[
            'Products.PloneTestCase',
        ]
    ),
    entry_points="""
    # -*- Entry points: -*-
    """,
)
