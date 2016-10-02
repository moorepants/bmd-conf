The source code for the main BMD conference website. The rendered version can
be viewed at:

http://moorepants.github.io/bmdconf

This site is generated with Pelican_.

.. _Pelican: getpelican.com

Build Instructions
==================

Install miniconda_ and add conda-forge as a channel. Create an environment for
Pelican sites::

   $ conda config --add channels conda-forge
   $ conda create -n pelican python=2 pelican ghp-import fabric
   $ source activate pelican
   (pelican)$

Rebuild and serve the site locally::

   (pelican)$ fab reserve

Push the site to Github pages::

   (pelican)$ fab gh_pages

.. _miniconda: http://conda.pydata.org/miniconda.html

License
=======

.. image:: https://i.creativecommons.org/l/by/4.0/88x31.png
   :target: http://creativecommons.org/licenses/by/4.0/
   :alt: Creative Commons License

This work is licensed under a `Creative Commons Attribution 4.0 International
License <href="http://creativecommons.org/licenses/by/4.0/">`_.
