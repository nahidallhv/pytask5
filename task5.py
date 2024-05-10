##print("Hello World")
class numHesablama:
    def __init__(self, numbers):
        self.numbers = numbers

    def add_numbers(self, nums_list):
      # self.numbers.append(nums_list)
        self.numbers.extend(nums_list)

    def num_Sum(self, target):
        indList = []
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == target:
                    indList.append((i, j))
        if indList:
            return indList
        else:
            return -1


my_list = [1, 2, 3, 4, 5]
hesablama = numHesablama(my_list)
hesablama.add_numbers([6, 7, 8])
print(hesablama.numbers) 
# print(hesablama.num_Sum(5))  
# print(hesablama.num_Sum(10))  
print(hesablama.num_Sum(7)) 

