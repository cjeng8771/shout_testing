##### Using Measurements to Calcuate Error in Local Clock Time for Nodes #####

####################
# IMPORT LIBRARIES #
####################

import numpy as np
from colorama import Fore, Style

####################
# DEFINE FUNCTIONS #
####################

def find_e_vector(col_num, links):
    file_name = "col_" + str(col_num) + ".txt"
    d = 0
    delta = np.zeros((len(links),1))

    with open(file_name,'r') as f:
        vals = f.readlines()
    
    for val in vals:
        val = val.replace(",\n", "")
        delta[d] = (int(val))
        d += 1
    
    estimate = np.dot(pinvA, delta)

    e_est = estimate[:len(rx_names)]
    T_est = estimate[len(rx_names):]
    return e_est, T_est

def print_results(col_num, rx_names, e_est, T_est):
    print(" ---------- column (repNum) " + str(col_num) + " in delta.txt ---------- ")
    print(Fore.RED + "(~, rx_name ) -----    e_estimate    -----   T_estimate" + Style.RESET_ALL)
    r = 0

    for rx in rx_names:
        rx_temp = rx
        if len(rx) != len("browning"):
            for i in range(len("browning")-len(rx)):
                rx_temp += " "
        if e_est[r][0] < 0 or T_est[r][0] < 0:
            print("(~, " + rx_temp + ") -----  [" + format(e_est[r][0],'.7f') + "]  ----- [" + 
                  format(T_est[r][0],'.7f') + ']')
        else:
            print("(~, " + rx_temp + ") -----  [" + format(e_est[r][0],'.8f') + "]  ----- [" + 
                  format(T_est[r][0],'.8f') + ']')
        r += 1

####################
# SETTING UP LINKS #
####################

rx_names = ["bes","browning","fm","honors","hospital","smt","ustar"]
links_names = ["bes-browning","bes-fm","bes-honors","bes-hospital","bes-smt","bes-ustar",
         "browning-bes","browning-fm","browning-honors","browning-hospital","browning-smt","browning-ustar",
         "fm-bes","fm-browning","fm-honors","fm-hospital","fm-smt","fm-ustar",
         "honors-bes","honors-browning","honors-fm","honors-hospital","honors-smt","honors-ustar",
         "hospital-bes","hospital-browning","hospital-fm","hospital-honors","hospital-smt","hospital-ustar",
         "smt-bes","smt-browning","smt-fm","smt-honors","smt-hospital","smt-ustar",
         "ustar-bes","ustar-browning","ustar-fm","ustar-honors","ustar-hospital","ustar-smt"]
links = []

for pair in links_names:
    pair = pair.split("-")
    links.append(pair)
    # print(pair)

print(" ----- all node links ----- ")
print(links)

####################
# SETTING UP A     #
####################

A = np.zeros((len(links),2*len(rx_names)))

# delta is a vector of the sample number of the start of the sync in the recieved signal
link_num = 0
for link in links:
    # each link is a (tx_name, rx_name)
    tx_num = rx_names.index(link[0])
    rx_num = rx_names.index(link[1])
    A[link_num,tx_num] = 1
    A[link_num,len(rx_names)+tx_num] = 1
    A[link_num,rx_num] = -1
    A[link_num,len(rx_names)+tx_num]
    link_num += 1

print(" ----- A matrix ----- ")
print(A)

####################
# FIND PEUSDO-INV  #
####################

pinvA = np.linalg.pinv(A)

print(" ----- peusdoinverse A ----- ")
print(pinvA)

####################
# DELTA FOR REPNUM #
####################

col_num = 1
file_name = "col_" + str(col_num) + ".txt"
d = 0
delta = np.zeros((len(links),1))

with open(file_name,'r') as f:
    vals = f.readlines()
    
for val in vals:
    val = val.replace(",\n", "")
    delta[d] = (int(val))
    d += 1

print(" ----- delta vector from measurements ----- ")
print(delta)

####################
# A MULTIPLICATION #
####################

estimate = np.dot(pinvA, delta)

print("Output of Shape: " + str(estimate.shape) + '\n')
print(" ----- estimate vector ----- ")
print(estimate)

####################
# GETTING ESTIMATE #
####################

e_est = estimate[:len(rx_names)]
T_est = estimate[len(rx_names):]

print(" ----- e_estimate ----- ")
print(e_est)
print(" ----- T_estimate ----- ")
print(T_est)

####################
# PRINTING RESULTS #
####################

print(" ---------- column (repNum) 1 in delta.txt ---------- ")
print(Fore.RED + "(~, rx_name ) -----    e_estimate    -----   T_estimate" + Style.RESET_ALL)
r = 0

for rx in rx_names:
    rx_temp = rx
    if len(rx) != len("browning"):
        for i in range(len("browning")-len(rx)):
            rx_temp += " "
    if e_est[r][0] < 0 or T_est[r][0] < 0:
        print("(~, " + rx_temp + ") -----  [" + format(e_est[r][0],'.7f') + "]  ----- [" + 
              format(T_est[r][0],'.7f') + ']')
    else:
        print("(~, " + rx_temp + ") -----  [" + format(e_est[r][0],'.8f') + "]  ----- [" + 
              format(T_est[r][0],'.8f') + ']')
    r += 1

####################
# RUNNING ALL COLS #
####################

e_est_1, T_est_1 = find_e_vector(1,links)
e_est_2, T_est_2 = find_e_vector(2,links)
e_est_3, T_est_3 = find_e_vector(3,links)
e_est_4, T_est_4 = find_e_vector(4,links)

####################
# PRINTING COLS    #
####################

print_results(1, rx_names, e_est_1, T_est_1)
print('\n ------------------------------ \n')

print_results(2, rx_names, e_est_2, T_est_2)
print('\n ------------------------------ \n')

print_results(3, rx_names, e_est_3, T_est_3)
print('\n ------------------------------ \n')

print_results(4, rx_names, e_est_4, T_est_4)
print('\n ------------------------------ \n')