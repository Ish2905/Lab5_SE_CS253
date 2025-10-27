# Lab5_SE_CS253

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Use of eval()** | Security (Bandit) | 49 | Use of eval() is a high-severity security risk that allows for arbitrary code execution. | Removed the entire line eval("print('eval used')"). |
| **Mutable Default Arg** | Bug (Pylint) | 8 | logs=[] is a mutable default argument. The same list is shared across all function calls, causing unexpected behavior. | Removed the logs=[] parameter from the function definition and deleted the logs.append() line. |
| **Bare except** | Bug (Pylint) | 17 | except: is an overly broad exception. It catches all errors, hiding potential bugs and making debugging difficult. | Changed the bare except: to the specific except KeyError: to only catch the expected error. |
| **No with for loadData** | Bug (Pylint) | 24 | File is opened with open() but not in a with block. This can cause resource leaks if an error occurs before f.close(). | Rewrote loadData to use the with open(...) as f: syntax, which guarantees the file will be closed. |
| **No with for saveData** | Bug (Pylint) | 28 | Same as above. File is opened for writing without a with block, risking a resource leak. | Rewrote saveData to use the with open(...) as f: syntax for safe file handling. |
| **Unused Import** | Style (Pylint/Flake8) | 2 | The logging module is imported at the top of the file but is never used, adding unnecessary clutter. | Removed the line import logging. |
| **Potential KeyError** | Bug (Pylint/Runtime) | 21 | getQty accesses stock_data[item] directly, which will crash the program with a KeyError if the item doesn't exist. | Changed return stock_data[item] to return stock_data.get(item, 0) to safely return 0 for missing items. |