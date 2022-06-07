import turtle as tt
turtle = tt.Turtle()

edges = int(input("ENTER NUMBER OF SIDES OF THE POLYGON"))
if edges >=3:
    for i in range(edges):
        inangle = 180-((edges-2)*180/edges)
        turtle.left(inangle)
        turtle.forward(100)
    input() # waiting for input
else:
    print("side number must equal or greater than 3")
