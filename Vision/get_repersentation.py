#cv algorithm
# ex: corners
# loop through positions in grid array of cube that we know are corners.
# at the start, we know the corner position we are looking at
# we look at the three sides in that corner to see their colors in order to detrermine which cubelet number it is
# ex: we are looking at corner position 5. We see White blue orange = 'WBG'. We look in our dictionary to find that that string (order insensitive) is corner number 2
# for the State object as defined in 01_rubic/libcube/cubes/cube3x3.py, set corner_pos[5] = 2