import csv
from io import TextIOWrapper


class CsvManager:

    # def __int__(self, action: str):
    #     self.file = open('data.csv')

    def manage_file(self, action: str) -> TextIOWrapper:
        return open('data.csv', action)

    def sort_field(self):
        pass

    def add_field(self, data: str):
        file = self.manage_file('a')
        writer = csv.writer(file)

        for row in data:
            writer.writerow(row)

        file.close()

    def update_field(self, target: str, new_value: str):
        data_list = list(csv.reader(self.manage_file('r')))

        for el in data_list:
            if target in el:
                indx = el.index(target)
                el[indx] = new_value

        writer = csv.writer(self.manage_file('w'))
        writer.writerow(data_list)

    def edit_field(self):
        pass

    def find_data(target: str):
        pass


manager = CsvManager
# manager.add_field('name', 'age')
manager.update_field('name', 'surname')