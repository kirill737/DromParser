import pandas as pd
from matplotlib import pyplot as plt

import numpy as np
import seaborn as sns




def show_analyt():
    data = pd.read_csv('result.csv')
    numeric = ['year', 'price', 'liters', 'horse_power', 'name', 'type', 'another_type', 'engine']
    data.head()

    def pr_criteria():
        return "Выберите номер критерия: \n 1 - год \n 2 - стоимость \n 3 - литраж \n 4 - л.с \n 5 - название \n 6 - бензин/дизель \n 7 - АКПП/МКПП \n 8 - Полноприводный да/нет"

    def min_value(column_name):
        return min(data[column_name])

    def max_value(column_name: str) -> float:
        return max(data[column_name])

    def average_value(column_name: str) -> float:
        return round(np.mean(data[column_name]), 0)


    contin = True
    guide = open('guide.txt', 'r')
    print(guide.read())
    guide.close()
    print("Введите что угодно, кроме числа, чтобы выйти")
    while contin:
        case = input()
        if case.isdigit():
            
            case = int(case)
            if case == 1:
                print("Введите: \n 1 - общая корреляция численных значений \n 2 - корреляция категорий")

                undercase = int(input())

                if undercase == 1:
                    sns.heatmap(data[numeric[:4]].corr(method='spearman'))
                    plt.show()
                elif undercase == 2:
                    sns.heatmap(pd.crosstab(data['name'], data['type']), cmap="YlGnBu", annot=True, cbar=False)
                    plt.show()
                    
            elif case == 2:
                print("Критерий, по которому будем смотреть распределение")
                print(pr_criteria())
                undercase = int(input()) - 1 
                if undercase < 8 and undercase >= 0:
                    fig = plt.figure()
                    fig.set_size_inches(5, 4)
                    plt.hist(data[numeric[undercase]])
                    plt.show()
                    print("распределение критерия")
                else:
                    print("ошибка")

            elif case == 3:
                print("Выберите критерий, чтобы увидеть максимальное и минимальное значения:")
                print(pr_criteria()[:75])
                undercase = int(input()) - 1 
                if undercase < 5 and undercase >= 0:
                    print("Минимальное значение", min_value(numeric[undercase]))
                    print("Максимальное значение", max_value(numeric[undercase]))

                else:
                    print("ошибка")

            elif case == 4:
                print("Выберите критерий, чтобы увидеть среднее значение")
                print(pr_criteria()[:75])

                undercase = int(input()) - 1 
                if undercase < 5 and undercase >= 0:
                    print("Среднее значение", average_value(numeric[undercase]))
                
                    
        else:
            contin = False

    return None


