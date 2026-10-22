import csv

info_count = 0
warning_count = 0
error_count = 0


try:
	with open('server.log', 'r') as log_file:
		for line in log_file:
			if "INFO" in line:
				info_count +=1
			elif "WARNING" in line:
				warning_count +=1
			elif "ERROR" in line:
				error_count +=1

except FileNotFoundError as e:
	print('file not found')

else:
	with open('log_summary.csv', 'w', newline = '') as csv_file:
		fieldnames = ['log_level','log_count']
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
		csv_writer.writeheader()

		csv_writer.writerow({'log_level': 'INFO', 'log_count': info_count})
		csv_writer.writerow({'log_level': 'WARNING', 'log_count': warning_count})
		csv_writer.writerow({'log_level': 'ERROR', 'log_count': error_count})

