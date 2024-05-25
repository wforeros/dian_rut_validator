import csv

def export_to_csv(data, filename):
  keys = data[0].keys()
  with open(filename + '.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)