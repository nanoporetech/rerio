import os
import sys
from urllib import request
import tarfile
import argparse


MODELS_DIR = 'basecall_models'


def get_parser():
    parser = argparse.ArgumentParser(description='Download model files.')
    parser.add_argument(
        'model_stubs', nargs='*',
        help='Path to model stubs found in `rerio/basecall_models/`.')
    parser.add_argument(
        '--download-all-models', action='store_true',
        help='Download all models.')

    return parser


def main():
    args = get_parser().parse_args()
    model_out_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        MODELS_DIR)
    if args.download_all_models:
        model_urls = []
        for fn in os.listdir(model_out_path):
            if fn.endswith('cfg') or fn.endswith('jsn'):
                continue
            stub_fn = os.path.join(model_out_path, fn)
            with open(stub_fn) as stub_fp:
                try:
                    stub_lines = stub_fp.readlines()
                except UnicodeDecodeError:
                    continue
                if len(stub_lines) != 1:
                    continue
                model_urls.append((stub_lines[0].strip(), stub_fn))
    else:
        for stub_fn in args.model_stubs:
            with open(stub_fn) as stub_fp:
                stub_lines = stub_fp.readlines()
                if len(stub_lines) > 1:
                    sys.stderr.write(
                        'Skipping invalid stub file: {}\n'.format(fn))
                    continue
                model_urls.append((stub_lines[0].strip(), stub_fn))

    sys.stderr.write('Downloading models\n')
    for model_url, stub_fn in model_urls:
        sys.stderr.write('Downloading {}\n'.format(stub_fn))
        stub_tgz_fn = stub_fn + '.tgz'
        with open(stub_tgz_fn, 'wb') as fp:
            fp.write(request.urlopen(model_url).read())
        with tarfile.open(stub_tgz_fn, 'r:gz') as tar_fp:
            tar_fp.extractall(model_out_path)
        os.remove(stub_tgz_fn)


if __name__ == '__main__':
    main()
