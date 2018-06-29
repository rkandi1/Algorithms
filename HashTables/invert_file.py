""" Question 5 """
class InvertedFile:
    def __init__(self, file_name):
        self.inv_lst = []
        self.inv_dict = {}
        file = open(file_name)
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                continue
            self.inv_lst+=line.strip().split(" ")
        for index in range(len(self.inv_lst)):
            self.inv_lst[index]=self.inv_lst[index].lower().strip("\n,.")
            if self.inv_lst[index] not in self.inv_dict:
                self.inv_dict[self.inv_lst[index]] = []
            self.inv_dict[self.inv_lst[index]].append(index)

    def indices(self, word):
        if word not in self.inv_dict:
            return []
        return self.inv_dict[word]

