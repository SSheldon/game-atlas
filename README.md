Prerequisites
----------
Before you can set up Game Atlas, you'll need the following programs:
* [git](http://git-scm.com)
* [Python 2.7](http://www.python.org)
* [pip](http://www.pip-installer.org)
* [virtualenv](http://www.virtualenv.org)
* [PostgreSQL](http://www.postgresql.org)

Setup
----------
To set up Game Atlas for development, run the following commands:

    $ git clone git@github.com:SSheldon/game-atlas.git && cd game-atlas
    $ virtualenv --distribute venv
    $ source activate
    $ pip install -r requirements.txt
    $ initdb

At this point, you may run Postgres using the steps below.
After starting Postgres, create the Game Atlas database with this command:

    $ createdb game_atlas

Running Postgres
----------
A Postgres server must be running for Game Atlas to connect to.
Remember that the environment variables must be defined in your shell via
sourcing the activate file.

You can run Postgres in a shell with the following command:

    $ postgres

Or, if you'd prefer to run Postgres in the background, use this command:

    $ pg_ctl -l $PGDATA/server.log start

And, to shut it down:

    $ pg_ctl stop

If you encounter a "could not create shared memory segment" error on OSX,
follow the instructions detailed here:
http://ruby.zigzo.com/2012/07/07/postgresql-postgres-app-and-a-gotcha-on-mac-osx-lion/

Running Django
----------
With Postgres running and the environment variables defined, you may run
Django with this command:

    $ python manage.py runserver

At this point, you are running Game Atlas locally and may visit it at
http://localhost:8000.
