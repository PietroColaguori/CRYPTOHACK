integers = []
for c in "label":
    integers.append(ord(c))

print("Integers:", integers)

flag_nums = []
for i in range(len(integers)):
    flag_nums.append(integers[i] ^ 13)

print("Flag UNICODE:", flag_nums)

flag = ""
for i in range(len(flag_nums)):
    flag += chr(flag_nums[i])

print("crypto{" + flag + "}")
