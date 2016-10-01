The source code for the main BMD conference website. The rendered version can
be viewed at:

http://moorepants.github.io/bmd-conf

This site is generated with Pelican_.

.. _Pelican: getpelican.com

Build Instructions
==================

Install miniconda_ and add conda-forge as a channel. Create an environment for
Pelican sites::

   $ conda config --add channels conda-forge
   $ conda create -n pelican python=2 pelican
   $ source activate pelican
   (pelican)$

Rebuild and serve the site locally::

   (pelican)$ fab reserve

Push the site to Github pages::

   (pelican)$ fab gh_pages

.. _miniconda: http://conda.pydata.org/miniconda.html

License
=======

.. raw:: html

   <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
     <img alt="Creative Commons License" style="border-width:0"
       src="https://i.creativecommons.org/l/by/4.0/88x31.png" />
   </a>
   <br />
   This work is licensed under a <a rel="license"
   href="http://creativecommons.org/licenses/by/4.0/">Creative Commons
   Attribution 4.0 International License</a>.
