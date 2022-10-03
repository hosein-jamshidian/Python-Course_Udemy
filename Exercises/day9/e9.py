# 9.1
#
# student_scores={
#     "Harry":81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62
# }
#
# student_grades={}
# # student_grades["Harry"]="Exeeds Expectations"
# # student_grades["Ron"]="Acceptable"
# # student_grades["Hermione"]="Outstanding"
# # student_grades["Draco"]="Acceptable"
# # student_grades["Neville"]="Fail"
#
# print(student_grades)
#
# for key in student_scores:
#     if student_scores[key]>90:
#         student_grades[key]="Outstanding"
#     elif student_scores[key]>80:
#         student_grades[key] = "Exeeds Expectations"
#     elif student_scores[key]>70:
#         student_grades[key]="Acceptable"
#     else:
#         student_grades[key]="Fail"
# print(student_grades)

#9.2

# travel_log=[
#     {'country':'France',
#      'cities':['paris','lille','dijon'],
#      'visits':12},
#     {'country':'german',
#      'cities':['berlin','humborg'],
#      'visits':10
#     }
# ]
#
# def add_new_country(country_name,country_visits,country_cities):
#     new_country={}
#     new_country["country"]=country_name
#     new_country["'cities"]=country_cities
#     new_country["visits"]=country_visits
#     travel_log.append(new_country)
# add_new_country('russia',14,['berlin','humborg'])
# print(travel_log)
#
# #FINAL:
#
import art


print(art.logo)
print("welcome to AUCTION!")

end=False
d={}
while not end :
    name=input("what is you're name ?\n").lower().strip()
    price=int(input("what is you're bid?\n$"))
    d[name]=price
    print(d)

    permission=input("you want to continue?(y / n)").lower()


    if permission=="n":
        max_value=0
        max_key=""
        #{'a':1,'b':2}
        for key in d:
            if d[key]>max_value:
                max_value=d[key]
                max_key=key
        print(f"the winner is {max_key} with a bid of ${int(max_value)}")
        end=True
