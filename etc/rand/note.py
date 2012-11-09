#!/usr/bin/env python
m1 = {'2':96, '3':32, '4':69, '5':40, '6':148, '7':104, '8':152, '9':119, '10':98, '11':3, '12':54}
m2 = {'2':22, '3':6, '4':95, '5':17, '6':74, '7':157, '8':60, '9':84, '10':142, '11':87, '12':130}
m3 = {'2':141, '3':128, '4':158, '5':113, '6':163, '7':27, '8':171, '9':114, '10':42, '11':165, '12':10}
m4 = {'2':41, '3':63, '4':13, '5':85, '6':45, '7':167, '8':53, '9':50, '10':156, '11':61, '12':103}
m5 = {'2':105, '3':146, '4':153, '5':161, '6':80, '7':154, '8':99, '9':140, '10':75, '11':135, '12':28}
m6 = {'2':122, '3':46, '4':55, '5':2, '6':97, '7':68, '8':133, '9':86, '10':129, '11':47, '12':106}
m7 = {'2':11, '3':134, '4':110, '5':159, '6':36, '7':118, '8':21, '9':169, '10':62, '11':147, '12':106}
m8 = {'2':30, '3':81, '4':24, '5':100, '6':107, '7':91, '8':127, '9':94, '10':123, '11':33, '12':5}
m9 = {'2':70, '3':117, '4':66, '5':90, '6':25, '7':138, '8':16, '9':120, '10':65, '11':102, '12':35}
m10 = {'2':121, '3':39, '4':139, '5':176, '6':143, '7':71, '8':155, '9':88, '10':77, '11':4, '12':20}
m11 = {'2':26, '3':126, '4':15, '5':7, '6':64, '7':150, '8':57, '9':48, '10':19, '11':31, '12':108}
m12 = {'2':9, '3':56, '4':132, '5':34, '6':125, '7':29, '8':175, '9':166, '10':82, '11':164, '12':92}
m13 = {'2':112, '3':174, '4':73, '5':67, '6':76, '7':101, '8':43, '9':51, '10':137, '11':144, '12':12}
m14 = {'2':49, '3':18, '4':58, '5':160, '6':136, '7':162, '8':168, '9':115, '10':38, '11':59, '12':124}
m15 = {'2':109, '3':116, '4':145, '5':52, '6':1, '7':23, '8':89, '9':72, '10':149, '11':173, '12':44}
m16 = {'2':14, '3':83, '4':79, '5':170, '6':93, '7':151, '8':172, '9':111, '10':8, '11':78, '12':131}

measureHead = """
/*
 * Measure {0}
 */
"""

def print_properly(map, i):
	print(  measureHead.format(i) )
	print( "measureMap = measureMapList.get({0});".format(i-1) )
	for i in range( 2, 13):
		print( "measureMap.put({0}, {1});".format(i, map[str(i)]) )

print_properly(m1, 1)
print_properly(m2, 2)
print_properly(m3, 3)
print_properly(m4, 4)
print_properly(m5, 5)
print_properly(m6, 6)
print_properly(m7, 7)
print_properly(m8, 8)
print_properly(m9, 9)
print_properly(m10, 10)
print_properly(m11, 11)
print_properly(m12, 12)
print_properly(m13, 13)
print_properly(m14, 14)
print_properly(m15, 15)
print_properly(m16, 16)



