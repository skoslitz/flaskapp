#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
  DEBUG=True,
  SECRET_KEY='You_will_never_know_:)'
)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

from flaskext.coffee import coffee
coffee(app) 

@app.route('/')
def index():
    return render_template('index.jade')

@app.route('/teeatlas')
def teeatlas():
	return render_template('teeatlas.jade')

@app.route('/teeatlas/taiwan')
def taiwan():
	return render_template('taiwan.jade')

if __name__ == '__main__':
    app.run()
