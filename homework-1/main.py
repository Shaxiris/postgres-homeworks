"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os.path
import psycopg2

BASEDIR = os.path.abspath('..')
PATH_TO_DATA = os.path.join(BASEDIR, 'homework-1', 'north_data')


def get_csv_data(path):
    with open(path, 'r', encoding='utf-8') as csv_file:
        csv_data = [data for data in csv.reader(csv_file)]

    return csv_data


def add_data(table_name, data, cur):
    column_amount = ', '.join(["%s"] * len(data[0]))

    cur.executemany(f'INSERT INTO {table_name} VALUES({column_amount})', data[1:])


if __name__ == '__main__':
    customers_data = get_csv_data(os.path.join(PATH_TO_DATA, 'customers_data.csv'))
    employee_data = get_csv_data(os.path.join(PATH_TO_DATA, 'employees_data.csv'))
    orders_data = get_csv_data(os.path.join(PATH_TO_DATA, 'orders_data.csv'))

    with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="12345"
    ) as conn:
        with conn.cursor() as cur:

            add_data('customers', customers_data, cur)
            add_data('employees', employee_data, cur)
            add_data('orders', orders_data, cur)

    conn.close()
