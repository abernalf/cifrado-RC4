# -*- coding: utf-8 -*-
def in_clave():
	w = input("------Introduzca la clave: ")
	w = w.split(',')
	return w


def generate_s():
	vector = [0]
	for i in range(1,256):
		vector += [i];
	return vector
def generate_v(clave,tam):
	z = 1;
	vector = [clave[0]]
	for i in range(1,tam):
		#print ("I: "+str(i))
		#print ("Z :"+str(z))
		if z < len(clave):
			vector += [clave[z]]
			z = z+1
		else:
			z = 0;
			vector += [clave[z]]
			z = z+1
	return vector	
	#print (len(vector))



def generate():
	vector_s = generate_s();
	clave = in_clave();
	vector_c = generate_v(clave,len(vector_s))
	print (vector_s)
	print("-------------------")
	print (vector_c)
	
w = 's'
while w == 's':
	generate();

	print("-----------------------------------------------");
	
	w = input("----¿DESEA REALIZAR OTRA OPERACIÓN?[s/n]----");