break_or_continue=0
progress=0
module_trailer=0
dn_progress=0
exclude=0
outcomes=0
credit_list=[]
outcome_list=[]

#CREAT User-Defined Function
def Volume_of_Credit():
    return(0,20,40,60,80,100,120)

print('wellcome,\n')
print('PROGRESSION OUTCOMS PROGRAM,\n')
# IDENTIFYING A STUDENT OR STAFF MEMBER
staffmember_or_student=input('if you are a student,enter(S).if you are staff member,enter(M)').upper()
if staffmember_or_student not in('M','S'):
    print('wrong input.pleas try again')
 
   
else: 
    while True:
        
        print()
        print()
    #INPUT RECEIVING PART AND CHACKING IF THE INPUT IS CORRECT PART
        try:
            pass_credit=int(input('Enter number of credits at pass :'))
        except:
            print('integer requird')
            continue
        if pass_credit not in Volume_of_Credit():
            print('Out of range')
            continue
        try:
            defer_credit=int(input('Enter number of credits at Defer :'))
        except:
            print('integer required')
            continue
        if defer_credit not in Volume_of_Credit():
            print('Out of range')
            continue
        try:
            fail_credit=int(input('Enter number of credits at fail :'))
        except:
            print('integer required')
            continue
        if fail_credit not in Volume_of_Credit() :
            print('Out of range')
            continue
        #CALCULAT TOTAL
        total = (pass_credit + defer_credit + fail_credit) 
        if total!=120:
            print('Total incorrect')
            continue
        outcomes+=1  #GET OUTCOMES
        add_list=pass_credit,defer_credit,fail_credit    #DETA ENTRY PART TO LIST 1
        credit_list.extend([add_list])                     #DETA ENTRY PART TO LIST 1
    # OUT PUT GIVING PART AND DETA ENTRY PART TO LIST 2  
        if pass_credit==120:
            print('Progress')
            progress+=1
            outcome_list.extend(['progress'])
        elif pass_credit==100:
            print('Progress(module trailer)')
            module_trailer+=1
            outcome_list.extend(['Progress(module trailer)'])
        elif defer_credit>=20 and fail_credit<80:
            print('Do not Progress – module retriever')
            dn_progress+=1
            outcome_list.extend(['Module retriever'])
        elif pass_credit==80 and fail_credit==40:
            print('Do not Progress – module retriever')
            dn_progress+=1
            outcome_list.extend(['Module retriever'])
        elif pass_credit==60 and fail_credit==60:
            print('Do not Progress – module retriever')
            dn_progress+=1
            outcome_list.extend(['Module retriever'])
        else:
            print('Exclude')
            exclude+=1
            outcome_list.extend(['Exclude'])
        #PART OF THA PROGRAM CONTINUES OR STOPS DEPENDING ON WHETHER IT IS A STUDENT OR STAFF MEMBERS
        if staffmember_or_student=='S':
            break
        elif staffmember_or_student=='M':
            pass

      

        print()
        print()

        break_or_continue=input('Would you like to enter another set of data? Enter (Y).Would you like quit and view results? Enter (Q) :').upper()
        if break_or_continue=='Q':
            print()
            print('...............................................................................................................................................')
            # HISTOGRAM PART
            print('Histogram')
            print('Progress',progress,           progress*'*')
            print('Trailer',module_trailer,      module_trailer*'*')
            print('Retriever',dn_progress,       dn_progress*'*')
            print('Excluded',exclude,            exclude*'*')
            print(outcomes,'outcome in total.\n')
            print('................................................................................................................................................')
            print()
            #THE PART THAT TAKES OUTPUT FROM LISTS
            for i in range(outcomes):
                print(outcome_list[i],'-',credit_list[i])
                print()
            
            print('................................................................................................................................................')    
            #TEXT FILE PART
            save_file=open('save file.txt','w')
            for i in range(outcomes):
                save_file.write( f'{outcome_list[i]}-{credit_list[i]}\n')
            save_file.close()
            print()
            print()
            #DISPLAY TEXT FILE PART
            print('LIST OUTCOMS')
            display_file=open('save file.txt','r')
            see_file=display_file.read()
            display_file.close()
            print(see_file)
            break
        
        elif break_or_continue=='Y':
            continue
        else:
            print('wrong input')
            break





        
            
                

        
            
