# banking

It's study project from hyperskill.org course.<br>
Here's 4 stages of this project - objectives and output samples:

[stage 1](https://hyperskill.org/projects/109/stages/591/implement)
Basically explains theory for create bank_card_number and menu.<br>
[stage 2](https://hyperskill.org/projects/109/stages/592/implement)
Add Luhn algorithm to program.<br>
[stage 3](https://hyperskill.org/projects/109/stages/593/implement)
Add login menu and SQLite database.<br>
[stage 4](https://hyperskill.org/projects/109/stages/594/implement)
Add money transfer, delete account features to program.
# How to run program?

If you use `<venv>` (I highly recommend do this) 

First, make new `<venv>`:
```
$ python3 -m venv venv
```
Second, activate it and install needed packages:
```$ source venv/bin/activate
(venv)$ pip3 install -r requirements.txt
(venv)$ ./banking.py
```
  
After work don't remember exit venv:
```
(venv)$ deactivate
```

## Sample program output.
Some commands:<br>
![image](https://github.com/ksemele/banking/blob/master/pics/simple.png)

If you uncomment temporary printing in `banking.py` you must see all accounts from `card.s3db`:<br>
![image](https://github.com/ksemele/banking/blob/master/pics/tmp_print.png)
