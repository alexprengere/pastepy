"""
Usage:
  pastepy (<file> <delimiter> <key>)... [options]
  pastepy (-h | --help)
  pastepy --version

Arguments
  <file>       The file to be joined
  <delimiter>  The delimiter for that file
  <key>        The indices of the fields for the key, separated by ','

Options:
  -h --help                Show this screen.
  --version                Show version.
  -d <d>, --delimiter <d>  Change delimiter for output [default: ,].
  -c, --complete           If paste is not possible, add empty strings.
"""

from __future__ import with_statement
from docopt import docopt


def get(row, delimiter, indices):
    """Extract key and value from row.

    >>> get('a,b,c', ',', (0, 1))
    (('a', 'b'), ('c',))
    >>> get('a,b,c', ',', (0, 2))
    (('a', 'c'), ('b',))
    """
    row = row.rstrip().split(delimiter)

    key = tuple(row[k] for k in indices)
    val = tuple(v for i, v in enumerate(row) if i not in indices)

    return key, val


def main(files, delimiters, keys, output_delimiter, complete):
    """Main runner.
    """
    data = {}
    for file_, d, key in zip(files, delimiters, keys):
        with open(file_) as f:
            data[file_] = dict(get(row, d, key) for row in f)

    # Processing the keys present in all files
    common_keys = set.intersection(*[
        set(d.iterkeys()) for d in data.itervalues()
    ])
    all_keys = set.union(*[
        set(d.iterkeys()) for d in data.itervalues()
    ])

    for key in all_keys:
        if complete or key in common_keys:
            line = [','.join(key)]
            for file_, d in zip(files, delimiters):
                line.append(d.join(data[file_].get(key, '')))
            print output_delimiter.join(line)


if __name__ == '__main__':

    kw = docopt(__doc__, version='Pastepy 0.1')

    main(**{
        'files'             : kw['<file>'],
        'delimiters'        : kw['<delimiter>'],
        'keys'              : [[int(i) for i in k.split(',')]
                                for k in kw['<key>']],
        'output_delimiter'  : kw['--delimiter'],
        'complete'          : kw['--complete'],
    })

