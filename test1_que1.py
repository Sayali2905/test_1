lenght = int(input("Enter the lenght: "))
breadth = int(input("Enter the breadth: "))
radius = int(input("Enter the radius "))


area_of_rectangle = lenght * breadth
perimeter_of_rectangle = 2 * (lenght + breadth)


area_of_circle = 3.14 * radius ** 2
perimeter_of_circle = 2 * 3.14 * radius

total_area = area_of_rectangle + area_of_circle

total_perimeter = perimeter_of_rectangle + perimeter_of_circle

print(f'Area = {total_area}')
print(f'Perimeter = {total_perimeter}')