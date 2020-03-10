.. image:: /ONT_logo.png
  :width: 800

******************

Rerio
"""""

Rerio contains "research release" basecalling models and configuration files.
All models are compatible with guppy (see `community page <https://community.nanoporetech.com/downloads>`_ for download/install instructions).

Installation
------------

Rerio can be downloaded by cloning from github ``git clone https://github.com/nanoporetech/rerio``.
Once downloaded, models can be run by specifying the guppy data path option (``-d`` or ``--data_path``) and selecting the desired config file.

::

    git clone https://github.com/nanoporetech/rerio
    ./ont-guppy/bin/guppy_basecaller -i fast5s/ -s basecalled_fast5s \
        -c dna_r9.4.1_450bps_modbases_all-context_hac.cfg -d ./rerio/

Megalodon Support
-----------------

Rerio research models can be run within megalodon by specifying the data directory in the ``--guppy-params`` argument.

::

   megalodon fast5s/ --guppy-params "-d ./rerio/" --guppy-config dna_r9.4.1_450bps_modbases_all-context_hac.cfg

Licence and Copyright
---------------------

|copy| 2020 Oxford Nanopore Technologies Ltd.

.. |copy| unicode:: 0xA9 .. copyright sign

Megalodon is distributed under the terms of the Oxford Nanopore
Technologies, Ltd.  Public License, v. 1.0.  If a copy of the License
was not distributed with this file, You can obtain one at
http://nanoporetech.com
