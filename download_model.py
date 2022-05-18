#!/usr/bin/env python3

import sys
import argparse
import os
import tarfile
from urllib import request

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")


CHECKPOINT_DIR = 'taiyaki_models'
MODELS_DIR = 'basecall_models'
CLAIR3_DIR = 'clair3_models'
REMORA_DIR = 'remora_models'


def get_parser():
    parser = argparse.ArgumentParser(description='Download model files.')

    model_grp = parser.add_mutually_exclusive_group()
    model_grp.add_argument(
        '--checkpoints', action='store_true',
        help='Download Taiyaki checkpoints rather than Guppy models'
    )
    model_grp.add_argument(
        '--clair3', action='store_true',
        help='Download Clair3 models rather than Guppy models'
    )
    model_grp.add_argument(
        '--remora', action='store_true',
        help='Download Remora models rather than Guppy models'
    )

    parser.add_argument(
        'model_stubs', nargs='*',
        help='Path to model stubs found in `rerio/basecall_models/`.'
    )

    return parser


def main():
    args = get_parser().parse_args()

    rootdir = os.path.dirname(os.path.realpath(__file__))
    modeldir = os.path.join(
        rootdir,
        CHECKPOINT_DIR if args.checkpoints
        else CLAIR3_DIR if args.clair3
        else REMORA_DIR if args.remora
        else MODELS_DIR
    )
    if len(args.model_stubs) == 0:
        args.model_stubs = [
            os.path.join(modeldir, fn)
            for fn in os.listdir(modeldir)
            if os.path.splitext(fn)[1] == ''
        ]

    model_urls = []
    for stub_fn in args.model_stubs:
        try:
            with open(stub_fn)as stub_fp:
                stub_lines = stub_fp.readlines()
        except (IsADirectoryError, UnicodeDecodeError):
            continue

        if len(stub_lines) != 1:
            sys.stderr.write(
                'Skipping invalid stub file: {}\n'.format(stub_fn))
            continue

        model_urls.append((stub_lines[0].strip(), stub_fn))

    sys.stderr.write('Models to download\n')
    for i, (_, stub_fn) in enumerate(model_urls):
        sys.stderr.write('{:3d}: {}\n'.format(
            i + 1, os.path.basename(stub_fn)))

    download_failed = False
    for model_url, stub_fn in model_urls:
        stub_base = os.path.basename(stub_fn)
        sys.stderr.write('Downloading {}\n'.format(stub_base))
        stub_tgz_fn = stub_fn + '.tgz'
        try:
            with open(stub_tgz_fn, 'wb') as fp:
                fp.write(request.urlopen(model_url).read())
            with tarfile.open(stub_tgz_fn, 'r:gz') as tar_fp:
                tar_fp.extractall(modeldir)
            os.remove(stub_tgz_fn)
        except Exception as e:
            sys.stderr.write('Error for {} ({})\n'.format(stub_base, e))
            download_failed = True

    return download_failed


if __name__ == '__main__':
    exit(main())
