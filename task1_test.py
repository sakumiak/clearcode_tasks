from task1 import group_by

none_year = group_by(open('launchlog.txt'), 'year')
f_year = group_by(open('launchlog.txt'), 'year', False)
s_year = group_by(open('launchlog.txt'), 'year', True)

none_month = group_by(open('launchlog.txt'), 'month')
f_month = group_by(open('launchlog.txt'), 'month', False)
s_month = group_by(open('launchlog.txt'), 'month', True)

def none_test():


	su = 0
	for s,v in none_year.items():
		su += v
	
	out = [True] if su == 10563 else False

	if none_year['1957'] == 4 and none_year['1958'] == 28 and none_year['1959'] == 31 and none_year['1960'] == 66:
		out.append(True)
	else:
		out.append(False)
	su = 0
	for s,v in none_month.items():
		su += v
	
	if su == 10563:
		out.append(True)
	else:
		out.append(False)

	if none_month['Apr'] == 940 and none_month['Aug'] == 847:
		out.append(True)
	else:
		out.append(False)
	return 'None-year',out

def fs_year_test():
	out = True
	for s,v in none_year.items():
		if f_year[s] + s_year[s] != none_year[s]:
			out = False

	return "Filter year test",out

def fs_month_test():
	out = True
	for s,v in none_month.items():
		if f_month[s] + s_month[s] != none_month[s]:
			out = False

	return "Filter month test",out

if __name__ == '__main__':

	print(none_test())
	print(fs_year_test())
	print(fs_month_test())
		
