#Calculate the distance in kilometers between jupiter and sun on january 1, 1230


#This solution required some internet research to find out about the ephem library
import ephem

jupiter = ephem.jupiter()
jupiter.computer('1230/1/1')
distance_au_units = jupiter.sun_distance
distance_km = distance_au_units * 149597870.691
print(distance_km)
