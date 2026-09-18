#to rewrite in binary file
#to append and rewrite in a+ mode in csv (append in done)
#file not exist error in 'n'

import csv as ca
import pickle as p
import os
from datetime import datetime



def csv(c,d):
    if c == 'a+' or c == 'a':
        with open(d,c,newline = '') as f:
            writer = ca.writer(f)
            print("If file opened in 'a' mode enter only append")
            g = input("Do you want to 'append' or 'read' the existing file: ")

            if g.lower() == 'append':
                ll = []
                num = 1
                numm = 1
                row = int(input('Enter the number of entries(rows): '))
                col = int(input('Enter the number of elements in each row: '))
                print()

                for i in range(row):
                    i = []
                    for j in range(col):
                        j = eval(input('Enter the '+str(numm)+'st '+'element of '+str(num)+'st row: '))
                        numm += 1
                        i.append(j)
                    numm = 1
                    print()
                    num += 1
                    ll.append(i)

                for mmm in ll:
                    writer.writerow(mmm)

                print()
                print("Enter only 'y' or 'n'")
                ch = input('Do you like to read the file: (y/n) ')
                print()

                if ch == 'y':
                    f.seek(0)
                    no = 1
                    hah = ca.reader(f)
                    for i in hah:
                        print('\t',no,'. ',i)
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                elif ch == 'n':
                    print('Program Ended! Aborting!')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                else:
                    print('Input Error. Try again!')
                    print()
                    
            elif g.lower() == 'read':
                print('READ MODE:- ')
                print()
                f.seek(0)
                re = ca.reader(f)
                no = 1

                for i in re:
                    print('\t',no,". ",i)

                print()
                final = input('Do you like to append now: (y/n) ')

                if final == 'n':
                    print('Alright! The program ended.')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                elif final == 'y':
                    writer = ca.writer(f)
                    ll = []
                    num = 1
                    numm = 1
                    row = int(input('Enter the number of entries(rows): '))
                    col = int(input('Enter the number of elements in each row: '))
                    print()

                    for i in range(row):
                        i = []
                        for j in range(col):
                            j = eval(input('Enter the '+str(numm)+'st '+'element of '+str(num)+'st row: '))
                            numm += 1
                            i.append(j)
                        numm = 1
                        print()
                        num += 1
                        ll.append(i)

                    for mmm in ll:
                        writer.writerow(mmm)

                    print()
                    fin = input('Like to read the file: (y/n) ')

                    if fin == 'y':
                        print('READ MODE:- ')
                        print()
                        f.seek(0)
                        re = ca.reader(f)
                        no = 1

                        for i in re:
                            print('\t',no,". ",i)
                        print()
                        ct = datetime.now()
                        print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                        print()

                    elif fin == 'n':
                        print('Alright! The program ended.')
                        print()
                        ct = datetime.now()
                        print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                        print()

                    else:
                        print('Invalid Input. Aborting Program!')

                else:
                    print('Invalid Input. Aborting Program!')
                


    elif c == 'w+' or c == 'w':
        with open(d,c,newline = '') as f:
            print("You have to write the file first!")
            writer = ca.writer(f)
            ll = []
            num = 1
            numm = 1
            row = int(input('Enter the number of entries(rows): '))
            col = int(input('Enter the number of elements in each row: '))
            print()

            for i in range(row):
                i = []
                for j in range(col):
                    j = eval(input('Enter the '+str(numm)+'st '+'element of '+str(num)+'st row: '))
                    numm += 1
                    i.append(j)
                numm = 1
                print()
                num += 1
                ll.append(i)

            for mmm in ll:
                writer.writerow(mmm)

            print()
            print("Enter 'n' if file is opened in 'w' mode.")
            ch = input('Would you like to read the file you created: (y/n) ')

            if ch == 'n':
                print("Alright! The program ended!")
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            elif ch == 'y':
                print()
                print('READ MODE:- ')
                print()
                f.seek(0)
                no = 1
                read = ca.reader(f)

                for i in read:
                    print('\t',no,". ",i)
                    no +=1

                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            else:
                print('Invalid input! Aborting!')
                print()



    elif c == 'r' or c == 'r+' or c == '':
        with open(d,c,newline = '') as f:
            print()
            print('OPENED THE FILE IN READ MODE:- ')
            za = ca.reader(f)
            no = 1

            for i in za:
                print('\t',no,". ",i)
                no += 1

            print()
            print("Enter 'n' if file is opened in 'r' mode")
            oh = input('Do want to write more on the file: (y/n) ')

            if oh == 'y':
                writer = ca.writer(f)
                num = 1
                print()
                print("Enter 'done' to End.")
                ll = []
                num = 1
                numm = 1
                row = int(input('Enter the number of entries(rows): '))
                col = int(input('Enter the number of elements in each row: '))
                print()

                for i in range(row):
                    i = []
                    for j in range(col):
                        j = eval(input('Enter the '+str(numm)+'st '+'element of '+str(num)+'st row: '))
                        numm += 1
                        i.append(j)
                    numm = 1
                    print()
                    num += 1
                    ll.append(i)

                for mmm in ll:
                    writer.writerow(mmm)

                print()
                final =  input("Do you like to read the edited file: (y/n) ")

                if final == 'y':
                    f.seek(0)
                    rap = ca.reader(f)
                    no = 1

                    for i in rap:
                        print('\t',no,'. ',i)
                        no += 1

                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                elif final == 'n':
                    print('Alright! The program ended.')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                else:
                    print('Invalid input! Aborting program!')

            elif oh == 'n':
                print('Alright! The program ended. ')
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            else:
                print('Invalid input! Aborting Program!')
                

            

    
def binary(c,d):
    if c == 'wb+' or c == 'wb':
        with open(d,c) as f:
            print("You have to write the file first.")
            print()
            true = True
            print("Enter 'done' to end the loop. ")
            lop = []

            while true:
                lok = input('Enter the data: ')

                if lok == 'done':
                    true = False
                    print()

                else:
                    lop.append(lok)
            p.dump(lop,f)
                    
            gy = input('Do you like to read the file: (y/n) ')

            if gy == 'n':
                print('Alright! The program ended.')
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            elif gy == 'y':
                f.seek(0)
                no = 1
                oa = p.load(f)
                print()
                print('IN READ MODE:- ')
                print()

                try:
                    for i in oa:
                        print('\t',no,'. ',i)
                        no += 1
                    print()

                except EOFError:
                    pass

                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            else:
                print('Input Error. Try again! ')

                

    elif c == 'rb' or c == 'rb+':
        with open(d,c) as f:
            gy = input('Do you like to read the file: (y/n) ')

            if gy == 'n':
                print('Alright! The program ended.')
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            elif gy == 'y':
                f.seek(0)
                print()
                no = 1
                while True:
                    f.seek(0)
                    oa = p.load(f)

                    try:
                        for i in oa:
                            print('\t',no,'. ',i)
                            no+=1

                    except EOFError:
                        pass
                    print()
                    print(oa)
                    print()
                    break

            else:
                print('Input Error. Try again! ')

            print("Enter 'n' if the file is opened in 'rb' mode.")
            gt = input('Do you like to rewrite the file: (y/n) ')
            print()

            if gt == 'n':
                print('Alright! The program ended.')
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            elif gt == 'y':
                f.seek(0)
                false = True
                print("Enter 'done' to end the loop. ")
                print()

                while false:
                    pol = input('Enter the data: ')

                    if pol == 'done':
                        print()
                        false = False

                    else:
                        p.dump(pol,f)
                    
                final = input('Do you like to read the edited file: (y/n) ')

                if final == 'y':
                    f.seek(0)
                    oaa = p.load(f)

                    try:
                        no = 1
                        print('IN READ MODE:-')
                        print()
                        for i in oa:
                            print('\t',no,'. ',i)
                        print()
                        
                    except EOFError:
                        pass

                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                elif final == 'n':
                    print('Alright! The Program Ended!')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

            else:
                print('Input Error. Aborting!')

    elif c == 'a' or c == 'ab+' or c == 'a+' or c == '':
        with open(d,c) as f:
            print('As this file is opened in append mode')
            print('The file MUST NEED TO BE EXISTED ')
            print('If not it may lead to ERRORS!')
            print()
            print("Enter 'append' if file opened in 'ab' mode")
            g = input("Do you want to 'append' or 'read' the existing file: ")

            if g == 'append':
                true = True
                print()
                print("Enter 'done' to end the loop. ")
                print()
                lop = []

                while true:
                    lok = input('Enter the data: ')

                    if lok == 'done':
                        true = False
                        print()

                    else:
                        lop.append(lok)
                p.dump(lop,f)
                        
                gy = input('Do you like to read the file: (y/n) ')

                if gy == 'n':
                    print('Alright! The program ended.')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                elif gy == 'y':
                    f.seek(0)
                    no = 1
                    while True:
                        oa = p.load(f)
                        print()
                        print('IN READ MODE:- ')
                        print()

                        try:
                            for i in oa:
                                print('\t',no,'. ',i)
                                no += 1
                            print()

                        except EOFError:
                            pass

                        print()
                        ct = datetime.now()
                        print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                        print()
                        break

                else:
                    print('Input Error. Try again! ')

            elif g == 'read':
                f.seek(0)
                no = 1
                oa = p.load(f)
                print()
                print('IN READ MODE:- ')
                print()

                try:
                    for i in oa:
                        print('\t',no,'. ',i)
                        no += 1
                        print()

                except EOFError:
                    pass

                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()
                gy = input('Do you like to append now: (y/n) ')

                if gy == 'n':
                    print()
                    print('Alright! The Program Ended.')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                elif gy == 'y':
                    true = True
                    print("Enter 'done' to end the loop. ")
                    lop = []

                    while true:
                        lok = input('Enter the data: ')

                        if lok == 'done':
                            true = False
                            print()

                        else:
                            lop.append(lok)
                    p.dump(lop,f)
                    final = input('Do you like to read the edited file: (y/n) ')

                    if final == 'n':
                        print()
                        print('Alright! The Program Ended.')
                        print()
                        ct = datetime.now()
                        print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                        print()
                    
                    elif final == 'y':
                        f.seek(0)
                        no = 1
                        oa = p.load(f)
                        print()
                        print('IN READ MODE:- ')
                        print()

                        try:
                            for i in oa:
                                print('\t',no,'. ',i)
                                no += 1
                            print()

                        except EOFError:
                            pass

                        print()
                        ct = datetime.now()
                        print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                        print()
                    
                

                
            




  
def text(c,d):
    if c == 'a+' or c == 'a':
        with open(d,c) as f:
            print('As this file is opened in append mode')
            print('The file MUST NEED TO BE EXISTED ')
            print('If not it may lead to ERRORS!')
            print()
            print("Enter 'append' if file opened in 'a' mode")
            g = input("Do you want to 'append' or 'read' the existing file: ")

            if g == 'append':
                aa = input('Is input values in list or string: ')

                if aa.lower() == 'list':
                    print("Add /n in the end for new line. ")
                    l = []
                    loop = True
                    yy = 1
                    print()
                    print("Enter 'done' in input to exist.")

                    while loop:
                        y = input('Enter the '+str(yy)+'st line or element of list: ')

                        if y == 'done':
                            loop = False

                        else:
                            yy+=1
                            l.append(y)
                            continue
                    print()
                    print('THE CREATED LIST:- ')
                    print(l)
                    print()
                    print('The list has been written successfully ')
                    f.writelines(l)
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                    
                elif aa.lower() == 'string':
                    loop = False
                    print()
                    print("Enter 'done' to stop!")
                    print()

                    while not loop:
                        zz = input("New line 'nl' or continuous 'c': ")

                        if zz == 'done':
                            print('Strings Appended!')
                            print()
                            loop = True

                        elif zz == 'nl':
                            y = input('Enter the line: ')
                            print()
                            f.write('\n'+y)

                        elif zz == 'c':
                            y = input('Enter the line: ')
                            print()
                            f.write(' '+y)

                        else:
                            print('Input Error! Try again.')
                            print()

                print("Enter 'n' if file is opened in 'a' mode")
                zad = input('Do you want to read the file: (y/n) ')
                if zad == 'y':
                    print()
                    print('IN READ MODE:-')
                    print()
                    f.seek(0)
                    aoaa = f.read()
                    print(aoaa)
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                elif zad == 'n':
                    print('Alright! The program ended. ')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                else:
                    print('Input Error. Try again!')
                        

            elif g == 'read':
                print()
                print('IN READ MODE:-')
                print()
                f.seek(0)
                aoaa = f.read()
                print(aoaa)
                print()
                final = input('Do you like to append in the file now: (y/n) ')

                if final == 'n':
                    print('Alright! The program ended.')

                elif final == 'y':
                    aa = input('Is input values in list or string: ')

                    if aa.lower() == 'list':
                        print("Add '\n' in the end for new line. ")
                        l = []
                        loop = True
                        yy = 1
                        print()
                        print("Enter 'done' in input to exist.")

                        while loop:
                            y = input('Enter the'+str(yy)+'st line or element of list: ')

                            if y == 'done':
                                loop = False

                            else:
                                yy+=1
                                l.append(y)
                                continue

                        print('THE CREATED LIST:- ')
                        print(l)
                        print('The list has been written successfully ')
                        f.writelines(l)
                        print()
                        ct = datetime.now()
                        print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                        print()

                        
                    elif aa.lower() == 'string':
                        loop = False
                        print()
                        print("Enter 'done' to stop!")
                        print()

                        while not loop:
                            zz = input("New line 'nl' or continuous 'c': ")

                            if zz == 'done':
                                print('Strings Appended!')
                                print()
                                loop = True

                            elif zz == 'nl':
                                y = input('Enter the line: ')
                                print()
                                f.write('\n'+y)

                            elif zz == 'c':
                                y = input('Enter the line: ')
                                print()
                                f.write(' '+y)

                            else:
                                print('Input Error! Try again.')
                                print()

                    print("Enter 'n' if file is opened in 'a' mode")
                    zad = input('Do you want to read the file: (y/n) ')

                    if zad == 'y':
                        f.seek(0)
                        aju = f.read()
                        print('IN READ MODE:-')
                        print()
                        print(aju)
                        print()
                        ct = datetime.now()
                        print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                        print()

                    elif zad == 'n':
                        print('Alright! The program ended. ')
                        print()
                        ct = datetime.now()
                        print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                        print()

                    else:
                        print('Input Error. Try again!')
                    
            else:
                print('Input Error! Try Again.')



    elif c == 'w+' or c == 'w':
        with open(d,c) as f:
            print("As this file opened in 'w+'or 'w' you have to write the file first!")
            print()
            aa = input('Is input values in list or string: ')

            if aa.lower() == 'list':
                print("Add '\n' in the end for new line. ")
                l = []
                loop = True
                yy = 1
                print()
                print("Enter 'done' in input to exist.")

                while loop:
                    y = input('Enter the '+str(yy)+'st line or element of list: ')

                    if y == 'done':
                        loop = False

                    else:
                        yy+=1
                        l.append(y)
                        continue

                print()
                print('THE CREATED LIST:- ')
                print('\t',l)
                print('The list has been written successfully ')
                f.writelines(l)
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

                
                    
            elif aa.lower() == 'string':
                loop = False
                print("Enter 'done' to stop.")
                print()
                zs = input('Enter your first line: ')
                print()
                f.write(zs)

                while not loop:
                    zz = input("New line 'nl' or continuous 'c': ")

                    if zz == 'done':
                        print()
                        loop = True

                    elif zz == 'nl':
                        y = input('Enter the line: ')
                        f.write('\n'+y)
                        print()

                    elif zz == 'c':
                        y = input('Enter the line: ')
                        f.write(' '+y)
                        print()

                    else:
                        print('Input Error! Try again.')
                        print()

            print()
            print("Enter 'n' if file is opened in 'w' mode")
            choice = input('Do you like to read the created file: (y/n) ')

            if choice == 'y':
                print()
                print('IN READ MODE:- ')
                print()
                f.seek(0)
                aoa = f.read()
                print(aoa)
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            elif choice == 'n':
                print('Alright! The program ended.')
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()

            else:
                print('Input Error! Try again. ')
            

            
    elif c == 'r' or c == 'r+':
        with open(d,c) as f:
            print('IN READ MODE:-')
            print()
            f.seek(0)
            ac = f.read()
            print(ac)
            print()
            print("Enter 'n' if file is opened in 'r' mode")
            zzz = input("Do you like to 're-write' or 'append' on the file: ")

            if zzz.lower() == 'append':
                print()
                aa = input('Is input values in list or string: ')

                if aa.lower() == 'list':
                    print("Add '/n' in the end for new line. ")
                    l = []
                    loop = True
                    yy = 1
                    print()
                    print("Enter 'done' in input to exist.")

                    while loop:
                        y = input('Enter the '+str(yy)+'st line or element of list: ')

                        if y == 'done':
                            loop = False

                        else:
                            yy+=1
                            l.append(y)
                            continue
                    print()
                    print('THE CREATED LIST:- ')
                    print(l)
                    print()
                    print('The list has been written successfully ')
                    f.writelines(l)
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                    
                elif aa.lower() == 'string':
                    loop = False
                    print()

                    while not loop:
                        zz = input("New line 'nl' or continuous 'c': ")

                        if zz == 'nl':
                            y = input('Enter the line: ')
                            f.write('\n'+y)
                            print()

                        elif zz == 'c':
                            y = input('Enter the line: ')
                            f.write(' '+y)
                            print()

                        else:
                            print('Input Error! Try again.')
                            print()

                final = input('Do you like to read the edited file: ')

                if final == 'y':
                    print()
                    print('IN READ MODE:-')
                    print()
                    f.seek(0)
                    ac = f.read()
                    print(ac)
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                elif final == 'n':
                    print('Alright! The program ended.')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    print()

                else:
                    print('Invalid input! Aborting program!')

            elif zzz.lower() == 'rewrite' or zzz.lower() == 're-write':
                print()
                f.seek(0)
                aa = input('Is input values in list or string: ')

                if aa.lower() == 'list':
                    print("Add '/n' in the end for new line. ")
                    l = []
                    loop = True
                    yy = 1
                    print()
                    print("Enter 'done' in input to exist.")

                    while loop:
                        y = input('Enter the '+str(yy)+'st line or element of list: ')

                        if y == 'done':
                            loop = False

                        else:
                            yy+=1
                            l.append(y)
                            continue
                    print()
                    print('THE CREATED LIST:- ')
                    print(l)
                    print()
                    print('The list has been written successfully ')
                    f.writelines(l)
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                    
                elif aa.lower() == 'string':
                    print()
                    fl = input('Enter the first line: ')
                    f.write(fl)
                    loop = False
                    print('Enter done to exist')
                    print()

                    while not loop:
                        zz = input("New line 'nl' or continuous 'c': ")

                        if zz == 'done':
                            loop = True

                        elif zz == 'nl':
                            y = input('Enter the line: ')
                            f.write('\n'+y)
                            print()

                        elif zz == 'c':
                            y = input('Enter the line: ')
                            f.write(' '+y)
                            print()

                        else:
                            print('Input Error! Try again.')
                            print()


                final = input('Do you like to read the edited file: (y/n) ')

                if final == 'y':
                    print('IN READ MODE:-')
                    print()
                    f.seek(0)
                    ac = f.read()
                    print(ac)
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))

                elif final == 'n':
                    print('Alright! The program ended.')
                    print()
                    ct = datetime.now()
                    print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))

                else:
                    print('Invalid input! Aborting program!')

            elif zzz.lower() == 'n':
                print('Alright! The Program Ended!')
                print()
                ct = datetime.now()
                print("THE PROGRAM ENDED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
                print()
                        
            else:
                print('Input Error. Aborting!')
                

print()
ct = datetime.now()
print("THE PROGRAM STARTED TIME:- ",ct.strftime("%Y-%m-%d %H:%M:%S"))
print()
print('FILES STORAGE:-')
print('\tEnter the datas required.')
print()

while True:
    choh = ['a','w','r','w+','r+','a+']
    b = input("Is your file already exists: (y/n) ")
    if b.lower() == 'y':
        print('Available options:- ')
        print('\t 1. r'+'     (It takes as wb+ for binary files)')
        print('\t 2. w'+'     (It takes as wb+ for binary files)')
        print('\t 3. a'+'     (It takes as rb+ for binary files)')
        print('\t 4. r+'+'    (It takes as rb+ for binary files)')
        print('\t 5. w+'+'    (It takes as ab+ for binary files)')
        print('\t 6. a+'+'    (It takes as ab+ for binary files)')
        print()

        c = input("What mode: ")
        if c not in choh:
            print('Invalid mode! Try again!')
            print()
            continue
        d = input("Enter your file name: ")
        a = input("'Binary File' or 'Csv File' or 'Text File': ")
        if a.lower() == 'csv file':

            if os.path.exists(d+'.csv'):
                print()
                print('File Name: ',d+'.csv')
                print('File Mode: ',c)
                print()
                csv(c,d+'.csv')
                print()
                break

            else:
                print('File Not Found! Try Again!')
                print()
                continue

        elif a.lower() == 'binary file':

            if os.path.exists(d+'.dat'):
                print()
                print("File Name: ",(d+'.dat'))
                print("File Mode: ",(c[0] + 'b+'))
                print()
                binary((c[0] + 'b+'),(d+'.dat'))
                print()
                break

            else:
                print('File Not Found! Try Again!')
                print()
                continue

        elif a.lower() == 'text file':

            if os.path.exists(d+'.txt'):
                print()
                print('File Name: ',d+'.txt')
                print('File Mode: ',c)
                print()
                text(c,d+'.txt')
                print()
                break

            else:
                print('File Not Found! Try Again!')
                print()
                continue

        else:
            print('Input Error! Try again.')
            print()
            continue

    elif b.lower() == 'n':
        c = 'w+'
        print("As this file doesn't exist, it is opened in 'w+' mode")
        print()
        d = input("Enter your new file name: ")
        a = input("'Binary File' or 'Csv File' or 'Text File': ")
        print()
        if a.lower() == 'csv file':

            if not os.path.exists(d+'.csv'):
                print('File Name: ',d+'.csv')
                print('File Mode: ',c)
                print()
                csv(c,d+'.csv')
                print()
                break

            else:
                print('File Already Exist! Try Again!')
                print()
                continue

        elif a.lower() == 'binary file':

            if not os.path.exists(d+'.dat'):
                print()
                print("File Name: ",(d+'.dat'))
                print("File Mode: ",(c[0] + 'b+'))
                print()
                binary((c[0] + 'b+'),(d+'.dat'))
                print()
                break

            else:
                print('File Already Exist! Try Again!')
                print()
                continue

        elif a.lower() == 'text file':

            if not os.path.exists(d+'.txt'):
                print('File Name: ',d+'.txt')
                print('File Mode: ',c)
                print()
                text(c,d+'.txt')
                print()
                break

            else:
                print('File Already Exist! Try Again!')
                print()
                continue

        else:
            print('Input Error! Try again.')
            print()
            continue

    else:
        print('Enter only valid letters! Try again.')
        print()
        continue
