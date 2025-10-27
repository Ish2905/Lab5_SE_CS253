import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0): #FIX 2: REMOVE logs=[]
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    #logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item)) 

def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError: #FIX 3: KeyError
        print(f"Warning: Item '{item}' not found, cannot remove.") 

def getQty(item):
    return stock_data[item]

def loadData(file="inventory.json"): #FIX 4: using with 
    try:
        with open(file, "r") as f:
            global stock_data
            stock_data = json.load(f) # Use json.load(f) for file objects
    except FileNotFoundError:
        print(f"Warning: '{file}' not found. Starting with empty inventory.")
        global stock_data
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode '{file}'. Starting with empty inventory.")
        global stock_data
        stock_data = {}

def saveData(file="inventory.json"):
    with open(file, "w") as f:
        json.dump(stock_data, f, indent=4) # FIX 5: USE WITH

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, no check
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    # eval("print('eval used')")  # FIX 1: REMOVED THIS LINE FOR SECURITY ISSUE.
    print("\nInventory check complete.")
main()