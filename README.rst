==============
ckanext-raygun
==============

A plugin for capturing exceptions using the [raygun](https://raygun.com) service.

------------------
CKAN < 2.9 support
------------------
As of `1.0.0` this extention has been made to work with CKAN 2.9. While attempts have been made to maintain compatibility
with prior version of CKAN, there may be issues. If any issues are discovered we are happy to accept PRs. Alternatively for
compatibility <2.9 the `0.1.0` tag can be used

------------
Requirements
------------

We know this works with CKAN 2.9, if you are installing it in a prior version we would appreciate your contributions in supporting backwards compatibility.

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
Configuration of this plugin happens through standard python logging config and via a wsgi specific middleware that picks up the `ckanext.raygun.api_key` config field::

    # The api key for accessing raygun
    ckanext.raygun.api_key = <your_api_key_here>
    # Optionally, set RaygunSender config (see raygun4py README for more info)
    ckanext.raygun.sender_config = {}

    # To support ad-hoc paster commands reporting to raygun add the following handler to your log config

    # 1. extend your handlers definition
    [handlers]
    keys = console, raygun

    [logger_root]
    level = WARNING
    handlers = console, raygun

    # 2. configure a handler for raygun
    [handler_raygun]
    class = ckanext.raygun.plugin.RaygunHandler
    args = ('<your_api_key_here>', <raygun_sender_config>,)
    level = NOTSET
    formatter = generic




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
