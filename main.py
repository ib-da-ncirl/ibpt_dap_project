# The MIT License (MIT)
# Copyright (c) 2019 Ian Buttimer

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from menu import Menu
import sys
from sales_journal import (
    get_app_config,
    make_call_execute_csv_to_postgres_pipeline,
    make_call_execute_csv_currency_to_postgres_pipeline,
    make_call_execute_interactive_plot_pipeline,
    make_call_execute_currency_to_postgres_pipeline,
    make_call_execute_create_sales_data_postgres_pipeline,
    make_call_execute_create_currency_data_postgres_pipeline,
    make_call_execute_clean_sales_data_postgres_pipeline,
    make_call_execute_clean_currency_data_postgres_pipeline,
)
from Apache_logs import (
    call_create_postgres_tables_pipeline,
    call_csv_to_postgres_pipeline,
    send_all_files_to_csv_postgres_pipeline,
    call_postgres_to_visualisation_pipeline
)

"""
"""





def main():

    # load app config
    (app_cfg, plotly_cfg) = get_app_config(sys.argv[0], sys.argv[1:])

    # resource entries for environment_dict
    postgres_warehouse = {'config': {'postgres_cfg': app_cfg['postgresdb']}}

    call_execute_csv_to_postgres_pipeline = \
        make_call_execute_csv_to_postgres_pipeline(app_cfg['sales_journal'], postgres_warehouse)

    call_execute_csv_currency_to_postgres_pipeline = \
        make_call_execute_csv_currency_to_postgres_pipeline(app_cfg['sales_journal'], postgres_warehouse)

    call_execute_interactive_plot_pipeline = \
        make_call_execute_interactive_plot_pipeline(app_cfg['sales_journal'], plotly_cfg, postgres_warehouse)

    call_execute_currency_to_postgres_pipeline = \
        make_call_execute_currency_to_postgres_pipeline(app_cfg['sales_journal'], postgres_warehouse)

    call_execute_create_sales_data_postgres_pipeline = \
        make_call_execute_create_sales_data_postgres_pipeline(app_cfg['sales_journal'], postgres_warehouse)

    call_execute_create_currency_data_postgres_pipeline = \
        make_call_execute_create_currency_data_postgres_pipeline(app_cfg['sales_journal']['currency'], postgres_warehouse)

    call_execute_clean_sales_data_postgres_pipeline = \
        make_call_execute_clean_sales_data_postgres_pipeline(app_cfg['sales_journal'], postgres_warehouse)

    call_execute_clean_currency_data_postgres_pipeline = \
        make_call_execute_clean_currency_data_postgres_pipeline(app_cfg['sales_journal']['currency'], postgres_warehouse)

    menu = Menu(title="Data Processing Menu")
    apache_sub = Menu(title="Apache Logs Processing Menu")
    sj_sub = Menu(title="SalesJournal Processing Menu")
    currency_sub = Menu(title="Supplementary non-submission Functionality Menu")
    menu.set_options([
        ("Apache Logs Processing", apache_sub.open),
        ("SalesJournal Processing", sj_sub.open),
        # ("Supplementary non-submission Functionality", currency_sub.open),
        ("Exit", Menu.CLOSE)
    ])
    apache_sub.set_options([
        ("Create apache log tables in Postgres", call_create_postgres_tables_pipeline),
        ("Upload one apache log data to Postgres", call_csv_to_postgres_pipeline),
        ("Upload all apache log data to Postgres", send_all_files_to_csv_postgres_pipeline),
        ("Generate plots", call_postgres_to_visualisation_pipeline),
        ("Return to main menu", apache_sub.close)
    ])
    sj_sub.set_options([
        ("Create sales data tables in Postgres", call_execute_create_sales_data_postgres_pipeline),
        ("Upload sales data to Postgres", call_execute_csv_to_postgres_pipeline),
        ("Interactive plot", call_execute_interactive_plot_pipeline),
        ("Clean sales data tables in Postgres", call_execute_clean_sales_data_postgres_pipeline),
        ("Return to main menu", sj_sub.close)
    ])
    currency_sub.set_options([
        ("Create currency data tables in Postgres", call_execute_create_currency_data_postgres_pipeline),
        ("Upload currency data to Postgres", call_execute_currency_to_postgres_pipeline),
        ("Clean currency data tables in Postgres", call_execute_clean_currency_data_postgres_pipeline),
        ("Return to main menu", currency_sub.close)
    ])
    menu.set_title_enabled(True)
    menu.open()


if __name__ == "__main__":
    main()

