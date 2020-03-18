.. image:: /ONT_logo.png
  :width: 800

******************

Rerio
"""""

Rerio contains "research release" basecalling models and configuration files.
All models are compatible with guppy (see `community page <https://community.nanoporetech.com/downloads>`_ for download/install instructions).
Since research models often utilise new features, the latest version of guppy may be need to be installed.

Installation
------------

Rerio can be downloaded by cloning from github ``git clone https://github.com/nanoporetech/rerio``.
Once rerio has been downloaded, models can be downloaded via the ``download_model.py`` script.

::

   # download all models
   python3 download_model.py --download-all-models
   # download specific model(s)
   python3 download_model.py basecall_models/res_dna_r941_min_modbases-all-context.v001

Once desired models have been downloaded, they can be run by specifying the guppy data path option (``-d`` or ``--data_path``) and selecting the desired config file (``-c`` or ``--config``).

::

   ./ont-guppy/bin/guppy_basecaller -i fast5s/ -s basecalled_fast5s \
       -d ./rerio/basecall_models/ \
       -c res_dna_r941_min_modbases-all-context.v001.cfg

Models Summary
--------------

============================================== ======= ====== ============== ========
Config                                         DNA/RNA Pore   Device         Modbases
============================================== ======= ====== ============== ========
res_dna_r941_min_modbases-all-context.v001.cfg DNA     R9.4.1 MinION/GridION 5mC, 6mA
============================================== ======= ====== ============== ========

Megalodon Support
-----------------

Rerio research models can be run within megalodon by specifying the data directory in the ``--guppy-params`` argument.

::

   megalodon fast5s/ --guppy-params "-d ./rerio/basecall_models/" \
       --guppy-config res_dna_r941_min_modbases-all-context.v001.cfg

Licence and Copyright
---------------------

|copy| 2020 Oxford Nanopore Technologies Ltd.

.. |copy| unicode:: 0xA9 .. copyright sign

Rerio is distributed under the terms of the Oxford Nanopore
Technologies, Ltd.  Public License, v. 1.0.  If a copy of the License
was not distributed with this file, You can obtain one at
http://nanoporetech.com
