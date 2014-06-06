from setuptools import setup, find_packages

setup(
    name='django-range-filter',
    version='1.0.0',
    description='Range filters for django admin',
    long_description=open('README.md').read(-1),
    author='Andrew Wang',
    author_email='andrew.dong.wang@gmail.com',
    url='http://github.com/ac0x/django-range-filter',
    keywords=[
        'django admin',
        'django range filter',
    ],
    install_requires=[
        "Django",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Environment :: Web Environment',
        'Operating System :: OS Independent'
    ],
    license='License :: OSI Approved :: BSD License',
)
