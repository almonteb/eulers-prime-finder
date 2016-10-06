#!/bin/bash

set -eo pipefail

which virtualenv >/dev/null

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
