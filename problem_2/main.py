import json

file_path = 'mission_computer_main.log'
output_file_path = 'error.log'

log_list = list()
try:
    with open(file_path, 'r', encoding='UTF-8') as log:
        log_list = log.readlines()
    log_list = [line.strip().split(',', 2) for line in log_list]
    print(log_list)

    log_list.sort(key=lambda x: x[0], reverse=True)

    log_dict = []
    for entry in log_list:
        time, log_type, detail = entry
        data = {
            'Time': time,
            'Type': log_type,
            'Detail': detail.strip(),
        }
        log_dict.append(data)
    print(log_dict)

    with open('mission_computer_main.json', 'w') as js:
        json.dump(log_dict, js, indent=4)

    search_str = str(input('검색단어 : '))
    for entry in log_dict:
        if search_str in entry['Detail']:
            print(f"Time: {entry['Time']}, Type: {entry['Type']}, Detail: {entry['Detail']}")

except Exception as e:
    print(f'오류!\n오류내용 : {e}')
    with open(output_file_path, 'a', encoding='UTF-8') as error_log:
        error_log.write(f'오류 발생! 오류 내용: {e}\n')
