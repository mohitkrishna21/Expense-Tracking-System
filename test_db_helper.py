#Automated testing for db_helper using pytest
#This file is containing test cases for db_helper file

from backend import db_helper

#When ever you wanna do some kinda setup for your test like intialize some configuration or changing system path etc
#you will do that in a file called conftest.py
#Anything you wanna do common for test cases you can do that in a conftest

#fetch expenses from some date verify they are okay or not
def test_fetch_expenses_for_date_aug_15():
    expenses=db_helper.fetch_expenses_for_date("2024-08-15")
    #there is a separate database for testing called test_db but as of now we are using same database
    #the size of expenses should be 1 since i have only one record
    assert len(expenses)==1
    assert expenses[0]['amount']==10.0
    assert expenses[0]['category']=='Shopping'
    assert expenses[0]['notes']=='Bought potatoes'

#you can have multiple test cases for same function
def test_fetch_expenses_for_date_invalid_date():
    expenses=db_helper.fetch_expenses_for_date("9999-08-15")
    assert len(expenses)==0

def test_fetch_expense_summary_invalid_range():
    summary=db_helper.fetch_expense_summary("2099-08-15","2088-09-30")
    assert len(summary)==0
#you can write as many as test cases


    

