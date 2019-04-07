
Centro-priceTag
=========

pricetag is a Django app powering the main website for pricetag
health system.

The latest source code is available at http://github.com/sonlinux/centro-pricetag.

* **Developers:** See our `project setup guide`_ and `developer guide`_


Project activity
----------------

Story queue on Waffle:

* [![Stories in Ready](https://badge.waffle.io/inasafe/inasafe.svg?label=ready&title=Ready)](http://waffle.io/inasafe/inasafe)
* [![Stories in In Progress](https://badge.waffle.io/inasafe/inasafe.svg?label=in%20progress&title=In%20Progress)](http://waffle.io/inasafe/inasafe)

[![Throughput Graph](https://graphs.waffle.io/kartoza/django-bims/throughput.svg)](https://waffle.io/inasafe/inasafe/metrics)

* Current test status master: [![Build Status](https://travis-ci.org/inasafe/inasafe.svg?branch=master)](https://travis-ci.org/inasafe/inasafe)

* Current test status develop: [![Build Status](https://travis-ci.org/inasafe/inasafe.svg?branch=develop)](https://travis-ci.org/inasafe/inasafe)



Quick Project Setup
-------------------

Refer to `project setup guide`_ for in depth information.

Make sure docker is installed, and project
already opened using PyCharm. Then run these command:


Quick Installation Guide
------------------------
For deployment I use `docker`_ so you need to have docker
running on the host. pricetag is a django app so it will help if you have
some knowledge of running a django site.

    git clone git://github.com/sonlinux/pricetag.git

    cd /project/root/dir/deployment

    make build

    make permissions

    make web

    make run

    # Wait a few seconds for the DB to start before to do the next command

    make migrate

    make collectstatic

    # You can access the project in two ways

    1. Via web server nginx by going to address in the web browser  

    >> http://0.0.0.0:60209/site-admin

    2. By setting up the local development server with Pycharm and this will
     expose the address. See instructions on setting up with pycharm locally
      in the README-dev.md file

      >> http://0.0.0.0:60206/site-admin



So as to create your admin account:
```
make superuser
```

[![PyCharm](https://cloud.githubusercontent.com/assets/1421861/16826865/4cde910c-49ab-11e6-95ae-48cf21f3a69f.png)](https://www.jetbrains.com/pycharm)

We use [PyCharm](https://www.jetbrains.com/pycharm) for our python development work

Thank you
_________


Thank you to the individual contributors who have helped to build pricetag
website:

* Alison Mukoma: AMukoma@brhc.com
