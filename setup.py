from setuptools import setup, find_packages

version = "4.3.1"


setup(
    name="Products.ContentWellPortlets",
    version=version,
    description="A Plone product that enables you to add portlets to the "
    "central column in a page",
    long_description="%s\n%s" % (open("README.rst").read(), open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="plone portletmanager",
    author="WebLion",
    author_email="support@weblion.psu.edu",
    url="http://weblion.psu.edu",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["setuptools", "Products.CMFPlone>=4.0b1"],
    extras_require=dict(
        test=[
            "Products.PloneTestCase",
        ]
    ),
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
