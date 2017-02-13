def acceleration(v1, v2, t1, t2):
    a = float(v2 - v1) / float(t2 - t1)
    return a

print(acceleration(0,10,0,20))

#If you were creating this in Python 2 the solution would need to have two float  functions converting the two differences to float numbers because if the differences are integers, Python will also output an integer (e.g. 3 / 2 outputs 0). In Python 3 you don't have to convert to floats.