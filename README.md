# [is-democracy-on-fire](http://www.isdemocracyonfire.com)  
A Flask implementation of a simple website, designed to answer a burning question  

## Intro  
is-democracy-on-fire (IDOF) is a project I started to learn a little bit about Flask, the popular web app framework for Python.  

## Running IDOF  
Running IDOF on your local machine is simple. Import the `app` module, create an `app` instance, and run it. You can do this in a python interpreter or standalone script like so:  


```python  
import app  

idof = app.create_app()  
idof.run()  
```  

This will start Flask's own web server and make IDOF available at `127.0.0.1:5000`. If you would like to run IDOF on an Apache web server, see [these instructions](doc/apache.md).  

