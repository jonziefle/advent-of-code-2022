input_file = 'input.txt'
elf_list = []

with open(input_file) as input:
    lines = input.readlines()
    elf_number = 1
    calorie_count = 0
    for line in lines:
        text = line.strip()
        if text == '':
            # add elf/calorie tuple to list
            elf_list.append((elf_number, calorie_count))
            elf_number += 1
            calorie_count = 0
        else:
            # otherwise increment the calorie_count
            calorie_count += int(text)
    
    # add last tuple
    if calorie_count > 0:
        elf_list.append((elf_number, calorie_count))

    # sort list by calories
    elf_list.sort(key=lambda elf: elf[1], reverse=True)

    total_calories = 0
    for elf in elf_list[:3]:
        print('Elf #{} is carrying {} calories'.format(elf[0], elf[1]))
        total_calories += elf[1]
    
    print('Combined, they are carrying {} calories'.format(total_calories))
    
