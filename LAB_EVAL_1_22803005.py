MOVIES={1:{"TITLE":"YJHD","COPIES":5},
       2:{"TITLE":"DDLJ","COPIES":5},
        3:{"TITLE":"EXORCISM","COPIES":5},
       4:{"TITLE":"IT","COPIES":5}}

CUSTOMER={100:{"NAME":"DIVYANSH","MOVIES":[]},
         200:{"NAME":"PRIYANSHU","MOVIES":[]},
         300:{"NAME":"PRANAV","MOVIES":[]},
         400:{"NAME":"SAUGAT","MOVIES":[]}}

def rent_movie(cid,mid):
    if mid in MOVIES and MOVIES[mid]["COPIES"]>0:
        CUSTOMER[cid]["MOVIES"].append(MOVIES[mid]["TITLE"])
        MOVIES[mid]["COPIES"]-=1
        print(CUSTOMER[cid]['NAME'])
        print(" has rented ")
        print(CUSTOMER[cid]['MOVIES'])
        print("\n")
        
    else:
        print("MOVIE NOT AVAILABLE")
        
def return_movie(cid,mid):
    if MOVIES[mid]['TITLE'] in CUSTOMER[cid]['MOVIES']:
        CUSTOMER[cid]['MOVIES'].remove(MOVIES[mid]['TITLE'])
        MOVIES[mid]["COPIES"]+=1
        print(CUSTOMER[cid]['NAME'])
        print(" has returned ")
        print(MOVIES[mid]['TITLE'])
        print("\n")
        
    else:
        print("MOVIE NOT AVAILABLE")

def dental_report():
    print("REPORT IS: ")
    print(".................................................................................................................")
    print("\n")
    for cid in CUSTOMER.keys():
        print(CUSTOMER[cid]["NAME"])
        print(" HAS RENTED ")
        print(CUSTOMER[cid]["MOVIES"])
        print("\n")
    else:
        print("NO MOVIE")

rent_movie(100,1)
rent_movie(100,3)
rent_movie(200,1)
rent_movie(300,1)
dental_report()
return_movie(100,1)
return_movie(300,1)
dental_report()
