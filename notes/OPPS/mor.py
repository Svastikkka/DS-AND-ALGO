class X: pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class C(B,A,Y):pass
print(C.mro())   # print MRO for class C
#[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
