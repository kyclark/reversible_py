# Find Reversible Words

Can figure out what these words have in common?

* Banana
* Dresser
* Grammar
* Potato
* Revive
* Uneven
* Assess

No, it is not that they all have at least 2 double letters.

In all of the words listed, if you take the first letter, place it at the end of the word, and then spell the word backwards, it will be the same word.

The `reversible.py` Python program will find such words in a given text file.
For example, given this file:

```
$ cat test.txt
weasels
banana
rip
dresser
my
grammar
flesh
```

The program will find three words:

```
$ ./reversible.py -f test.txt
banana
dresser
grammar
```

By default, the program will use `/usr/share/dict/words`.
On my system, it find 546 such words:

```
$ ./reversible.py | wc -l
     546
```

Run `pytest` to execute tests:

```
$ pytest -v
========================== test session starts ===========================
...
collected 3 items

reversible_test.py::test_exists PASSED                             [ 33%]
reversible_test.py::test_usage PASSED                              [ 66%]
reversible_test.py::test_file PASSED                               [100%]

=========================== 3 passed in 0.25s ============================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
