# Loops - For Loops and While Loops

# Question 1

# counter = 8

# while counter > 0:
#     print(counter)

    # if counter%2 == 0:
    #     print(f"{counter} is an even number.")
    # else:
    #     print(f"{counter} is an odd number.")


# Question 2

# mailing_list = [
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Biscuit", "biscuit@whippies.park"],
#     ["Rory", "rory@whippies.park"]
# ]

# # print(mailing_list)

# for item in mailing_list: 
#     print(f"{item[0]:<5}: {item[1]}")


# Question 3

names = ["Izzy", "Archie", "Boston"]

counter = 0
while counter < 3:
    names = input("What is your name? ")
    counter = counter + 1

print(names)



# # Question 4

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]
# total = 0

# for item in groceries:
#     quantity = input(f"What quantity of {item[0]} would you like?")
#     item[1] = item[1] *int(quantity)
#     total += item[1]

# total = f"${total:.2f}"

# print("==== Izzy's Food Emporium ====")
# for item in groceries:
#     print(f"{item[0]:<20} ${item[1]:.2f}")
# print("==============================")
# print(f"{total:>27}")





    
        # print(f"{item[0]:<20} ${item[1]:.2f}")
