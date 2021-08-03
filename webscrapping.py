import unittest
class Person:
    def __init__(self, name, work=None, city='Roorkee'):
        self.name = name
        self.city = city
        if(work!=None):
            self.work = work
    def show(self):
        return "My name is "+self.name+" and my current city is "+self.city+"."
def decorator(func):
    def wrapper(i):
        c=0
        import mysql.connector
        mydb = mysql.connector.connect(host='localhost',database='img', user='mrstark', password='Sanjeet@2001')
        mycursor = mydb.cursor()
        sql = "SELECT * FROM user WHERE username = '"+i+"'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            c+=1 
        if(c>0):
            return func(i)
        else:
            return "Username is not in database"
    return wrapper
@decorator
def scrap(username):
    from selenium import webdriver
    from time import sleep
    #from webdriver_manager.firefox import ChromeDriverManager
    from selenium.webdriver.firefox.options import Options 
    from getpass import getpass
    from bs4 import BeautifulSoup
    usr=input('Enter Email Id:')
    pwd = getpass('Enter Password:')    
    driver = webdriver.Firefox()
    driver.get('https://m.facebook.com/')
    #print ("Opened facebook")
    sleep(1)
    
    username_box = driver.find_element_by_id('m_login_email')
    username_box.send_keys(usr)
    #print ("Email Id entered")
    sleep(1)
    
    password_box = driver.find_element_by_id('m_login_password')
    password_box.send_keys(pwd)
    #print ("Password entered")
    
    login_box = driver.find_element_by_name('login')
    login_box.click()
    
    #print ("Done")
    sleep(5)
    driver.get('https://m.facebook.com/'+username+'/about')
    next_value = 300
    while next_value<3000: 
        #driver.execute_script("next_value="+next_value";")
        driver.execute_script("window.scrollBy(0,"+str(next_value)+")")
        next_value+=300
        sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    #print(soup.prettify())
    table = soup.find('title')
    naam=table.text
    #current city
    table = soup.findAll('h4')
    b=''
    for x in range(0,len(table)):
        if(table[x+1].text=="Current town/city"):
            b=table[x].text
            break
        else:
            continue
    #print(b)
    #work
    table = soup.find('div', attrs={'id':'work'})
    table = table.findAll('span', attrs={'class':'_52jd'})
    c=list()
    for x in range(0,len(table)):
        c.append(table[x].text)
    print(naam, "works at ",c)
    #fav
    table = soup.findAll('span', attrs={'class':'_2w79'})
    d=list()
    for x in range(0,len(table)):
        d.append(table[x].text)
    #print(b)
    output=str()
    if(len(d)):
        output+=str(d)+"\n"
    else:
        output+="There are no fav \n"
    person = Person(naam,c,b)
    sleep(3)
    driver.quit()
    output+=person.show()
    return output
    #input('Press anything to quit')
    #print("Finished")
#print(scrap("radhikagarg1601"))
#print(scrap("sanjeetmanna14"))
#scrap("anshul.d.sharma.7")
class LearnTest(unittest.TestCase):
    def test_func_1(self):
        a="radhikagarg1601"
        result = scrap(a)
        self.assertEqual(result,"['Quantum Computing Group', 'How I Met Your Mother', 'IITR Honest Confessions', 'The DREAM PIE Bakery', 'IIT Roorkee', 'mansiyogaandfitness']\nMy name is Radhika Garg and my current city is Roorkee.")
    def test_func_2(self):
        a="sanjeetmanna14"
        result = scrap(a)
        self.assertEqual(result,"Username is not in database")
if __name__=="__main__":
    unittest.main()