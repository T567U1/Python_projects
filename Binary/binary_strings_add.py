x = '10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101'
y = '110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011'
max_len = max(len(x), len(y))
if len(x) < max_len:
    x = '0' * (max_len - len(x)) + x
if len(y) < max_len:
    y = '0' * (max_len - len(y)) + y
print(int(x, 2) + int(y, 2))
def go(l1, l2, carry = 0, ans = ''):
    if not l1:
        return ans, carry
    if l1[-1] == '1' and l2[-1] == '1':
        if carry:
            ans = '1' + ans
        else:
            ans = '0' + ans
            carry += 1
    elif l1[-1] == '0' and l2[-1] == '1' or l1[-1] == '1' and l2[-1] == '0':
        if carry:
            ans = '0' + ans
        else:
            ans = '1' + ans
    else:
        if carry:
            ans = '1' + ans
            carry -= 1 if carry > 0 else 0
        else:
            ans = '0' + ans
    print(ans, carry)
    return go(l1[:-1], l2[:-1], carry, ans)
f = go(x, y)
print(f[0] if not f[1] else '1' + f[0])
