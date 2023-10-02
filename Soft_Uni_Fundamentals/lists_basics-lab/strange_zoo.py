input_tail = input()
input_body = input()
input_head = input()

meerkat = [input_tail, input_body, input_head]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)