#The count-and-say sequence is the sequence of integers beginning as follows:
#1, 11, 21, 1211, 111221, ...

#1 is read off as "one 1" or 11.
#11 is read off as "two 1s" or 21.
#21 is read off as "one 2, then one 1" or 1211.
#Given an integer n, generate the nth sequence.


def count_and_say(n):
	new_string = start_string = "1";
	k = 0
	n = n -1;
	while k < n:
		new_string = "";
		i = 0;
		while i < len(start_string):
			count = 1;
			if i+1 < len(start_string) and start_string[i] == start_string[i+1] :
				count = count + 1;
				i = i + 1;
			new_string = new_string + str(count) + start_string [i];i = i + 1;
		start_string = new_string;
		k = k + 1;
	return start_string;

print count_and_say (10);
