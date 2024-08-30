earth_weight = input("what is youre weight on earth")

#Input is currently a string, make sure to clean it up

earth_weight = float(earth_weight)

earth_gravity = 9.807
moon_gravity = 1.622

moon_weight = earth_weight / earth_gravity * moon_gravity

print(f"(your weight on da moon is {moon_weight})")

