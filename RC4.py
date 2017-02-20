# -*- coding: utf-8 -*-
def in_clave():
	w = input("------Introduzca la clave: ")
	w = w.split(',')
	return w

def in_data():
	w = input("------Introduzca el valor a cifrar/descifrar: ")
	w = w.split(',')
	return w
def des_binarizar(numero):
	return int(str(numero),2)
	int(bin(25)[2:])

def binarizar(numero):
	return "%08d" % int(bin(numero)[2:])

def generate_s():
	vector = [0]
	for i in range(1,256):
		vector += [i];
	return vector
def mostrar(palabra):
	print ("El resultado en decimarl es: ")
	print (palabra)
	print ("El resultado en binario es: ")
	for i in range(0,len(palabra)):
		palabra[i] = binarizar(palabra[i])
	print (palabra)
	
	



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
def prga(clave_s):
	i = 0
	f = 0
	k = 0
	j = 0
	data = in_data()
	while k < len(data):
		i = (i + 1)%256
		j = (j + clave_s[i])%256
		aux = clave_s[j]
		clave_s[j] = clave_s[i]
		clave_s[i] = aux
		t = (clave_s[i]+clave_s[j])%256
		if k == 0:
			sol = [clave_s[t]]
		else:
			sol += [clave_s[t]]
		k = k+1
	#print(int(data[0]) ^ int(sol[0]))
	res = [int(data[0]) ^ int(sol[0])]
	for i in range(1,len(sol)):
		#print(int(data[i]) ^ int(sol[i]))
		res += [int(data[i]) ^ int(sol[i])]
	mostrar(res)


def generate():
	vector_s = generate_s();
	clave = in_clave();
	vector_c = generate_v(clave,len(vector_s))
	f = 0
	for i in range(0,256):
		f = (f + int(vector_s[i]) + int(vector_c[i])) % 256;
		aux = vector_s[f]
		vector_s[f] = vector_s[i]
		vector_s[i] = aux
	print(vector_s)
	print(vector_c)
	prga_ = prga(vector_s)
#for i = 0 to 255{
#f = (f + S[i] + K[i]) mod 256;
#intercambia S[i] y S[f];}
	
w = 's'
while w == 's':
	generate();
	

	print("-----------------------------------------------");
	
	w = input("----¿DESEA REALIZAR OTRA OPERACIÓN?[s/n]----");