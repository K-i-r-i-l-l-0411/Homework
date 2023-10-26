import time
def timestamp_to_year(timestamp):
    time_struct = time.gmtime(timestamp)
    year = time_struct.tm_year
    return year

timestamp = 1624198275
#timestamp = int(input())
year = timestamp_to_year(timestamp)
print(f'Измерение происходило в {year} году')