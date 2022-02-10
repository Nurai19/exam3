import csv


class CsvManager:

    def __init__(self, data):
        self.data = data

    def sort_field(self):
        pass

    def adding_field(self):
        with open('dict.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow((self.data['first_name'], self.data['last_name'], self.data['age'], self.data['gender'],
                             self.data['hobby'], self.data['job']))
            f.close()

    def update_field(self):

        row_num = 1
        new_value = 'Replaced Line'

        with open('dict.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=';')
            lines = []

            for current_line in csv_reader:
                if csv_reader.line_num == row_num:
                    current_line = new_value
                lines.append(current_line)

        with open('dict.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(lines)

    def edit_field(self):
        line_to_editing = []
        with open('dict.csv') as f:
            csv_reader = csv.reader(f, delimiter=';')
            for row in csv_reader:
                line_to_editing.append(row)
        print(line_to_editing)
