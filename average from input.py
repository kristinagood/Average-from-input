def main():
    total = 0.0
    count = 0

    infile = open('numbers.txt', 'r')

    for line in infile:
        number = float(line)
        count += 1
        total += number
    average = total/count
    print('The average number is:', format(average))

main()
