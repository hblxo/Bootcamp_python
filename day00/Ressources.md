# Day00 - Basics

Let's get started with the Python language! 🐍

    *Notions : Basic setup, variables, types, functions, ...*

***

## Install

*copy in ~/.zshrc :*

```bash
function set_conda {
	HOME=$(echo ~)
    INSTALL_PATH="/goinfre"
    MINICONDA_PATH=$INSTALL_PATH"/miniconda3/bin"
    PYTHON_PATH=$(which python)
    SCRIPT="Miniconda3-latest-MacOSX-x86_64.sh"
    REQUIREMENTS="jupyter numpy pandas"
    DL_LINK="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"

	if echo $PYTHON_PATH | grep -q $INSTALL_PATH; then
		echo "good python version :)"
	else
	cd
	if [ ! -f $SCRIPT ]; then
		curl -LO $DL_LINK
		fi
		if [ ! -d $MINICONDA_PATH ]; then
			sh $SCRIPT -b -p $INSTALL_PATH"/miniconda3"
	fi
	conda install -y $(echo $REQUIREMENTS) clear
	echo "Which python:"
	which python
	if grep -q "ˆexport PATH=$MINICONDA_PATH" ~/.zshrc
	then
		echo "export already in .zshrc";
	else
		echo "adding export to .zshrc ...";
		echo "export PATH=$MINICONDA_PATH:\$PATH" >> ~/.zshrc
	fi
	source ~/.zshrc
	fi
}

```

```bash
source ~/.zshrc ;
set_conda
```

```bash
which python
```

## Ressources externes

---

- Syntaxe if/else:

    ```python
    if expression1:
    statement(s)
    elif expression2:
    statement(s)
    else:
    statement(s)
    ```

    - [Python IF...ELIF...ELSE Statements](https://www.tutorialspoint.com/python/python_if_else.htm)

- String methods

    ```python
    >>> s = “Whereof one cannot speak, thereof one must be silent.”
    >>> s
    'Whereof one cannot speak, thereof one must be silent.'
    >>> s.upper()
    'WHEREOF ONE CANNOT SPEAK, THEREOF ONE MUST BE SILENT.'
    >>> s.lower()
    'whereof one cannot speak, thereof one must be silent.'
    ```

    - [Python String Methods: str(), upper(), lower(), count(), find(), replace() & len() - Python - The Hello World Program](https://thehelloworldprogram.com/python/python-string-methods/)

    - [isupper(), islower(), lower(), upper() in Python and their applications - GeeksforGeeks](https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/)

    - [Python String split() Method](https://www.tutorialspoint.com/python/string_split.htm)

- Arguments

    ```python
    def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello",name)

    greet("Monica","Luke","Steve","John")
    ```

    - [Python Function Arguments](https://www.programiz.com/python-programming/function-argument)

- String iteration

    - [Python - Strings](https://www.tutorialspoint.com/python/python_strings.htm)

- Tuple iteration

    - [How to iterate through a tuple in Python?](https://www.tutorialspoint.com/How-to-iterate-through-a-tuple-in-Python)

- Print method

    ```python
    print("Python is fun.")

    a = 5
    # Two objects are passed
    print("a =", a)

    b = a
    # Three objects are passed
    print('a =', a, '= b')
    ```

    - [Python print()](https://www.programiz.com/python-programming/methods/built-in/print)

- Dict

  - [Python dictionary get() Method](https://www.tutorialspoint.com/python/dictionary_get.htm)

    ```python
    for key, value in cookbook.items():
            print("Ingredients list:", value.get('ingredients'))
            print("To be eaten for", value.get('meal'))
            print("Takes", value.get('prep_time'), " minutes of cooking.")
    ```

  - [Built-in Types - Python 3.8.2 documentation](https://docs.python.org/3/library/stdtypes.html#dict.pop)

- Assert statement

  - [What is the use of "assert" in Python?](https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python)

- Others

  - [http://hplgit.github.io/primer.html/doc/pub/input/._input-readable007.html](http://hplgit.github.io/primer.html/doc/pub/input/._input-readable007.html)

  - [https://www.tutorialspoint.com/python/time_strftime.htm](https://www.tutorialspoint.com/python/time_strftime.htm)

  - [https://docs.python.org/3/library/cmath.html?highlight=conversion](https://docs.python.org/3/library/cmath.html?highlight=conversion)