# create empty list of finished sandwiches to fill
sandwich_orders = ['tuna and sweetcorn', 'chicken and bacon', 'turkey and ham']
finished_sandwiches = []
# while sandwich orders is not empty pop each element and append it to finished
print("sorry deli has run out of pastrami")
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    made_sandwich = sandwich_orders.pop()
    print(f"Making {made_sandwich.title()}")
    finished_sandwiches.append(made_sandwich)
# loop through each finished sandwich to let customer know its made
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} sandwich is made")
