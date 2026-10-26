area = int(input("Enter area of one wall:"))

interior_cost = int(input("Enter interior cost: "))
exterior_cost = int(input("Enter exterior cost:"))

interior_total_cost = area * interior_cost
exterior_total_cost = area * exterior_cost

total_cost = interior_total_cost + exterior_total_cost

print(f'Interior Painting Cost = {interior_total_cost}')
print(f'Exterior Painting Cost = {exterior_total_cost}')
print(f'Total Printing Cost = {total_cost}')