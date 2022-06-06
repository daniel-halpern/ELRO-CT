from random import randint, random

# Plotting libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#

def normalizeType(type):
    """
    Normalize the type of the apartment
    :param type: type of the apartment
    :return: the normalized type
    """
    if type == 'coop':
        return 0
    else:
        return 1

def normalizeBedroom(bedroom):
    """
    Normalize the number of bedrooms
    :param bedroom: number of bedrooms
    :return: the normalized number of bedrooms
    """
    return (bedroom - 1)/6

def normalizeBathroom(bathroom):
    """
    Normalize the number of bathrooms
    :param bathroom: number of bathrooms
    :return: the normalized number of bathrooms
    """
    return (bathroom - 1)/5

def normalizeLivingroom(livingroom):
    """
    Normalize the number of livingrooms
    :param livingroom: number of livingrooms
    :return: the normalized number of livingrooms
    """
    return (livingroom - 1)/2

def normalizeDiningroom(diningroom):
    """
    Normalize the number of diningrooms
    :param diningroom: number of diningrooms
    :return: the normalized number of diningrooms
    """
    return diningroom - 1

def normalizeCondition(condition):
    """
    Normalize the condition of the apartment
    :param condition: condition of the apartment
    :return: the normalized condition
    """
    return (livingroom - 2)/3

def normalizeArea(area):
    """
    Normalize the area of the apartment
    :param area: area of the apartment
    :return: the normalized area
    """
    return (area-900)/3600


def calculateOutput(weights, type, bedroom, bathroom, livingroom, diningroom, condition, area):
    """
    Calculate the output of the perceptron
    :param weights: weights of the perceptron
    :param sat: SAT score
    :param gpa: GPA score
    :param essay: essay score
    :param rec: recommendation score
    :param extra: extra score
    :return: the output of the perceptron
    """
    sum = weights[1] * type + weights[2] * bedroom + weights[3] * bathroom + weights[4] * livingroom + weights[5] * diningroom + weights[6] * condition + weights[7] * area + weights[0]
    if sum > 0:
        return 1
    else:
        return -1


########################################################################################################################
#                                                                                                                      # 
#                                               APP START                                                              #
#                                                                                                                      #
########################################################################################################################


# Training Data

type = []
bedroom = []
bathroom = []
livingroom = []
diningroom = []
condition = []
area = []
price = []

# Weights
weights = [random()*10, random()*10, random()*10, random()*10, random()*10, random()*10, random()*10, random()*10]
startingWeights = weights

# Read the data from the file
with open('./inputs/training.txt', 'r') as f:
    for row in f:
            row_lst = row.split()
            type.append(row_lst[0])
            bedroom.append(float(row_lst[1]))
            bathroom.append(float(row_lst[2]))
            livingroom.append(float(row_lst[3]))
            diningroom.append(float(row_lst[4]))
            condition.append(float(row_lst[5]))
            area.append(float(row_lst[6]))

# Normalize the sat score
for i in range(0, len(type)):
    type[i] = normalizeType(type[i])
    bedroom[i] = normalizeType(bedroom[i])
    bathroom[i] = normalizeType(bathroom[i])
    livingroom[i] = normalizeType(livingroom[i])
    diningroom[i] = normalizeType(diningroom[i])
    condition[i] = normalizeType(condition[i])
    area[i] = normalizeType(area[i])

print(f"Starting Equation: {weights[1]} * type + {weights[2]} * gpa + {weights[3]} * essay + {weights[4]} * rec + {weights[5]} * extra + {weights[0]}")

learning_rate = 0.0005
max_epoch = 10000
errorList = []
epochs = []
trainingOut_list = []
epoch = 0
while epoch < max_epoch:
    epoch += 1
    r = randint(0, len(type)-1)
    print(calculateOutput(weights, type[r], bedroom[r], bathroom[r], livingroom[r], diningroom[r], condition[r], area[r]))



#with open(f'./outputs/weights.txt', 'w') as f:
#    f.write("{}, {}, {}, {}, {}, {}".format(weights[0], weights[1], weights[2], weights[3], weights[4], weights[5]))

#with open(f'./outputs/errors.txt', 'w') as f:
#    for i in range(0, len(errorList)):
#        f.write(f"{errorList[i]}\n")

#with open(f'./outputs/training_output.txt', 'w') as f:
#    f.write(f"Initial Equation : {weights[1]}*s + {weights[2]}*g + {weights[3]}*e + {weights[4]}*r + {weights[5]}*c + {weights[0]} = 0\n\n")
#    for i in range(0, len(trainingOut_list)):
#        f.write(f"{trainingOut_list[i]}\n")
#    f.write(f"\nFinal Equation: {trainingOut_list[len(trainingOut_list)-1]}")


# plotting graph

# sns.set_theme(style="darkgrid")

# # setting up dataframe
# zipped = list(zip(errorList, epochs))
# df = pd.DataFrame(zipped, columns=['Error Rate', 'Iterations'])

# # More complicated, but more customizable appearance (seaborn)        
# g = sns.relplot(x="Error Rate", y="Iterations", kind="line", data=df)
# g.figure.autofmt_xdate()
# plt.show()

# #simple matplotlib
# plt.plot(epochs, errorList)
# plt.title('Error rate vs iterations')
# plt.xlabel('Iterations')
# plt.ylabel('Error rate (%)')
# plt.show()

