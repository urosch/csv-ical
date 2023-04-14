"""
Example for converting a CSV file into an iCal file
"""

from datetime import datetime, timedelta
from typing import Any, List

from csv_ical import Convert


convert = Convert()
csv_file_location = '../slo_prazniki/eb8b25ea-5c00-4817-a670-26e1023677c6.csv'
ical_file_location = '../slo_prazniki/prazniki.ics'
csv_configs = {
    'HEADER_ROWS_TO_SKIP': 1,
    'CSV_NAME': 2,
    'CSV_START_DATE': 1,
    'CSV_END_DATE': 1,
    'CSV_DESCRIPTION': 4,
    'CSV_LOCATION': 3,
}

convert.read_csv(csv_file_location, csv_configs)
i = 0
while i < len(convert.csv_data):
    row: List[Any] = convert.csv_data[i]
    start_date = row[csv_configs['CSV_START_DATE']]
    end_date = row[csv_configs['CSV_END_DATE']]
    try:
        startal = datetime.strptime(start_date, '%Y-%d-%mT%H:%M:%S')
        row[csv_configs['CSV_START_DATE']] = startal.date()
        konec = datetime.strptime(end_date, '%Y-%d-%mT%H:%M:%S')
        row[csv_configs['CSV_END_DATE']] = konec.date()
        i += 1
    except ValueError:
        convert.csv_data.pop(i)
        print(convert.csv_data)
    row[csv_configs['CSV_NAME']] = row[csv_configs['CSV_NAME']]

convert.make_ical(csv_configs)
convert.save_ical(ical_file_location)
