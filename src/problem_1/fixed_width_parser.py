import csv

def file_parsing(input_file, spec, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        for line in f_in:
            parsed_row = []
            start = 0
            for width in spec:
                parsed_row.append(line[start:start + width].strip())
                start += width
            writer.writerow(parsed_row)

# Example usage:
spec = [20, 25, 30]
file_parsing('input.txt', spec, 'output.csv')
