# class Player:
#     def __init__(self, name):
#         self.name = name

#     def run(self):
#         print('You are running')

# player1 = Player('Peter')
# player1.run()

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('peny', 2)
cat2 = Cat('tom', 1)
cat3 = Cat('jerry', 4)



# 2 Create a function that finds the oldest cat
def find_oldest(*args):
    return max(args)

oldest_cat = find_oldest(cat1.age, cat2.age, cat3.age) 

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat} years old')