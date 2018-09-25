The source code for the main BMD conference website. The rendered version can
be viewed at:

http://bmdconf.org

This site is generated with Pelican_.

.. _Pelican: getpelican.com

Local Build Instructions
========================

Install miniconda_ and add conda-forge as a channel. Create an environment for
Pelican sites::

   $ conda config --add channels conda-forge
   $ conda create -n pelican pelican
   $ source activate pelican
   (pelican)$

Rebuild and serve the site locally::

   (pelican)$ make devserver

Stop the server::

   (pelican)$ make stopserver

Once changes are made, submit a pull request and the site will be built
automatically with doctr.

.. _miniconda: http://conda.pydata.org/miniconda.html

License
=======

.. image:: https://i.creativecommons.org/l/by/4.0/88x31.png
   :target: http://creativecommons.org/licenses/by/4.0/
   :alt: Creative Commons License

This work is licensed under a `Creative Commons Attribution 4.0 International
License <href="http://creativecommons.org/licenses/by/4.0/">`_.
