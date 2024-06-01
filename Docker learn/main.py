while True:
    user_input = input('Enter some info (or "exit" to stop): ')
    
    # Exit the loop if the user enters 'exit'
    if user_input.lower() == 'exit':
        break

    with open('names.txt', 'a') as file:
        file.write(user_input + '\n')
        
    
with open('names.txt', 'r') as file:
    print(file.read())