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

Here are my answers for the reflection.md file:

1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest: The easiest fixes were definitely deleting the eval() function and the unused import logging. They were just single lines to remove, and it was obvious why they were bad (one was a huge security risk, the other was just clutter).

Hardest: The hardest one to understand was the logs=[] (mutable default argument) issue. It's not a syntax error, so it looked fine. I had to understand the concept that the list is created only once, which is a weird Python thing. The fixes for loadData and saveData were also a bit harder because I had to rewrite several lines to use the with open... and try...except structure instead of just changing one word.


2. Did the static analysis tools report any false positives? If so, describe one example.
I didn't really see any false positives for the big issues. Everything the tools flagged, like the eval() , the bare except , and the mutable default argument, was a real problem that made the code buggy or insecure.


Pylint might have flagged other minor things, like using global stock_data, but in a small script like this, it's not really a false positive, just a style guideline that I chose to use. So for this lab, no, all the main warnings were valid.

3. How would you integrate static analysis tools into your actual software development workflow?
I'd use them in two main places:

Locally: I would set up a pre-commit hook. This would automatically run Flake8  (for style) and Bandit  (for security) every time I try to git commit. It would stop me from committing messy or insecure code in the first place.


In CI (Continuous Integration): I would set up a GitHub Actions workflow. This would run all the tools (Pylint, Flake8, Bandit) automatically every time someone pushes code to the repository. If any tool finds a high-severity issue, the build would fail, and it would block the bad code from being merged into the main branch.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
The code is so much better now.

Robustness: This is the biggest win. The app won't crash anymore if I ask for an item that isn't in stock (from fixing getQty) or if the inventory.json file is missing (from fixing loadData).

Security: It's actually secure now that the eval() hole is gone.

Readability: It's much cleaner. Using with open... makes the file handling clearer. Also, replacing the bare except:  with except KeyError: makes it obvious what error we're expecting, which makes it way easier to debug.