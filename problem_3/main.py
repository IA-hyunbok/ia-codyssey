import csv
import pickle

file_path = 'Mars_Base_Inventory_List.csv'
output_file_path = 'output.csv'
error_path = 'error.log'
binary_output_file_path = 'Mars_Base_Inventory_List.bin'


try:
    data = open (file_path,'r',encoding='UTF-8')
    data_reader = csv.reader(data)
    data_list = list()
    for line in data_reader:
        data_list.append(line)
    print('csv파일 내용 :')
    print(data_list)
    data_list.sort(key=lambda x : x[4], reverse = True)

    high_Flamm=list()
    for col in data_list:
        try:
            if float(col[4])>=0.7:
                high_Flamm.append(col)
        except ValueError:
            continue
    print('인화성이 0.7 넘는 목록 :')
    print(high_Flamm)

    with open(output_file_path, 'w', newline='', encoding='UTF=8') as output:
        csv_writer = csv.writer(output)
        csv_writer.writerow(['Substance','Weight (g/cm³)', 'Specific Gravity', 'Strength', 'Flammability'])
        csv_writer.writerows(high_Flamm)
    
    with open(binary_output_file_path, 'wb') as binary_output:
        pickle.dump(data_list, binary_output)

    print('이진파일 내용 :')
    with open(binary_output_file_path, 'rb') as binary_input:
        loaded_data = pickle.load(binary_input)
        for item in loaded_data:
            print(item)
except Exception as e:
    print(f'오류!\n오류내용 : {e}')
    with open(error_path, 'a', encoding='UTF-8') as error_log:
        error_log.write(f'오류 발생! 오류 내용: {e}\n')
