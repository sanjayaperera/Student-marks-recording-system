Dictionary={}
count=0
#CREAT User-Defined Function
def Volume_of_Credit():
    return(0,20,40,60,80,100,120)
print('WELLCOME,\n')
while True:
    
    print()
    print()
#STUDENT ID RECEIVING PART
    student_id_letter=input('plse enter student id first letter:').lower()
    if student_id_letter!='w':
        print('wrong letter')
        continue
    try:
        student_id_numbers=int(input('plese enter student id numbers'))
      
    except:
        print('wrong student id number')
        continue
    student_id_numbers_str=str(student_id_numbers)
    if len(student_id_numbers_str)==7:
        pass
    else:
        print('wrong student id number')
        continue
    student_id =student_id_letter+student_id_numbers_str
            
    print()
    print()
    #INPUT RECEIVING PART AND CHACKING IF THE INPUT IS CORRECT PART
    try:
        pass_credit=int(input('Enter number of credits at pass :'))
    except:
        print('integer requird')
        continue
    if pass_credit not in Volume_of_Credit() :
        print('Out of range')
        continue
    try:
        defer_credit=int(input('Enter number of credits at Defer :'))
    except:
        print('integer required')
        continue
    if defer_credit not in Volume_of_Credit() :
        print('Out of range')
        continue
    try:
        fail_credit=int(input('Enter number of credits at fail :'))
    except:
        print('integer required')
        continue
    if fail_credit not in Volume_of_Credit() :
        print('Out of range')
    total = pass_credit + defer_credit + fail_credit
    if total!=120:
        print('Total incorrect')
        continue
    count+=1
    add_dictionary=pass_credit,defer_credit,fail_credit#SETTING CREDIT TO ADD TO THE DICTIONARY

    # OUT PUT GIVING PART AND DETA ENTRY PART TO DICTIONARY
    if pass_credit==120:
        print('Progress')
        Dictionary[student_id]=f'progress -{add_dictionary}'
        
    elif pass_credit==100:
        print('Progress(module trailer)')
        Dictionary[student_id]=f'Progress(module trailer)-{add_dictionary}'
     
    elif defer_credit>=20 and fail_credit<80:
        print('Do not Progress – module retriever')
        Dictionary[student_id]=f'Do not Progress – module retriever-{add_dictionary}' 
       
        
    elif pass_credit==80 and fail_credit==40:
        print('Do not Progress – module retriever')
        Dictionary[student_id]=f'Do not Progress – module retriever-{add_dictionary}' 
       
    elif pass_credit==60 and fail_credit==60:
        print('Do not Progress – module retriever')
        Dictionary[student_id]=f'Do not Progress – module retriever-{add_dictionary}'
        
    else:
        print('Exclude')
        Dictionary[student_id]=f'Exclude -{add_dictionary}'
    print()
    print()

    break_or_continue=input('Would you like to enter another set of data? Enter (Y).Would you like quit and view dictionary? Enter (Q) :').upper()
    print()
    print('.............................................................................................................')
    
    if break_or_continue=='Q': #PRINT DICTIONARIY
        for(studentnumber,output)in Dictionary.items():
            print(studentnumber,'-',output)
        break
    elif break_or_continue=='Y':
        continue
    else:
        print('wrong input')
        break
        

