# Booking script

Yes, I know it is bad :D 

## How to use it

### Initial setup, only needed once

> !!!! PYTHON3 IS REQUIRED !!!!

```bash
$ python -m venv .
$ source ./bin/activate
$ pip install -r requirements.txt
```

### How to run the script from the script folder
```bash
$ source ./bin/activate
$ python main.py --help
usage: main.py [-h] [--birthday dd-mm-yyyy] [--surname SURNAME] [--name NAME] [--email EMAIL] [--phone PHONE] [--gym {beest,hetlab}] [--day {Maandag,Dinsdag,Woensdag,Donderdag,Vrijdag,Zaterdag,Zondag}] [--time h:mm]

I need you data, jacket and motocycle

optional arguments:
  -h, --help            show this help message and exit
  --birthday dd-mm-yyyy
                        birthday
  --surname SURNAME
  --name NAME           just name
  --email EMAIL         email on which you've registered your account
  --phone PHONE         your mobile phone number
  --gym {beest,hetlab}  choose the gym you want to go
  --day {Maandag,Dinsdag,Woensdag,Donderdag,Vrijdag,Zaterdag,Zondag}
                        pick the day
  --time h:mm           pick the time (only 00 or 30 in mm is possible)

# For example
$ python main.py --birthday 1-12-1990 --surname Surname --name Name --gym beest --day Mondag --time '13:30' --email your@email.com --phone +31663829528
```
