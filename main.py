
first = (int(input('Ведите число:')))
second= (int(input('Ведите число:')))
third=(int(input('Ведите число:')))
if first==second==third:
    print(3)
elif first==second!=third or first==third!=second or first!=second==third:
    print(2)
elif first!=second!=third:
    print(0)