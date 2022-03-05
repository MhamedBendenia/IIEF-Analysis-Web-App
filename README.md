# IIEF-Analysis-Web-App

IIEF stands for International Index of Erectile Function and is the gold standard of erection assessment and used by all leading erectile dysfunction researchers. The app offers a small web service written with Django REST framework, which calculates the IIEF score. It consists of five questions, each with five options to answer:

1 – Over the last 6 months, how do you rate your confidence that you could get and keep an
erection? Options: Very low / Low / Moderate / High / Very high

2 – Over the last 6 months, when you had an erection with sexual stimulation, how often was it
hard enough for penetration? Options: Almost never or never / A few times / Sometimes /
Most times / Almost always or always

3 – Over the past 6 months, during sexual intercourse, how often were you able to maintain your
erection after you had penetrated your partner? Options: Almost never or never / A few times /
Sometimes / Most times / Almost always or always

4 – Over the past 6 months, during sexual intercourse, how difficult was it to maintain your
erection to completion of intercourse? Options: Extremely difficult / Very difficult / Difficult /
Slightly difficult / Not difficult

5 – Over the last 6 months, when you attempted sexual intercourse, how often was it satisfactory
for you? Options: Almost never or never / A few times / Sometimes / Most times / Almost
always or always

Each answer is assigned a value from one to five points: 'Very low', 'Almost never or never' and
'Extremely difficult' being one point, 'Low', 'A few times' and 'Very difficult' being two points and so forth up to 'Very high', 'Almost always or always' and 'Not difficult' being five points.


A patient should give exactly one answer to each question. The sum of the values corresponding to the
given answer is called the IIEF score and lies between 5 and 25.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Tests

```bash
python3 manage.py test
```
