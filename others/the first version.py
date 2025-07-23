with open("answers.txt", "r") as file, open("marks.txt", "r") as file_of_marks:
    file = list(map(lambda x: x.strip("\n"), file.readlines()))
    file_of_marks = list(map(lambda x: x.strip("\n"), file_of_marks.readlines()))
    file_of_marks = list(map(lambda x: x.split(" - "), file_of_marks))
    dct_of_marks = dict(file_of_marks)
    counter_of_answer, lst = 0, []
    kq = int(input("Количество вопросов в тесте:"))
    for i in range(int(input("Количество учеников:"))):
        name = input(f"Имя {i+1} ученика:")
        for j in range(kq):
            answer =  input(f"Ответ ученика {name} на {j+1} вопрос:")
            if answer == file[j]:
                counter_of_answer += 1
        mark = dct_of_marks[str(counter_of_answer)]
        print(f"Ученик {name} дал правильный ответ в {counter_of_answer} вопросах, получив оценку {mark}")
        fin_dct = {name: mark}
        lst.append(fin_dct)
        counter_of_answer = 0
    for li in lst:
        for key, value in li.items():
            print(f"{key}: {value}")