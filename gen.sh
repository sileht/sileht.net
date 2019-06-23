#!/bin/bash

if [ "$1" == "-d" ] ; then
    DEBUG=True
    shift
fi

if [ ! -d "venv" ]; then
    virtualenv venv
    venv/bin/pip install pelican pysvg markdown beautifulsoup4 pillow typogrify cssutils html5lib
fi
source venv/bin/activate

pelican content -o output -s settings.py -d --ignore-cache $*
[ "$DEBUG" ] && exit 0
ghp-import output
git push origin gh-pages -f
rm -rf output
