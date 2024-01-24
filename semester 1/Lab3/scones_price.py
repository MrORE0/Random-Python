# scone_price = 1.49
# scone_amount = int(input("How many scones have you purchased: "))
# scone_old = int(input("How many of these scones are older than one day: "))

# if scone_old != 0:
#     regular_price = scone_price * scone_amount
#     discount_price = scone_old * (scone_price * 0.60)
#     final_price = regular_price - discount_price
# else:
#     final_price = scone_amount * scone_price

# print(f"The regular price for the scones is: {regular_price}")
# print("The discount price for the scones is: %i" % (discount_price))
# print("The final price for the scones is: {0}".format (final_price))



def pricing ():
    scone_price = 1.49
    scone_amount = int(input("How many scones have you purchased: "))
    scone_old = int(input("How many of these scones are older than one day: "))

    if scone_old != 0:
        regular_price = scone_price * scone_amount
        discount_price = scone_old * (scone_price * 0.60)
        final_price = regular_price - discount_price
    else:
        final_price = scone_amount * scone_price

    print(f"The regular price for the scones is: €{round(regular_price,2)}" , end=" ", sep = " ")
    print("The discount price for the scones is: €%.2f" % (discount_price), end = " ", sep = " ")
    print("The final price for the scones is: €{0}".format (round(final_price,2)), end = " ", sep = " ")
    
pricing()



# def pricing ():
#     scone_price = 1.49
#     scone_amount = int(input("How many scones have you purchased: "))
#     scone_old = int(input("How many of these scones are older than one day: "))

#     if scone_old != 0:
#         regular_price = scone_price * scone_amount
#         discount_price = scone_old * (scone_price * 0.60)
#         final_price = regular_price - discount_price
#     else:
#         final_price = scone_amount * scone_price

#     print(f"The regular price for the scones is: €{round(regular_price,2)}" , end=" ", sep = " ")
#     print("The discount price for the scones is: €%.2f" % (discount_price), end = " ", sep = " ")
#     print("The final price for the scones is: €{0}".format (round(final_price,2)), end = " ", sep = " ")

# pricing()