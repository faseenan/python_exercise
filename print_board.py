


def dispay_board(x='a',ncol=3,nrow=4):
	s='|'+' '+x+' '
	line= '*---'*ncol+'*'+'\n'+s*ncol+'|'+'\n'
	print(line*nrow, end='')
	print('*---'*ncol+'*')


#a=input('Enter the value ')

dispay_board('a',6,9)

dispay_board('a',nrow=10)









