# Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
print(voting_data)



# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'votin_data' is not defined. Did you mean: 'voting_data'?
# >>> voting_data
# [{'county': 'Arapahoe', 'registered_voters': 422829}]
# >>> voting_data.append({"county":"Denver","registered_voters":463353})
# >>> voting_data.append({"county":"Jefferson","registered_voters":432438})
# >>> voting_data
# [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
# >>> len(voting_data)
# 3
# >>> voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
# >>> voting_data
# [{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
# >>> voting_data.remove({'county":"Arapahoe","registered_voters":422829})
#   File "<stdin>", line 1
#     voting_data.remove({'county":"Arapahoe","registered_voters":422829})
#                         ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> voting_data.remove({county":"Arapahoe","registered_voters":422829})
#   File "<stdin>", line 1
#     voting_data.remove({county":"Arapahoe","registered_voters":422829})
#                               ^^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> voting_data.remove(0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
# >>> voting_data.pop(0)
# {'county': 'Arapahoe', 'registered_voters': 422829}
# >>> voting_data
# [{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
# >>> voting_data.append({'county': 'Denver', 'registered_voters': 463353})
# >>> voting_data.pop(2)
# {'county': 'Jefferson', 'registered_voters': 432438}
# >>> voting_data.insert(2,{'county': 'Jefferson', 'registered_voters': 432438})
# >>> voting_data
# [{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}]
# >>> voting_data.pop(1)
# {'county': 'Denver', 'registered_voters': 463353}
# >>> voting_data.append({'county': 'Arapahoe', 'registered_voters': 422829})
# >>> voting_data
# [{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
# >>> {'county': 'Arapahoe', 'registered_voters': 422829}
# {'county': 'Arapahoe', 'registered_voters': 422829}
# >>> ls
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'ls' is not defined
# >>>
