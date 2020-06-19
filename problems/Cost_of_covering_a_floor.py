def cost_of_tile():
	price = int(input('What is the cost of each tile? '))
	area = int(input('What is the total area to be covered? '))
	tile_area = int(input('What is the area of each tile? '))
	cost = area / tile_area * price
	return cost

print(cost_of_tile())