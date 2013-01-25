The buildout configuration of the Python Software Verband Plone 4 Website

##Installation for Development

### Prerequisites
- Python 2.7
- virtualenv
- libxslt-dev

### Checkout & Prepare Source
    $ git clone git@github.com:pysv/pysv_buildout.git
    $ cd pysv_buildout/
    $ virtualenv virt_env
    $ source virt_env/bin/activate
    $ ln -s devel.cfg buildout.cfg

### Run bootstrap
    $ python bootstrap.py
    $ ./bin/develop co pysv.policy
    $ ./bin/buildout


### Start Plone
    $ bin/instance fg

[http://localhost:13090/](http://localhost:13090/)

