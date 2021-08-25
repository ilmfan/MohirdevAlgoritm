import math
def tub_sonlar(n, k):
	output_list = []
	for i in range(n, k):
		b = True
		a = round(math.sqrt(i))
		j = 2
		while b and j <= a:
			if i % j == 0:
				b = False
			else:
				j += 1
		if b:
			output_list.append(i)
	return output_list
