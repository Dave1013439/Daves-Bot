import os

def runModule(name: str):
    if name + ".py" in os.listdir(os.path.join(os.getcwd(), "modules")):
        exec(open(os.path.join(os.getcwd(), f"modules/{name}.py"), "r").read())