# "E" : [Z,A,n]
Element = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Nh Fl Mc Lv Ts Og'
Element = Element.split(" ")
# print(Element)
# z = '1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99	100	101	102	103	104	105	106	107	108	109	110	111	112	113	114	115	116	117	118'
# z = z.replace(' ','')
# z = z.replace('	',',')
# z = [z]
z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118]
# print(z,type(z))
A = [1.008,4.003,6.94,9.01,10.8,12.01,14.01,16,19,20.18,22.99,24.31,26.98,28.09,30.97,32.07,35.45,39.95,39.1,40.08,44.96,47.87,50.94,52,54.94,55.85,58.93,58.69,63.55,65.39,69.72,72.64,74.92,78.96,79.90,83.79,85.47,87.62,88.91,91.22,92.91,95.96,98,101.1,102.9,106.4,107.9,112.4,114.8,118.7,121.8,127.6,126.9,131.3,132.9,137.3,138.9,140.1,140.9,144.2,145,150.4,152.0,157.2,158.9,162.5,164.9,167.3,168.9,173.0,175.0,178.5,180.9,183.9,186.2,190.2,192.2,195.1,197.0,200.5,204.38,207.2,209.0,209,210,222,223,226,227,232,231,238,237,244,243,247,247,247,252,257,258,259,262,267,268,271,272,277,276,281,280,277,284,289,288,293,296,294]
# print (A)
################################################################
# group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, group13, group14, group15, group16, group17, group18
group1 = {1,3,11,19,37,55,87}
group2 = {4,12,20,38,56,88}
group3 = {21,39,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103}
group4 = {22,40,72,104}
group5 = {23,41,73,105}
group6 = {24,42,74,106}
group7 = {25,43,75,107}
group8 = {26,44,76,108}
group9 = {27,45,77,109}
group10 = {28,46,78,110}
group11 = {29,47,79,111}
group12 = {30,48,80,112}
group13 = {5,13,31,49,81,113}
group14 = {6,14,32,50,82,114}
group15 = {7,15,33,51,83,115}
group16 = {8,16,34,52,84,116}
group17 = {9,17,35,53,85,117}
group18 = {2,10,18,36,54,86,118}

# period1 , period2 , period3 , period4 , period5 , period6 , period7
period1 = {1,2}
period2 = {3,4 ,5,6,7,8,9,10}
period3 = {11,12,13,14,15,16,17,18}
period4 = {19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36}
period5 = {37,38,39,40,41,41,42,43,44,45,46,47,48,49,50,51,52,53,54}
period6 = {55,56,57,58,59, 60, 61, 62, 63, 64, 65, 66 , 67, 68, 69, 70, 71, 72, 73, 74 , 75, 76, 77, 78, 79, 80, 81, 82 , 83, 84, 85, 86}
period7 = {87, 88, 89, 90 , 91, 92, 93, 94, 95, 96, 97, 98 , 99, 100, 101, 102, 103, 104 , 105, 106, 107, 108, 109, 110, 111 , 112 , 113 , 114 , 115 , 116 , 117 , 118}
# group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, group13, group14, group15, group16, group17, group18
Z = 27
g1 = Z in group1
g2 = Z in group2
g3 = Z in group3
g4 = Z in group4
g5 = Z in group5
g6 = Z in group6
g7 = Z in group7
g8 = Z in group8
g9 = Z in group9
g10 = Z in group10
g11 = Z in group11
g12 = Z in group12
g13 = Z in group13
g14 = Z in group14
g15 = Z in group15
g16 = Z in group16
g17 = Z in group17
g18 = Z in group18
if g1==True :
    print("this element in the group 1")
elif g2==True :
    print("this element in the group 2")
elif g3==True :
    print("this element in the group 3")
elif g4==True :
    print("this element in the group 4")
elif g5==True :
    print("this element in the group 5")
elif g6==True :
    print("this element in the group 6")
elif g7==True :
    print("this element in the group 7")
elif g8==True :
    print("this element in the group 8group8")
elif g9==True :
    print("this element in the group 9")
elif g10==True :
    print("this element in the group 10group10")
elif g11==True :
    print("this element in the group 11group11")
elif g12==True :
    print("this element in the group 12group12")
elif g13==True :
    print("this element in the group 13")
elif g14==True :
    print("this element in the group 14")
elif g15==True :
    print("this element in the group 15group15")
elif g16==True :
    print("this element in the group 16")
elif g17==True :
    print("this element in the group17")
elif g18==True :
    print("this element in the group18")

p1 = Z in period1
p2 = Z in period2
p3 = Z in period3
p4 = Z in period4
p5 = Z in period5
p6 = Z in period6
p7 = Z in period7

if p1 == True:
    print("thes element in the period1")
elif p2 == True:
    print("thes element in the period2")
elif p3 == True:
    print("thes element in the period3")
elif p4 == True:
    print("thes element in the period4")
elif p5 == True:
    print("thes element in the period5")
elif p6 == True:
    print("thes element in the period6")
elif p7 == True:
    print("thes element in the period7")





##############################################################

f = list(zip(z,A))
print(f)
