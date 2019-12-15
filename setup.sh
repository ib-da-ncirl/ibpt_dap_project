#!/bin/bash

echo Installing project and dependencies [pip]
pip3 install --no-cache-dir git+https://github.com/ib-da-ncirl/db_toolkit.git
pip3 install --no-cache-dir git+https://github.com/ib-da-ncirl/dagster_toolkit.git
pip3 install --no-cache-dir git+https://github.com/ib-da-ncirl/sales_journal.git
pip3 install --no-cache-dir git+https://github.com/philtap/Apache_logs

while true; do
    read -p "Do you wish to produce static plots using the SalesJournal pipeline?" yn
    case $yn in
        [Yy]* )
            # see https://github.com/plotly/orca
            echo Installing project dependencies [conda]
            conda install -c plotly plotly-orca
            break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo Creating directories
mkdir -p data
mkdir -p output



