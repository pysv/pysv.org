The buildout configuration of the Python Software Verband Plone 4 Website

##Installation for Development

### Use Plone Unified Installer to fill up the buildout cachel (to prevent hazzle with removed pypi packages):
    $ wget https://launchpad.net/plone/4.2/4.2.3/+download/Plone-4.2.3-UnifiedInstaller.tgz
    $ tar xfz Plone-4.2.3-UnifiedInstaller.tgz
    $ rm Plone-4.2.3-UnifiedInstaller.tgz 
    $ ./Plone-4.2.3-UnifiedInstaller/install.sh --target=<Pfadd> standalone 


### Checkout & Prepare Source
    $ git clone git@github.com:pysv/pysv_buildout.git
    $ ln -s devel.cfg buildout.cfg

### Run bootstrap


### Start Plone

