.. image:: /ONT_logo.png
  :width: 800

******************

Rerio
"""""

Rerio contains "research release" basecalling models and configuration files.
All models are compatible with Guppy (see `community page <https://community.nanoporetech.com/downloads>`_ for download/install instructions).
Since research models often utilise new features, the latest version of Guppy may be required.

Installation
------------

Rerio can be downloaded by cloning from github ``git clone https://github.com/nanoporetech/rerio``.
Once Rerio has been downloaded, models can be downloaded via the ``download_model.py`` script.

::

   # Download all models
   rerio/download_model.py
   # Download specific model(s)
   rerio/download_model.py rerio/basecall_models/res_dna_r941_min_modbases-all-context_v001

Once desired models have been downloaded, they can be run by specifying the Guppy data path option (``-d`` or ``--data_path``) and selecting the desired config file (``-c`` or ``--config``).

::

   ./ont-guppy/bin/guppy_basecaller -i fast5s/ -s basecalled_fast5s \
       -d ./rerio/basecall_models/ \
       -c res_dna_r941_min_modbases-all-context_v001.cfg

Models Summary
--------------

============================================== ======= ====== ============== ========
Config                                         DNA/RNA Pore   Device         Modbases
============================================== ======= ====== ============== ========
res_dna_r941_min_modbases-all-context_v001.cfg DNA     R9.4.1 MinION/GridION 5mC, 6mA
============================================== ======= ====== ============== ========

Megalodon Support
-----------------

Rerio research models can be run within megalodon by specifying the data directory in the ``--guppy-params`` argument.

::

   megalodon fast5s/ --guppy-params "-d ./rerio/basecall_models/" \
       --guppy-config res_dna_r941_min_modbases-all-context_v001.cfg

Barcoding Support
-----------------

The Rerio github code repository includes a minimal barcoding stub to allow Guppy to run successfully.
In order to enable full Guppy barcoding capabilities, all barcoding files must be transferred from the guppy data directory to the rerio data directory.

::

   cp ont-guppy/data/barcoding/* rerio/basecall_models/barcoding/
   
Versioning
----------
Rerio is versioned by the minimum version of Guppy required to run _all_ models in the repository.  
A new release of Rerio will be tagged when a model is added that requires a more recent version of Guppy.


Licence and Copyright
---------------------

|copy| 2020 Oxford Nanopore Technologies Ltd.

.. |copy| unicode:: 0xA9 .. copyright sign

Rerio is distributed under the terms of the Oxford Nanopore
Technologies, Ltd.  Public License, v. 1.0.  If a copy of the License
was not distributed with this file, You can obtain one at
http://nanoporetech.com
