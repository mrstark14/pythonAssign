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
            raise Exception("Order of two matrices different")
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
            raise Exception("Order of two matrices different")
    def __mul__(self,other):
        if(self.col!=other.rows):
            raise Exception("Invalid operation")
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
            raise Exception("NOT A SQUARE MATRIX")
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
    def determinant(self):
        if(self.col!=self.rows):
            raise Exception("NOT A SQUARE MATRIX")
        else:
            x=0
            if len(self.mat)==1:
                return self.mat[0][0]
            else:
                for d in range(0,len(self.mat)):   
                    if(d==0):
                        c=[]
                        for y in range(1,len(self.mat)):
                            c.append(self.mat[y][1:])
                        c1=Matrix(c,self.rows-1,self.col-1)
                        x+=((-1)**d)*self.mat[0][d]*c1.determinant()
                    elif(d==len(self.mat)-1):
                        c=[]
                        for y in range(1,len(self.mat)):
                            c.append(self.mat[y][0:len(self.mat)-1])
                        c1=Matrix(c,self.rows-1,self.col-1)
                        x+=((-1)**d)*self.mat[0][d]*c1.determinant()
                    else:
                        c=[]
                        for y in range(1,len(self.mat)):
                            c.append(self.mat[y][0:d]+self.mat[y][d+1:])
                        c1=Matrix(c,self.rows-1,self.col-1)
                        x+=((-1)**d)*self.mat[0][d]*c1.determinant()             
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
#print(d.determinant())
#print(c.determinant())
#print(d.exponent(3))
#print(c.exponent(3))
class LearnTest(unittest.TestCase):
    def setUp(self):
        self.a=Matrix([[14,30,3],[5,8,5]],2,3)
        self.b=Matrix([[2,3,4],[5,6,7]],2,3)
        self.c=Matrix([[1,2],[3,4],[5,6]],3,2)
        self.d=Matrix([[1,4,2,6],[0,1,4,4],[-1,0,1,0],[2,0,4,1]],4,4)
    def test_sub_1(self):
        result=self.a-self.b
        result1 = Matrix([[12,27,-1],[0,2,-2]],2,3)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_add_1(self):
        result=self.a+self.b
        result1 = Matrix([[16,33,7],[10,14,12]],2,3)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_mul_1(self):
        result=self.a*self.c
        result1 = Matrix([[119,166],[54,72]],2,2)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_mul_2(self):
        result=self.c*self.a
        result1 = Matrix([[24,46,13],[62,122,29],[100,198,45]],3,3)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_det_1(self):
        result=self.d.determinant()
        result1 = 47
        self.assertEqual(result,result1)
    def test_exp_1(self):
        result=self.d.exponent(3)
        result1 = Matrix([[23,52,210,126],[-4,17,68,36],[-13,-12,-45,-34],[14,8,96,45]],4,4)
        self.assertEqual(result.__repr__(),result1.__repr__())
    def test_det_2(self):
        result=self.c.determinant()
    def test_mul_3(self):
        result=self.a*self.d
    def test_add_2(self):
        result=self.a+self.d
    def test_exp_2(self):
        result=self.c.exponent(3)
    def test_sub_2(self):
        result=self.a-self.d
if __name__=="__main__":
    unittest.main()