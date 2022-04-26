import random

lotto_list = []
print("creating 100 random lottery tickets")
for i in range(100):
    lotto_list.append(random.randrange(1000000000, 9999999999))
winners = random.sample(lotto_list, 2)
print("Lucky 2 Lottery tickets are ", winners)

import random

name = 'pynative'
char = random.choice(name)
print("random char is", char)

import random
import string


def randomString(string_length):
    """"Generate a random string of 5 characters"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))


print("Random String is ", randomString(5))

import random
import string


def randomPassword():
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(random_source, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


print("Password is ", randomPassword())

import random
num1 = random.random()
print("First Random float is ", num1)
num2 = random.uniform(9.5, 99.5)
print("Second Random float is ", num1)
num3 = num1 * num2
print("Multiplication is ", num3)

import secrets
print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))

import random
dice = [1, 2, 3, 4, 5, 6, 7]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))
    
import random
import time


def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, " and ", endDate)
    random_generator = random.random()
    date_format = '%m/%d/%Y'
    start_time = time.mktime(time.strptime(startDate, date_format))
    end_time = time.mktime(time.strptime(endDate, date_format))

    random_time = start_time + random_generator * (end_time - start_time)
    random_date = time.strftime(date_format, time.localtime(random_time))
    return random_date


print("Random Date = ", getRandomDate("1/1/2016", "12/12/2019"))
