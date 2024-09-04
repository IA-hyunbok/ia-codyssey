print('Hello Mars')

file_path = 'mission_computer_main.log'
output_file_path = 'error.log'

try:
    with open(file_path, 'r', encoding='UTF-8') as log:
        logs = log.readlines()
        for text in logs:
            print(text.strip())

        print()
        logs.sort(reverse=True)
        with open('sorted_log.log', 'w', encoding='UTF-8') as sorted_log:
            for text in logs:
                sorted_log.write(text.strip() + '\n')
                print(text.strip())

except Exception as e:
    print(f'오류!\n오류내용 : {e}')
    with open(output_file_path, 'a', encoding='UTF-8') as error_log:
        error_log.write(f'오류 발생! 오류 내용: {e}\n')
    