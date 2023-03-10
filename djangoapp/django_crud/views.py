from django.shortcuts import render, redirect
import mysql.connector
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here.

#mysql connection
mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='django_crud'
)

mycursor = mydb.cursor()



def index(request):

    mycursor.execute("SELECT * FROM django_crud_cruding")
    result = mycursor.fetchall()
    context = {'posts': result}
    return render(request, 'index.html', context)



def crud(request):
    return render(request, 'crud.html')


@csrf_exempt
def upload_post(request):
    if request.method == "POST":
        post = request.POST['upload_post']
        nows = datetime.datetime.now()
        mysql_datetime = nows.strftime('%Y-%m-%d %H:%M:%S')
        mycursor.execute("INSERT INTO django_crud_cruding(post,created_at) VALUES(%s,%s)",(post,mysql_datetime))
        mydb.commit()

        return redirect('index')

    return redirect('crud') 




#delete post
def delete_post(request, post_id):
    # post_id = request.GET.get('post_id')
    mycursor.execute("DELETE FROM django_crud_cruding WHERE c_id=%s", (post_id,))
    mydb.commit()    
    return redirect('index')


def update(request, post_id):
    mycursor.execute("SELECT * FROM django_crud_cruding WHERE c_id=%s", (post_id, ))
    result = mycursor.fetchall()
    context = {'posts': result}
    return render(request, 'update.html', context)