import csv
import time


def run_code():
    mapping_file_name = 'mapping.csv'
    mappings = read_mapping_file(mapping_file_name)

    infile_name = 'index.html.md'
    replace_headings(infile_name, mappings)


def read_mapping_file(file_name):
    mapping = {}
    with open(file_name, newline='') as csvfile:
        mapping_csv = csv.reader(csvfile, delimiter=',')
        next(mapping_csv)
        for row in mapping_csv:
            mapping[row[0]] = row[1]
    return mapping


def replace_headings(file_name, mapping):
    fin = open(file_name, "rt")
    data = fin.read()
    for from_value, to_value in mapping.items():
        data = data.replace('# {}'.format(from_value), '# {}'.format(to_value))
    fin.close()

    fin = open(file_name, "wt")
    fin.write(data)
    fin.close()


if __name__ == '__main__':
    run_code()
