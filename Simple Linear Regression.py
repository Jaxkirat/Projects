import matplotlib.pyplot as plt 
from scipy import stats

x = [2, 5, 6, 7, 8, 2, 1, 4 ,5 ,6] 
y = [9,2,3,4,5,4,2,5,6,7]

plt.scatter(x,y)       ####plots the given data points

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)    ###calculates necesarry information to predict further information  

def y_predict(x):
    return slope*x + intercept                        ###funaction that predicts a data point based on the trend/data input by the user


print(y_predict(4))                                  ###test to check predicted value

u= list(map(y_predict,x))                            ###maps predicted and given data into lists


print(u)                                             

plt.plot(x,u)                                        ### plots the prediction line on the graph
