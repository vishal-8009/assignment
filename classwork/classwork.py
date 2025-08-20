class student:
    def __init__(self):
        print("__init__")
    def __new__(cls):
        print("__new__")
        obj = object.__new__(cls)
        return obj
    def __del__(self):
        print("__del__")

student()
input




class student:
    def __init__(self):
        self.name = "vishal gupta"
        self.branch = "cse"


st=student()
print(st.name)
print(st.branch)        


