pastepy
=======

This is kind of a pure Python `paste` implementation.

```bash
$ cat a.csv
a,b,1
a,c,2
$ cat b.csv
a,b,6
d,c,7
$ python paste.py a.csv ',' 0,1 b.csv ',' 0,1 -d ';'
a,b;1;6
$ python paste.py a.csv ',' 0,1 b.csv ',' 0,1 -d ';' --complete
a,b;1;6
d,c;;7
a,c;2;
```

