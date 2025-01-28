# საკლასო დავალება:

# შექმენით ფუნქცია რომელიც მიიღებს ორ პარამეტრს - main_list, indexes_list.

# თქვენი დავალებაა, რომ indexes_list სიაში რა ინდექსებიც იქნება მოცემული, მთავარ სიაში, მაგ ინდექსებზე წაშალოთ ელემენტები
def popper(main_list,indexes_list):
    for i in main_list:
        main_list.pop(indexes_list)
    
            
    print(main_list)
        

    
# popper([3,5,6,8,9],2)
# შექმენით ფუნქცია სახელად remove_one_element, რომელსაც გადაეცემა სია და ინდექსი.

# სიიდან მაგ ინდექსზე მყოფი ელემენტი ამოშალეთ და დაბეჭდეთ სია.
# def remove(li,ind):
#     li.pop(ind)

    