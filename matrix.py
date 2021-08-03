import unittest
class Matrix:
    def __init__(self, matrix,rows,col):
        self.mat=matrix
        self.rows=rows
        self.col=col
    def __repr__(self):
        a=""
        for x in range(0,self.rows):
            for y in range(0,self.col):
                a+=str(self.mat[x][y])+"  "
            a+="\n"
        return a
    def __add__(self,other):
        if(self.rows==other.rows and self.col==other.col):
            c=[]
            for x in range(0,self.rows):
                d=[]
                for y in range(0, self.col):
                    d.append(self.mat[x][y]+other.mat[x][y])
                c.append(d)
            e=Matrix(c,self.rows,self.col)
            return e
        else:
            return "NOT POSSIBLE"
    def __sub__(self,other):
        if(self.rows==other.rows and self.col==other.col):
            c=[]
            for x in range(0,self.rows):
                d=[]
                for y in range(0, self.col):
                    d.append(self.mat[x][y]-other.mat[x][y])
                c.append(d)
            e=Matrix(c,self.rows,self.col)
            return e
        else:
            return "NOT POSSIBLE"
    def __mul__(self,other):
        if(self.col!=other.rows):
            return "NOT POSSIBLE"
        else:
            c=[]
            for x in range(0, self.rows):
                d=[]
                for y in range(0, other.col):
                    e=0
                    for z in range(0, self.col):
                        e+=self.mat[x][z]*other.mat[z][y]
                    d.append(e)
                c.append(d)
            a=Matrix(c,self.rows,other.col)
            return a
    def exponent(self, n):
        if(self.col!=self.rows):
            return "NOT POSSIBLE"
        else:
            c=self.mat
            for x1 in range(0,n-1):
                c1=[]
                for x in range(0, self.rows):
                    d=[]
                    for y in range(0, len(c)):
                        e=0
                        for z in range(0, self.col):
                            e+=self.mat[x][z]*c[z][y]
                        d.append(e)
                    c1.append(d)
                c=c1
            a=Matrix(c,self.rows,self.rows)
            return a
    def determinant(self,a):
        if(self.col!=self.rows):
            return "NOT POSSIBLE"
        else:
            x=0
            if len(a)==1:
                return a[0][0]
            else:
                for d in range(0,len(a)):   
                    if(d==0):
                        c=[]
                        for y in range(1,len(a)):
                            c.append(a[y][1:])
                        x+=((-1)**d)*a[0][d]*self.determinant(c)
                    elif(d==len(a)-1):
                        c=[]
                        for y in range(1,len(a)):
                            c.append(a[y][0:len(a)-1])
                        x+=((-1)**d)*a[0][d]*self.determinant(c)
                    else:
                        c=[]
                        for y in range(1,len(a)):
                            c.append(a[y][0:d]+a[y][d+1:])
                        x+=((-1)**d)*a[0][d]*self.determinant(c)             
            return x   
#a=Matrix([[14,30,3],[5,8,5]],2,3)
#b=Matrix([[2,3,4],[5,6,7]],2,3)
#c=Matrix([[1,2],[3,4],[5,6]],3,2)
#d=Matrix([[1,4,2,6],[0,1,4,4],[-1,0,1,0],[2,0,4,1]],4,4)
#print(a-b)
#print(a+b)
#print(a+d)
#print(a*c)
#print(c*a)
#print(c*d)
#print(d.determinant(d.mat))
#print(c.determinant(c.mat))
#print(d.exponent(3))
#print(c.exponent(3))
class LearnTest(unittest.TestCase):
    def setUp(self):
        self.a=Matrix([[14,30,3],[5,8,5]],2,3)
        self.b=Matrix([[2,3,4],[5,6,7]],2,3)
        self.c=Matrix([[1,2],[3,4],[5,6]],3,2)
        self.d=Matrix([[1,4,2,6],[0,1,4,4],[-1,0,1,0],[2,0,4,1]],4,4)
    def test_func_1(self):
        result=self.a-self.b
        result1 = Matrix([[12,27,-1],[0,2,-2]],2,3)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_func_2(self):
        result=self.a+self.b
        result1 = Matrix([[16,33,7],[10,14,12]],2,3)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_func_3(self):
        result=self.a+self.d
        result1 = "NOT POSSIBLE"
        self.assertEqual(result,result1)
    def test_func_4(self):
        result=self.a*self.c
        result1 = Matrix([[119,166],[54,72]],2,2)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_func_5(self):
        result=self.c*self.a
        result1 = Matrix([[24,46,13],[62,122,29],[100,198,45]],3,3)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_func_6(self):
        result=self.c*self.d
        result1 = "NOT POSSIBLE"
        self.assertEqual(result,result1)
    def test_func_7(self):
        result=self.d.determinant(self.d.mat)
        result1 = 47
        self.assertEqual(result,result1)
    def test_func_8(self):
        result=self.c.determinant(self.c.mat)
        result1 = "NOT POSSIBLE"
        self.assertEqual(result,result1)
    def test_func_9(self):
        result=self.d.exponent(3)
        result1 = Matrix([[23,52,210,126],[-4,17,68,36],[-13,-12,-45,-34],[14,8,96,45]],4,4)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_func_10(self):
        result=self.c.exponent(3)
        result1 = "NOT POSSIBLE"
        self.assertEqual(result,result1)
if __name__=="__main__":
    unittest.main()