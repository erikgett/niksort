import time
import pandas as pd
import numpy as np


class TableInterseption:

    def __init__(self, filenamelist):
        self.filenamelist = filenamelist
        self.i = len(self.filenamelist) - 1

    def createlistfromfile(self, filename="_bysviat_.txt"):
        niknames = open(filename, "r")
        list_niks = []

        while True:
            line = niknames.readline()
            if not line:
                break
            list_niks.append(line.strip())
        niknames.close

        return list_niks

    def sortandwritetotxt(self, list=[], filename="_bysviat_.txt"):
        sorted_list = sorted(list)
        f = open('sorted' + filename, "w")
        for item in sorted_list:
            f.write("%s\n" % item)

        return sorted_list

    def functionreadandsort(self, filename="_bysviat_.txt"):
        list_niks = self.createlistfromfile(filename)
        sorted_list = self.sortandwritetotxt(list_niks)
        return sorted_list, list_niks

    def findbyname(self, name="alsdfkj", sorted_list=["alsdfkj", "alsdfasdfkj"]):
        if name in sorted_list:
            print("it in list, index -", sorted_list.index(name))
        else:
            print("it is not in list")

    def binary_search(self, data, elem):
        low = 0
        high = len(data) - 1

        while low <= high:

            middle = (low + high) // 2

            if data[middle] == elem:
                return middle
            elif data[middle] > elem:
                high = middle - 1
            else:
                low = middle + 1

        return -1

    def intersection_list(self, list1, list2):
        interseptions = len(set(list1).intersection(list2))
        N1 = interseptions / len(list1) * 100
        N2 = interseptions / len(list2) * 100
        return N1, N2, interseptions



    def intersectionlastwithall(self, i=3, listcomparison=[]):

        lastlist = self.createlistfromfile('sorted' + self.filenamelist[i])

        dictwithinfo = {}
        for g in range(self.i + 1):
            dictwithinfo[g] = None

        for t in range(i):
            listN = self.createlistfromfile('sorted' + self.filenamelist[t])

            a = self.intersection_list(lastlist, listN)


            print(self.filenamelist[i], 'сравнил с', self.filenamelist[t], "получили-", a)

            listcomparison.append(a)
        return listcomparison

    def intersection_recursive(self, a=0, infolist=[]):

        i = self.i - a

        if i == (self.i):
            #     сортируем и записываем отсортированные файлы
            for i in range(self.i + 1):
                listniks = self.createlistfromfile(self.filenamelist[i])
                self.sortandwritetotxt(listniks, self.filenamelist[i])



        if i != 0:
            a += 1

            infolist = self.intersectionlastwithall(i)
            self.intersection_list(self.filenamelist[a], self.filenamelist[i])
            return self.intersection_recursive(a, infolist)
        print(infolist)

        return infolist

    def generatehtmltable(self):
        print('nf')









x = TableInterseption(["_bysviat_.txt", "_bysviatmi_.txt", "_volkeit_.txt", "_volkeitmi_.txt"])
x.intersection_recursive()
