#Python intern tastk - task 1
#Kamil Majewski 2017


#Creat str list of months and years
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year_list = []
for year in range(1957,2018):
	year_list.append(str(year))

#Function counter 
#   Inputs: field_value: str success: bool or None  lines: list(list(str))
#		Output: count: int
#		This function change variable success in 'S' or 'F' if success isn't equal None. Next in for loop it counting launches with or without filters.
def counter (field_value, success, lines):
	count = 0

	if success == True:
		success = 'S'
	elif success == False:
		success = 'F'

	for line in lines:
		if line[0] != " ":
			launch_date = line[13:21]
			suc = line[193] if not(success == None) else None
			if field_value in launch_date and success == suc:
				count += 1
		else:
			if field_value in launch_date and success == suc:
				count += 1
	return count

#Function group_by
#		Inputs: stream: file  field: ['year','month']   succes: bool or None
#		Output: out: {field: int}
#		This function save file lines into list named lines. Next it check field and in for loop use counter function to filter and counting chosen list.
def group_by(stream, field, success = None):
	lines = stream.readlines()
	stream.close()
	out = dict()

	#Delete last list from lines. This list is equale ['/n'].
	del(lines[-1])
	
	if not(field in ["year","month"]):
		return "Wrong field value"
	elif field == "year":
		for field_value in year_list:
			out.update({field_value:counter(field_value,success,lines)}) 
	else:
		for field_value in month_list:
			out.update({field_value:counter(field_value,success,lines)})

	return out

	

if __name__ == '__main__':
	out = group_by(open('launchlog.txt'),"year")
	print(out)
