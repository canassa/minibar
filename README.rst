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

Output:

.. image:: https://raw.githubusercontent.com/canassa/minibar/master/docs/img/progressbar_01-400x22.gif
  :alt: Progress bar


Minibar can be customized
--------------------------

.. code-block:: python

    template = "{i}/{total} {bar} {elapsed}s {eta}"

    for i in minibar(range(100), template=template):
        time.sleep(0.05)

The following widgets are avaliable:

* ``{i}`` The numeric progress counter.
* ``{total}`` The total value.
* ``{bar}`` The progress bar.
* ``{elapsed}`` The time ellapsed in seconds.
* ``{eta}`` The estimated time to finish.
