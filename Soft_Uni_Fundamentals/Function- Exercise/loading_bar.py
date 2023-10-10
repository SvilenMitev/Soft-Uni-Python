def loading_bar(number:int):
    if number == 100:
        return f"100% Complete!\n" f"[%%%%%%%%%%]"
    else:
        symbol_number = number/10
        return f"{number}% [{(int(symbol_number))*'%'}{(10-int(symbol_number))*'.'}]\n" "Still loading..."


percentage_input = int(input())
print(loading_bar(percentage_input))