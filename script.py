# PDA implementation for language L = {a^n b^n | n >= 1}

def pda_an_bn(input_string):
    stack = []
    state = "q0"

    # push initial stack symbol
    stack.append("Z0")

    for char in input_string:

        # State q0: reading 'a' and pushing into stack
        if state == "q0":
            if char == 'a':
                stack.append('A')

            elif char == 'b':
                # switch to state q1 when 'b' starts
                if stack[-1] == 'A':
                    stack.pop()
                    state = "q1"
                else:
                    return "Rejected"
            else:
                return "Rejected"

        # State q1: reading 'b' and popping from stack
        elif state == "q1":
            if char == 'b':
                if stack[-1] == 'A':
                    stack.pop()
                else:
                    return "Rejected"
            else:
                return "Rejected"

    # Final condition check
    if state == "q1" and stack == ["Z0"]:
        return "Accepted"
    else:
        return "Rejected"


# Main program
print("PDA for L = {a^n b^n | n >= 1}")
user_input = input("Enter a string: ")
result = pda_an_bn(user_input)
print("Result:", result)