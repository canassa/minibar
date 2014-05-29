Minibar
========

A (WIP) python progress bar

.. image:: https://travis-ci.org/canassa/minibar.svg?branch=master
  :alt: Travis CI build status
  :target: https://travis-ci.org/canassa/minibar
  
Installing
----------

.. code-block:: python

    pip install minibar

Usage
-----

.. code-block:: python

    import minibar
    import time

    for i in minibar.bar(range(100)):
        time.sleep(0.05)

Minibar can be customized
--------------------------

.. code-block:: python

    bar = minibar.format('Time left: {bar} {eta}')

    for i in minibar(range(100)):
        time.sleep(0.05)

The following widgets are avaliable

* ``{bar}`` The progress bar
* ``{time_ellapsed}`` The time ellapsed
* ``{eta}`` The estimated time to finish
* ``{counter}`` 0 of 100
