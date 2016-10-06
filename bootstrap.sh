#!/bin/bash

set -eo pipefail

if ! which pip >/dev/null; then
    echo "pip not found -- installing. NOTE: you may be prompted for your password.'"
    sudo easy_install pip
fi

if ! which virtualenv >/dev/null; then
    echo "virtualenv not found -- installing. NOTE: you may be prompted for your password.'"
    sudo pip install virtualenv
fi

if [[ ! -d env ]]; then
    echo "Preparing virtualenv"
    virtualenv env
fi

. env/bin/activate
pip install --upgrade -r requirements.txt


case ${1} in
    run)
        python src/app.py
    ;;
    test)
        for file in test/*_test.py; do
            PYTHONPATH=src python ${file}
        done
    ;;
esac
