import csv
import numpy
import matplotlib.pyplot as plt

# This will result in error, because some entries are string instead of numbers
# data = numpy.loadtxt(fname='AII_7_7.csv', delimiter=',')

with open('AII_7_7.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = numpy.array
    for row in csv_reader:
        # print(row)
        for entry in row:
            print(type(entry), entry)

# fig = plt.figure(figsize=(10.0, 3.0))

# axes1 = fig.add_subplot(1, 3, 1)
# axes2 = fig.add_subplot(1, 3, 2)
# axes3 = fig.add_subplot(1, 3, 3)

# axes1.set_ylabel('average')
# axes1.plot(numpy.mean(data, axis=0))

# axes2.set_ylabel('max')
# axes2.plot(numpy.max(data, axis=0))

# axes3.set_ylabel('min')
# axes3.plot(numpy.min(data, axis=0))

# fig.tight_layout()

# plt.savefig('inflammation.png')
# plt.show()
