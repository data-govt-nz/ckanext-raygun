.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/mediasuite/ckanext-raygun.svg?branch=master
    :target: https://travis-ci.org/mediasuite/ckanext-raygun

.. image:: https://coveralls.io/repos/mediasuite/ckanext-raygun/badge.svg
  :target: https://coveralls.io/r/mediasuite/ckanext-raygun

.. image:: https://pypip.in/download/ckanext-raygun/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-raygun/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-raygun/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-raygun/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-raygun/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-raygun/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-raygun/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-raygun/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-raygun/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-raygun/
    :alt: License

=============
ckanext-raygun
=============

A plugin for capturing exceptions using the [raygun](https://raygun.com) service.

------------
Requirements
------------

We know this works with CKAN 2.7, if you are installing it in a prior version we would appreciate your contributions in supporting backwards compatibility.

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-raygun:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-raygun Python package into your virtual environment::

     pip install ckanext-raygun

3. Add ``raygun`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

    # The api key for accessing raygun
    ckanext.raygun.api_key = your_secret_key


------------------------
Development Installation
------------------------

To install ckanext-raygun for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/mediasuite/ckanext-raygun.git
    cd ckanext-raygun
    pip install -e .
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.raygun --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-raygun on PyPI
---------------------------------

ckanext-raygun should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-raygun. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-raygun
----------------------------------------

ckanext-raygun is availabe on PyPI as https://pypi.python.org/pypi/ckanext-raygun.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
