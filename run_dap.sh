#!/bin/bash

export POSTGRES_CFG=dap_postgres.cfg
export CSV_DIR_PATH=data/apache_logs

#python3 -q main.py --cfg_path=dap_config.yaml --plot_path=plots.yaml --data_dir=data/sales_journal --orca_exe=/home/ibuttimer/anaconda3/lib/orca_app/orca
python3 -q main.py --cfg_path=dap_config.yaml --plot_path=plots.yaml --data_dir=data/sales_journal
