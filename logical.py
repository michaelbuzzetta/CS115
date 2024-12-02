def f(x,y,z):
    return (not x and not y and y)\
            or (not x and y and not z)\
            or (x and not y and not z)\
            or (x and y and not z)\
            or (x and y and z)

def test_f():
    assert(f(0,0,0))==0
