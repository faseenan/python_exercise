#stock_transaction.py
nshare_purchased = 2000
amount_one_share = 40.00
total_paid = nshare_purchased*amount_one_share

print('--'*50)
print("Total amount joe paid for stock $",format(total_paid, '.2f'), sep='')
commission_when_bought= total_paid*.03
print("The amount paid to the broker when joe bought the stock $",format(commission_when_bought, '.2f'), sep='')
paid_money = total_paid+commission_when_bought
print ('total money Joe paid  $',format(paid_money, '.2f'), sep='')
print('--'*50)


nshare_sold = 2000
amount_of_one_sold_share = 42.75
total_amount_share_sold = amount_of_one_sold_share*nshare_sold
commission_when_sold = total_amount_share_sold*.03
print("Total amount joe sold the stock for  for $",format(total_amount_share_sold, '.2f'), sep='')
print("The amount paid to the broker when joe sold  the stock $",format(commission_when_sold, '.2f'), sep='')
total_money_when_sold = total_amount_share_sold - commission_when_sold

print ('money Joe got after selling the stock  $',format(total_money_when_sold, '.2f'), sep='')
print('--'*50)

profit = total_money_when_sold - paid_money
if profit>0:
	print("Joe made profit")
else:
	print("joe lost the money")



