# [itp-w2] Hangman

Today we are going to re-create the game 'Hangman' in Python!

It is broken down into several small functions that, when combined and
completed, form a working game!

Use docstrings (comments below function definitions) and unit tests to guide 
your coding. To do so, we'll make use of more advanced features of Py.test.

#### make test

Up to this point, you've just used `make test` to run your tests. If you read the `Makefile` you'll see that `make test` is just an alias for `PYTHONPATH=. py.test -s tests`. Breaking it down:

* `PYTHONPATH=.`: sets the PYTHONPATH in the current directory. Don't worry much about it. We talk about it in detail in the Advanced Python course 😉
* `py.test`: The Py.test command
* `-s tests`: It's just indicating Py.test to run all the tests in the `tests` directory.

Try running this by yourself in the command line and see that it does the same thing as `make test`: `PYTHONPATH=. py.test -s tests`

#### Running a single test

Now we want to start looking at the functions in `main.py` and implement them. But if we run all the tests, we get a huge stacktrace that's not useful at all. We want to tackle functions one by one, and to do so, we want to run tests one by one. For example, we want to work on the `_get_random_word` function. To make sure it's correct we want to use the test [`test_get_random_word`](https://github.com/rmotr-group-projects/itp-w2-hangman/blob/master/tests/test_main.py#L10). **How can we run just that one particular test?** Simple, just use the `-k` argument of Py.test. `-k` takes a string as input and runs all the tests that match that string. We could do for example:

```sh
$ PYTHONPATH=. py.test -s tests -k test_get_random_word
```

That'll run just the test `test_get_random_word`. Please note that we're still using the base part of the command: `PYTHONPATH=. py.test -s tests`.

#### Tidy the results

When we just start our project we run our tests and it's just one big pile of red messages that make no sense. For example, this is how running tests with this empty project looks like:

![image](https://cloud.githubusercontent.com/assets/872296/22155266/98cb3a96-df0d-11e6-961d-e1b9cf647bce.png)

There's no useful information aside than seeing that 20 tests failed. That's because we're inlcuding the "stacktrace" for all our failing tests. The stacktrace is useful when we're debugging a particular error (something not working ok), but in this case it's just noise. The way to get rid of it is by using the `--tb` option (stands from "traceback"). We could do for example `--tb=no`. This is how it looks like:

![image](https://cloud.githubusercontent.com/assets/872296/22155375/f7d16308-df0d-11e6-95f5-28773f8263ff.png)

If you combine it with the `-v` option, you get:

![image](https://cloud.githubusercontent.com/assets/872296/22155432/277793a2-df0e-11e6-854a-38bef83b40f2.png)

Try running different options for `--tb` like `--tb=line` or `--tb=short` and combine them with `-v`.
