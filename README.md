luften-i-debatten-ar-unken-och-instangd
=======================================

A web spider that crawls www.dn.se, downloads landscape formatted byline images and aggregates them into a collage.


Usage
=====

    $ cd luften-i-debatten-ar-unken-och-instangd

    $ mkvirtualenv luften

    $ pip install -r pip_requirements.txt

    $ cd scrapyproject

    $ scrapy crawl dn

    $ cd ..

    $ python collage.py

Your collage will be in /tmp/collage.jpg