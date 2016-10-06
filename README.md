# Euler's Prime Finder
Euler's Prime Finder is a flask application which will calculate the Xth Y digit prime number in the expansion of Euler's number.

## Requirements
* bash
* virtualenv
* python
* pip

## Getting started
Upon first execution of the bootstrap script, it'll do the following:

1. Ensure virtualenv is installed (if not: pip install virtualenv)
2. If the virtualenv has not been created, create & install dependencies (via pip)
3. Either launch the webserver or run tests (depending on the value of ARG[1])

## Launch
1. Run the following command:

        ./bootstrap.sh run
2. Browse to http://localhost:5000

## Run tests
    ./bootstrap.sh test