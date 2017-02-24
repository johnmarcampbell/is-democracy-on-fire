# [is-democracy-on-fire](http://www.isdemocracyonfire.com)
A Flask implementation of a simple website, designed to answer a burning question

##Intro
is-democracy-on-fire (IDOF) is a project I started to learn a little bit about Flask, the popular web app framework for Python.

## Running locally
Running IDOF on your local machine is simple. Import the `app` module, create an `app` instance, and run it. You can do this in a python interpreter or standalone script like so:


```python
import app

idof = app.create_app()
idof.run()
```

This will start Flask's own web server and make IDOF available at `127.0.0.1:50001`. 

## Running on Apache
Running IDOF with an Apache web server requires the [`mod_wsgi`](https://modwsgi.readthedocs.io/en/develop/) Apache module. You can install this on a Debian system (and subsequently enable it) with:

```shell
apt-get install libapache2-mod-wsgi
a2enmod wsgi
```

The source includes two files to configure IDOF to run on Apache. 
* `app.wsgi` is a script that `mod_wsgi` will use to load the IDOF app
* `idof.conf` is a virtual host configuration file. This should be copied (or linked) to wherever your Apache installation keeps these files.

### Where to install?
`app.wsgi` and `idof.conf` assume you are cloning this repo into /var/www/idof. If that is not the case, you'll have to make two minor changes:
* **If** you are using a virtual environment, you'll have to change the `VIRTUAL_PATH` variable in `app.wsgi` to wherever you installed the source.
* In `idof.conf`, the second value set for the `WSGIScriptAlias` option should be the correct path to `app.wsgi`.

### How to install?
Installing the app would look something like this

```shell
git clone git@github.com:johnmarcampbell/is-democracy-on-fire.git /var/www/idof
cd /var/www/idof
[Set up and activate a virtual environment here if you wish]
pip install -r requirements.txt
cp idof.conf /etc/apache2/sites-available
a2ensite idof
service apache2 restart
```

Depending on how your Apache installation is configured, some of these paths may need to be changed. Most of these commands will need to be run with elevated priviliges by using `sudo`.
