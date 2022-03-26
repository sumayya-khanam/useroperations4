import csv
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def saveUsername(request):
    username = request.GET.get('username')
    file = open('app7/users.txt', 'a+')
    status = 'User not saved'
    with open('app7/users.txt') as myfile:
        if username in myfile.read():
            status = 'User already exists'
        else:
            file.write('\n'+ username)
            status='User saved'
    file.close()
    return Response(status)


@api_view(['POST'])   
def checkPassword(request):
    password = request.POST.get('password') 
    status = 'Invalid password'
    print(password)
    l, u, p, d = 0, 0, 0, 0
    if (len(password) >= 8):
        for letter in password:
            if (letter.islower()):
                l+=1
                
            if (letter.isupper()):
                u+=1
                
            if (letter.isdigit()):    
                d+=1
            if (letter == '@'  or letter == '$' or letter == '_'):
                p+=1
    
    if ( l>=1 and u>=1 and p>=1 and d>=1 and l+u+p+d == len(password)):
        print("Valid password")      
        status = "Valid password"
    else:
        print("Invalid password")    
        status = "Invalid password"
    return Response(status)  

@api_view(['GET'])
def checkUsername(request):
    username = request.GET.get('username')  
    file  = open('app7/users.txt','r+')
    users = file.read().splitlines()
    file.close()
    print(users)
    status = 'invalid username'
    if username in users:
        status = 'Valid username'
    return Response(status)

@api_view(['GET'])
def viewproducts(request):
    csv_file= open('app7/products.csv')
    csv_reader= csv.reader(csv_file, delimiter = ',')
    line_count= 0
    display = []
    for row in csv_reader:
        if line_count == 0:
            print(f'{row[1]} {row[2]} {row[3]} ')
            display.append(f'{row[1]} {row[2]} {row[3]} ')
            line_count +=1
        else:
            print(f'{row[1]} \t  {row[2]} \t {row[3]} ')
            line_count +=1
            display.append(f'{row[1]} {row[2]} {row[3]} ')
    return Response(display)

    
            
                  
        
        
        
        
