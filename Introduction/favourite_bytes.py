from pwn import xor

ctx_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

ctx_bytes = bytes.fromhex(ctx_hex)

# Let's try a bruteforce approach
for key in range(256):

    # We XOR the ctx_bytes with the key to obtain the ptx
    flag = xor(ctx_bytes, key)

    # If the result contains the string "crypto", we have found the flag!
    if b"crypto" in flag:
        print(flag)

''' Additional code to display whole bruteforce results
for key in range(256):
    print("Try n. " + str(key), ":", xor(ctx_bytes, key))
'''

