import pytest
import pandas as pd
# from test_tool.tool_for_test import *
from clean_data.clean_text.guess_by_root import *


class Employee(object):
    def Work(self):
        pass


class Manager():
    def __init__(self):
        self.employees = []

    def addEmployee(self, a):
        self.employees.append(a)


class Developer(Employee):
    def __init__(self):
        print("developer added")

    def Work(self):
        print("turning coffee into code")


class Designer(Employee):
    def __init__(self):
        print("designer added")

    def Work(self):
        print("turning lines to wireframes")


class Testers(Employee):
    def __init__(self):
        print("tester added")

    def Work(self):
        print("testing everything out there")



if __name__ == "__main__":
    a = Manager()
    a.addEmployee(Developer())
    a.addEmployee(Designer())
    for i in a.employees:
        i.Work()

# print(df["text"])
# def a(x, **kwargs):
#     print(kwargs["q"])
# def s(x, ** kwargs):
#     a(x, **kwargs)
#
# def l(x, **kwargs):
#     s(x, **kwargs)
# l(2, q="333")
# guess = RootGuess(df, "text", bag_words=bag_words,
#                           bag_sentences=bag_sentences, num_decision=2,
#                           name_output_col="text")
# s = guess.guess()
#
#
# target = pd.DataFrame({"guess": ["fever",
#                                         "fever,myalgia,weakness",
#                                         np.nan,
#                                         "cough,fever",
#                                         "fever,dysphagia,weakness,fatigue",
#                                         "fever,cough"]})
#
# col_a = s["guess"]
# col_b = target["guess"]
# print(col_b.name )
# df = pd.concat([col_a, col_b], axis=1)
# df["test"] = df.apply(
#     lambda x: Tool.compere_values_without_order(x[0], x[1]), axis=1)
# print(df["test"].all() == True)


# print(result)
# # class Animal:
#     def __init__(self, name, if_eat):    # Constructor of the class
#         self.name = name
#         self.if_eat = if_eat
#
#     def talk(self):              # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Cat(Animal):
#     def __init__(self, name, if_eat, leg):
#         super().__init__(name, if_eat)
#         self.leg = leg
#
#     def talk(self):
#         return 'Meow!'
#
# class Dog(Animal):
#     def talk(self):
#         return 'Woof! Woof!'
#
# class Snak(Animal):
#     def talk(self):
#         return "ssssssss"
# param= {"name":'Missy',
#         "if_eat":"yes",
#         "leg": 4}
# animals = [Cat(**param)]
#            # Dog('Lassie'),
#            # Snak("soffia")]
#
# for animal in animals:
#     print (animal.name + ': ' + animal.talk())
# m = Cat('Missy', 6 )
# print(m.name)

# class UserStore():
#     """
#     The base class for accessing a user's information.
#     The client must extend this class and implement its methods.
#     """
#     def get_name(self, token):
#         raise NotImplementedError
#
#
# class AlwaysMaryUser(UserStore):
#     def get_name(self, token):
#         return 'Mary'

# class SQLUserStore(UserStore):
#     def __init__(self, db_params):
#         self.db_params = db_params
#
#     def get_name(self, token):
#         # TODO: Implement the database lookup
#         raise NotImplementedError
#
# class WebFramework():
#     def __init__(self, user_store: UserStore):
#         self.user_store = user_store
#
#     def greet_user(self, token):
#         user_name = self.user_store.get_name(token)
#         print(f'Good day to you, {user_name}!')
#
#
# client = WebFramework(AlwaysMaryUser())
# client.greet_user('user_token')

# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# greet_me(name="yasoob", limon = "rfrfr")
#
# df = pd.DataFrame({"text": ["fever  ", "Mild to moderate",
#                             "Mild:moderate ", "cough, fever  ",
#                             "  cough   ", "Respiratory symptoms ",
#                             "eye irritation, fever ", "respiratory complaints ",
#                             "chest pain, respiratory distress, fever, dysphagia, asthenia, weakness, fatigue " ,
#                             "fever:cough:acute respiratory distress syndrome "]})
# bag_words = {}
# bag_sentences = {}
# num_decision = 2
# guess = RootGuess(df, "text", bag_words, bag_sentences, num_decision)
#
# simple_df = pd.DataFrame({"text": ["a", "ab", "c  f s", "b"]})
# simple_ex = RootGuess(simple_df, "text", bag_words, bag_sentences, num_decision=2)
# simple_result = simple_ex.df[simple_ex.col]
#
# result = simple_ex.get_dummies_from_input_col()
#
# print(result == target)



