def process_lines(filename):
    total_sum = 0
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  
            first_digit = None
            last_digit = None
            # first digit
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break 

            #last degit
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            
            # If both digits are found, form the two-digit number and add to the sum
            if first_digit is not None and last_digit is not None:
                two_digit_number = int(first_digit + last_digit)
                total_sum += two_digit_number
    
    return total_sum

filename = '357.txt' 
result = process_lines(filename)
print(result)


