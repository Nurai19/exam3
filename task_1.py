dict_ = {
    "float": [],
    "bool": [],
    "none": [],
    "int": [],
    "str": []
}


class DistributeList:

    def __init__(self, our_list: list):
        self.our_list = our_list

    def send_list(self):
        for output in self.our_list:
            if float is type(output):
                dict_["float"].append(output)
            elif bool is type(output):
                dict_["bool"].append(output)
            elif None is type(output):
                dict_["none"].append(output)
            elif int is type(output):
                dict_["int"].append(output)
            elif str is type(output):
                dict_["str"].append(output)


Result = DistributeList([1, 4.7, "hi", False, None])
Result.send_list()
print(dict)
