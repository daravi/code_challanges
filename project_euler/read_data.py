def read_int_grid_data(path):
    
    with open(path) as f:
        grid_data = [i.split() for i in f.readlines()]
    
    new_grid_data = grid_data
    
    for row in range(len(grid_data)):
        for col in range(len(grid_data[row])):
            new_grid_data[row][col] = int(grid_data[row][col])
    
    return new_grid_data
    
grid = read_int_grid_data('/Users/daravi/Google Drive/1 Academic/3 Other/Project Euler/data.txt')
for line in grid:
    print line