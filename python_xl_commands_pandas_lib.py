Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\shahr\OneDrive\Desktop\Python\Python-Exercise\Ex_HTTPRequestAndJSON.py =
Program for a quizzing game
Which is not a type of neuron?

Motor Neuron
Sensory Neuron
Interneuron
Perceptual Neuron

= RESTART: C:\Users\shahr\OneDrive\Desktop\Python\Python-Exercise\Ex_HTTPRequestAndJSON.py =
Program for a quizzing game
What is Everest&#039;s favorite food in the Nickelodeon/Nick Jr. series &quot;PAW Patrol&quot;?

Traceback (most recent call last):
  File "C:\Users\shahr\OneDrive\Desktop\Python\Python-Exercise\Ex_HTTPRequestAndJSON.py", line 27, in <module>
    print(str(answer_number) + "- " + answer)
NameError: name 'answer_number' is not defined
>>> 
= RESTART: C:\Users\shahr\OneDrive\Desktop\Python\Python-Exercise\Ex_HTTPRequestAndJSON.py =
Program for a quizzing game
In "Star Trek", Klingons respect William Shakespeare, they even suspect him having a Klingon lineage.

1- False
2- True
true
The LS2 engine is how many cubic inches?

1- 364
2- 402
3- 346
4- 376

= RESTART: C:\Users\shahr\OneDrive\Desktop\Python\Python-Exercise\Ex_HTTPRequestAndJSON.py =
Program for a quizzing game
From which country does the piano originate?

1- France
2- Italy
3- Germany
4- Austria
Ans: 
Italy 
Press enter to keep playing or type 'quit' to end the game: 
Your answer is incorrect
Your Score:  0
Which character is from "Splatoon"?

1- Marie
2- Cyrus
3- Palutena
4- Shulk
Ans: 
Shulk
Press enter to keep playing or type 'quit' to end the game: 
Your answer is incorrect
Your Score:  0
The 2016 United States Presidential Election is the first time Hillary Clinton has run for President.

1- False
2- True
Ans: 
True
Press enter to keep playing or type 'quit' to end the game: 
Your answer is incorrect
Your Score:  0
Which of these book series is by James Patterson?

1- The Legend of Xanth
2- Maximum Ride
3- The Bartemaeus Trilogy
4- Harry Potter
Ans: 
Maximum Ride
Press enter to keep playing or type 'quit' to end the game: 
Your answer is correct
Your Score:  1
About how old is Earth?

1- 3.5 Billion Years
2- 4.5 Billion Years
3- 5.5 Billion Years
4- 2.5 Billion Years
Ans: 
4.5 Billion Years
Press enter to keep playing or type 'quit' to end the game: 
Your answer is correct
Your Score:  2
Who voiced Finn in Adventure Time?

1- John DiMaggio
2- Jeremy Shada
3- Tom Kenny
4- Nolan North
Ans: 
Tom Kenny
Press enter to keep playing or type 'quit' to end the game: 
Your answer is incorrect
Your Score:  2
"PAYDAY: The Heist" is a sequel to the board game "Payday".

1- False
2- True
Ans: 
True
Press enter to keep playing or type 'quit' to end the game: quit
Your answer is incorrect
Your Score:  2
Your final score:  2
>>> import pandas as pd
file = pd.ExcelFile
>>> file = pd.ExcelFile("C:\Users\shahr\OneDrive\Desktop\original.xlsx")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> file = pd.ExcelFile("C:/Users/shahr/OneDrive/Desktop/original.xlsx")
>>> print(file.sheet_names)
['sales', 'customers']
>>> sheet = file.parse('sales')
>>> print(sheet)
        Date             Customer  Invoice  Amount
0 2018-12-01  Steel Brothers Inc.       98    1340
1 2018-12-10             MMC Inc.       99    1900
2 2018-12-12             MMC Inc.      100    2900
3 2018-12-18  Steel Brothers Inc.      101     977
4 2018-12-21     Steel & Iron LLC      102    3400
>>> type(sheet)
<class 'pandas.core.frame.DataFrame'>
>>> print(sheet.Date)
0   2018-12-01
1   2018-12-10
2   2018-12-12
3   2018-12-18
4   2018-12-21
Name: Date, dtype: datetime64[ns]
>>> sheet.Amount.sum()
10517
>>> sheet.loc[0]
Date        2018-12-01 00:00:00
Customer    Steel Brothers Inc.
Invoice                      98
Amount                     1340
Name: 0, dtype: object
>>> sheet.loc[0, "Amount"]
1340
>>> sheet.set_index("Customer", inplace = True)
>>> sheet.loc["MMC Inc."]
               Date  Invoice  Amount
Customer                            
MMC Inc. 2018-12-10       99    1900
MMC Inc. 2018-12-12      100    2900
>>> sheet = sheet.reset_index()
>>> sheet["Invoice"]
0     98
1     99
2    100
3    101
4    102
Name: Invoice, dtype: int64
>>> sheet.loc[sheet["Amount"] > 2000]
           Customer       Date  Invoice  Amount
2          MMC Inc. 2018-12-12      100    2900
4  Steel & Iron LLC 2018-12-21      102    3400
>>> sheet.loc[sheet["Amount"].idxmax()]
Customer       Steel & Iron LLC
Date        2018-12-21 00:00:00
Invoice                     102
Amount                     3400
Name: 4, dtype: object
>>> sheet.loc[sheet["Amount"].idxmax()]["Customer"]
'Steel & Iron LLC'
>>> sheet.loc[sheet["Amount"] > 1800]
           Customer       Date  Invoice  Amount
1          MMC Inc. 2018-12-10       99    1900
2          MMC Inc. 2018-12-12      100    2900
4  Steel & Iron LLC 2018-12-21      102    3400
>>> sheet.loc[sheet["Amount"] > 1800]["Customer"]
1            MMC Inc.
2            MMC Inc.
4    Steel & Iron LLC
Name: Customer, dtype: object
>>> sheet.loc[sheet["Amount"] > 1800]["Customer"].unique()
array(['MMC Inc.', 'Steel & Iron LLC'], dtype=object)
>>> sheet.loc[sheet["Amount"] > 1800]["Customer"][0]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    sheet.loc[sheet["Amount"] > 1800]["Customer"][0]
  File "C:\Python38\lib\site-packages\pandas\core\series.py", line 871, in __getitem__
    result = self.index.get_value(self, key)
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 4405, in get_value
    return self._engine.get_value(s, k, tz=getattr(series.dtype, "tz", None))
  File "pandas\_libs\index.pyx", line 80, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 90, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 997, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1004, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 0
>>> sheet.loc[sheet["Amount"] > 1800]["Customer"].unique()[0]
'MMC Inc.'
>>> for customer in sheet.loc[sheet["Amount"] > 1800]["Customer"].unique():
	print(customer)

MMC Inc.
Steel & Iron LLC
>>> 