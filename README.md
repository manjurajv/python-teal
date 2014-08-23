python-teal
===========

Dynamically plot performance data of processes


Installation Instructions
-----------------

**Create virtual environment**
```bash
$ virtualenv --no-site-packages teal
```

**Activate environment**
```bash
$ source teal/bin/activate
```

**Install dependencies**
```bash
(teal)$ pip install matplotlib
```

AFAIK, it's not possible to install wx under virtualenv.

The hack we follow is on [Stack Overflow](http://stackoverflow.com/questions/6977799/installing-wxpython-in-virtualenv-under-linux)

**Install dependencies outside virtualenv**
```bash
$ sudo apt-get install python-wxgtk2.8 python-2hon-wxtools wx2.8-doc wx2.8-examples wx2.8-headers wx2.8-i18n
```

**Create symlinks inside virtualenv**
```bash
cd <teal>/lib/python-2.7/site-packages
ln -s /usr/lib/python2.7/dist-packages/wx-2.8-gtk2-unicode/ .
ln -s /usr/lib/python2.7/dist-packages/wx.pth .
ln -s /usr/lib/python2.7/dist-packages/wxversion.py .
ln -s /usr/lib/python2.7/dist-packages/wxversion.pyc .
```
