def tree(height:int=5, char:str="*", file:str=None):
    if len(char) != 1: raise Exception("The lenght of a char must be 1.")
    if height > 1:
        end = ""
        for i in range(1, height+1):
            end+=(str((i+i-1)*char).center(height*2-1))+"\n"
        for i in range(height//4):
            end+=(str((height//4)*char).center(height*2-1))+"\n"
        if not height//4:end+=(char.center(height*2-1))+"\n"
        if file:
            with open(file, "w") as doc: doc.write(end)
        return end
    else: raise Exception(f"A tree with a heigth of {height} is not a tree...")

def triangle(height:int=5, char:str="*", file:str=None):
    if len(char) != 1: raise Exception("The lenght of a char must be 1.")
    if height > 1:
        end = ""
        for i in range(1, height+1):
            end+=(str((i+i-1)*char).center(height*2-1))+"\n"
        if file:
            with open(file, "w") as doc: doc.write(end)
        return end
    else: raise Exception(f"A tree with a heigth of {height} is not a triangle...")

def square(height:int=5, char:str="*", file:str=None, scale:bool=True):
    end=""
    for i in range(height//(2 if scale else 1)):
        end+=(height*char)+"\n"
    if file:
        with open(file, "w") as doc: doc.write(end)
    return end
