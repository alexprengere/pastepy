pastepy
=======
This is kind of a pure Python `paste` implementation.

Installation
------------
`docopt` is needed, so:
```bash
$ sudo pip install docopt
```

Examples
--------
Let's take two simple CSV files:
```bash
$ cat a.csv
a,b,1
a,c,2
$ cat b.csv
a,b,6
d,c,7
```
Try to paste them together given the first two fields as keys (hence the `0,1`):
```bash
$ python paste.py a.csv ',' 0,1 b.csv ',' 0,1
a,b;1;6
```
The `--complete` option fills data not present in all files with empty strings:
```bash
$ python paste.py a.csv ',' 0,1 b.csv ',' 0,1 --complete
a,b;1;6
d,c;;7
a,c;2;
```

More
----
You can paste more than 2 files together!
Indeed you can add other triplets of `<file> <delimiter> <key>`:
```bash
$ python paste.py -h
Usage:
  pastepy (<file> <delimiter> <key>)... [options]
  pastepy (-h | --help)
  pastepy --version

Arguments
  <file>       The file to be pasted
  <delimiter>  The line delimiter for that file
  <key>        The indices of the fields for the key, separated by ','

Options:
  -h --help                Show this screen.
  --version                Show version.
  -d <d>, --delimiter <d>  Change delimiter for output [default: ,].
  -c, --complete           If paste is not possible, add empty strings.

```
