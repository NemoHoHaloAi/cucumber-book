import os,sys,random,math,time

import numpy

import matplotlib.pyplot as plt

'''
原型聚类：k_means
'''

data = [line[:-1].split(",") for line in open("watermelon_4.csv").readlines()]

plt.scatter([float(row[1]) for row in data if row[3]=="1"],[float(row[2]) for row in data if row[3]=="1"],color = "g")
plt.scatter([float(row[1]) for row in data if row[3]=="0"],[float(row[2]) for row in data if row[3]=="0"],color = "r")
plt.show()

data = [[float(row[1]),float(row[2])] for row in data]
print(data)

k = 2
clusters = [[data[i]] for i in random.sample(range(len(data)),k=k)]
cluster_centers = [[sum([row[0] for row in cluster])/len(cluster),sum([row[1] for row in cluster])/len(cluster)]for cluster in clusters]
print(cluster_centers)
print(clusters)

def min_distance(cluster_centers,point):
    min_idx = 0
    min_dist = 9999
    for idx,center in enumerate(cluster_centers):
        dist = float((((center[0]-point[0])**2)+((center[1]-point[1])**2))**0.5)
        if dist < min_dist:
            min_idx = idx
            min_dist = dist
    return min_idx,min_dist

for i in range(1000):
    clusters = [[] for i in range(k)]
    for row in data:
        min_idx,min_dist = min_distance(cluster_centers,row)
        clusters[min_idx].append(row)
    cluster_centers = [[sum([row[0] for row in cluster])/len(cluster),sum([row[1] for row in cluster])/len(cluster)]for cluster in clusters]

print(cluster_centers)
print(clusters)

for cluster in clusters:
    plt.scatter([row[0] for row in cluster],[row[1] for row in cluster])

plt.show()
