from django.shortcuts import render
import mysql.connector as sql
un=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global un,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sudha1234",database='priyanshu')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                un=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users values('{}','{}','{}')".format(un,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')
