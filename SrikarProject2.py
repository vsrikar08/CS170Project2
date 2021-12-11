import math
import copy
import numpy as np
import random

  #data_type = input('Enter in if you want large or small data set:' )
  #print(data_type)
 # if(data_type=="large"):
 #   data_file = open("Ver_2_CS170_Fall_2021_LARGE_data__35.txt", "r")
 # elif (data_type=="small"):
 #   data_file = open("Ver_2_CS170_Fall_2021_Small_data__98.txt", "r")
 # else:
  #  print("Invalid input program crashing")
   # exit(1)


def forwardSelection(data):
  feature_list=[] #list for which features are best
  testing_list=[] # list for testing new features
  #now colums are features while row is the qualifications and stuff for each thing
  depthAccuracy=0.0
  potential_feature=0
  currentAccuracy=0.0
  maxAccuracy=0.0
  # we don't want to count the first row which is the label
  for i in range(1,len(data[0])):
    print("Current depth of tree is:", i )
    depthAccuracy=0.0
    potential_feature=0
    for k in range(1,len(data[0])):
      if(k not in testing_list):
        currentAccuracy=0.0
        print("looking at feature: ", k)
        temp_testing_list=testing_list.copy()
        temp_testing_list.append(k)
        #can't use float call
        currentAccuracy=float(accuracy(data,temp_testing_list, k))
        print("Current Accuracy: ", currentAccuracy)
        #replaced max_accuracy with depth accuracy because max accuracy was the overall thing
        if(currentAccuracy > depthAccuracy):
          depthAccuracy=currentAccuracy
          #should not append to list here because then it could be replace
          potential_feature=k
    testing_list.append(potential_feature)
    print("Current testing list: ", testing_list)
    #back to level
    print("Best feature on this level: ", potential_feature)
    print("Best accuracy on this level: ", depthAccuracy)
    if(depthAccuracy > maxAccuracy):
      #using copy is better according to Giang
      feature_list.append(potential_feature)
      maxAccuracy=depthAccuracy
    else:
      print("Accuracy is going lower, going to continue till end though")
    print("Best accuracy in total: ", maxAccuracy)
    print("Current best set to use: ", testing_list)
  print("Done with forwardSelection. The best feature is {0} with accuracy of {1}%." .format(feature_list, maxAccuracy*100))  
   
       





def backwardElimination(data):
  #we don't know length of list so we need to populate it based on data set
  feature_list=[]
  for i in range (1,len(data[1])):
    feature_list.append(i)
  testing_list=[]
  testing_list=copy.deepcopy(feature_list)
  #print ("Feature list: ", feature_list)
  #print ("testing list: ", testing_list)
  depthAccuracy=0.0
  remove_feature=0
  currentAccuracy=0.0
  maxAccuracy=0.0
  all_accuracy=0.0
  all_accuracy=float(accuracy(data,testing_list, 0))
  print("Accuracy for all numbers in list: ", all_accuracy)
  for i in range(1,len(data[0])):
    print("Current depth of tree is:", i )
    depthAccuracy=0.0
    remove_feature=0
    for k in range(1,len(data[0])):
      #we want it to be in testing list for it to be there 
      if(k in testing_list):
        print("looking at feature: ", k)
        temp_testing_list=testing_list.copy()
        temp_testing_list.remove(k)
        currentAccuracy=float(accuracy(data,temp_testing_list, k))
        print("Current Accuracy: ", currentAccuracy)
        if(currentAccuracy > depthAccuracy):
          depthAccuracy=currentAccuracy
          remove_feature=k
    testing_list.remove(remove_feature)
    print("Best feature to remove on this level: ", remove_feature)
    print("Best accuracy on this level: ", depthAccuracy)
    if(depthAccuracy >= maxAccuracy):
      feature_list.remove(remove_feature)
      maxAccuracy=depthAccuracy
    else:
      print("Accuracy is going lower, going to continue till all elements are done ")
    print("Best accuracy in total: ", maxAccuracy)
    print("Current feature best set to use: ", feature_list)
  print("Done with backwardElimination. The best feature is {0} with accuracy of {1}%." .format(feature_list, maxAccuracy*100))  

def accuracy(data, testing_list, feature):
  # we don't wantto append or change the origianl file

  print("List to test: ", testing_list)
  correctly_classified=0
  #we want to find out how many data points are as close to each other as possible
  for i in range (len(data)):
    #first row whether male or female
    label= data[i][0]
    nearest_label=0
    #print("Menschen ")
    #need to assign apparently to compare
    #for element in data:
     # obj1=data[i][element]
    obj1=[]
    for element in testing_list:
      obj1.append(data[i][element])
    #print obj1
    nearest_neighbor_distance=math.inf
    nearest_neighbor_location=math.inf
    for k in range (len(data)):
      distance=0 
      if(i!=k):
        obj2=[]
        for other_element in testing_list:
          obj2.append(data[k][other_element])
        #print (len(testing_list_2))
        #print (len(obj1))
        #print ("Obj1: ", obj1)
        #print ("Obj2: ", obj2)
        #time to find distance
        for j in range (0,len(obj1)):
          distance+= (obj1[j]-obj2[j])**2
        #sum of distances squared
        distance=math.sqrt(distance)
        if(distance<nearest_neighbor_distance):
          nearest_neighbor_distance=distance
          nearest_neighbor_location=k
          nearest_label=data[nearest_neighbor_location][0] 
    
    if(label==nearest_label):
      correctly_classified=correctly_classified+1
  
  ret_value=(correctly_classified/len(data))
  return ret_value  

def main():
  #choose data set
  data_type = input('Enter in if you want large or small data set: ' )
  #print(data_type)
  if(data_type=="large"):
    data_file = open("Ver_2_CS170_Fall_2021_LARGE_data__35.txt", "r")
  elif (data_type=="small"):
    data_file = open("Ver_2_CS170_Fall_2021_Small_data__98.txt", "r")
  else:
    print("Invalid input program crashing")
    exit(1)
   
 # data_lines=data_file.readlines()
  #for line in data_lines:
  #  print(line) its working lol
  data_list=[]
  
  #now we want to turn them into numbers we can actually understand
  for line in data_file:
    lines= line.strip()
    ListRow = [float(f) for f in lines.split()]
    data_list.append(ListRow)
  data_file.close()
  #for index in data_list:
  #  print (index) 
  #data_size=len(data_list[1])
  #print(data_size)
  #select algorithm
  destinèe=int(input("Choose what algorithm you want, press 1 for forward selection, press 2 for backward selection: "))
 
  if(destinèe==1):
    #do forward selection
    print("Forward Selection")
    forwardSelection(data_list)
  elif( destinèe==2):
    #do backward selection
    print("Backward Selection")
    backwardElimination(data_list)
  else:
    print("British")
    exit(1)
main()


