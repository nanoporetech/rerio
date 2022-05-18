Rerio Basecalling Models
""""""""""""""""""""""""

This directory contains research basecalling models for use with the Nanopore Guppy basecaller.

The research models intended for current use are described in the main Rerio README.
Description of some deprecated models can be found here.

Flip-flop Modified Base Models
------------------------------

Previous generations of modified base models were integrated in to the "flip-flop" basecaller output.
This produced canonical and modified basecalls from a single neural network.
The current recommendation for modified base calling is to use Remora models which separate the canonical basecalling from the modified base calling netowrks.
Remora models provide higher modified base detection accuracy, are more simple to train, and don't effect the canonical basecalled sequence.

Deprecated modified base model descriptions:

=============================================== ======= ====== ============== ============ ==========================
Config                                          DNA/RNA Pore   Device         Tested Guppy Notes
=============================================== ======= ====== ============== ============ ==========================
res_dna_r941_min_modbases_5mC_v001.cfg          DNA     R9.4.1 MinION/GridION v4.2.2       5mC in all context
res_dna_r941_prom_modbases_5mC_v001.cfg         DNA     R9.4.1 PromethION     v4.2.2       5mC in all context
res_dna_r103_prom_modbases_5mC_v001.cfg         DNA     R10.3  PromethION     v4.2.2       5mC in all context
res_dna_r941_min_modbases_5mC_5hmC_v001.cfg     DNA     R9.4.1 MinION/GridION v4.2.2       5hmC & 5mC in all context
res_dna_r941_min_modbases-all-context_v001.cfg  DNA     R9.4.1 MinION/GridION v3.5.1       5mC & 6mA in all contexts
=============================================== ======= ====== ============== ============ ==========================

Megalodon Support
-----------------

Rerio research models can be run within megalodon by specifying the data directory in the ``--guppy-params`` argument.

::

   megalodon fast5s/ --guppy-params "-d ./rerio/basecall_models/" \
       --guppy-config res_dna_r941_min_modbases_5mC_5hmC_CpG_v001.cfg \
       --mod-motif mh CG 0
