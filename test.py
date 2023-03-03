
def var_name(var):
    for name, value in globals().items():
        if value is var:
            return name

prout = "test"

print(var_name(prout))

if 0 in [0,13]:
    print("ok")
else:
    print("non")