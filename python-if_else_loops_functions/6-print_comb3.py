#!/usr/bin/python3
output = []
for n in range(100):
	if n < 10:
        	output.append(f"0{n}")
	else:
		res = []
        	res.append(f"{str(n)}")
		last.append(f"{(res[0])[0]}")
		last.append(f"{(res[0])[1]}")
		last.sort()
	if (last[0] + last[1]) in output:
		continue
	else:
		output.append(last[0] + last[1])
]

for i in output:
	print (i, separated = ", ")
