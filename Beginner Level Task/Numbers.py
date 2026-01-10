print("================================================================")
print("1: Function to format a number")
def format_number(num, fmt):
    return format(num, fmt)

result = format_number(145, 'o')
print("Formatted result (octal):", result)

print("================================================================")

print("2: Area of a circular pond and total amount of water")
radius = 84
pi = 3.14

area = pi * radius ** 2
print("Area of pond:", int(area))  

water_per_sq_meter = 1.4
total_water = area * water_per_sq_meter
print("Total water in the pond (liters):", int(total_water)) 

print("=================================================================")

print("3: Speed calculation")
distance = 490          
time_minutes = 7
time_seconds = time_minutes * 60  

speed = distance / time_seconds
print("Speed in meters per second:", int(speed))  
print("================================================================")
