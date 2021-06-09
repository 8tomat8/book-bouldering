import argparse
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

days = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']
gyms = {
    'beest': 'http://mijn.klim.nl/beest-asd?p=118',
    'hetlab': 'http://mijn.klim.nl/het-lab?p=121',
}

parser = argparse.ArgumentParser(description='I need you data, jacket and motocycle')
parser.add_argument('--birthday', metavar='dd-mm-yyyy', type=str, help='birthday')
parser.add_argument('--surname', type=str)
parser.add_argument('--name', type=str, help='just name')
parser.add_argument('--email', type=str, help='email on which you\'ve registered your account')
parser.add_argument('--phone', type=str, help='your mobile phone number')
parser.add_argument('--gym', type=str, choices=[k for k in gyms.keys()], help='choose the gym you want to go')
parser.add_argument('--day', type=str, choices=days, help='pick the day')
parser.add_argument('--time', type=str, metavar='h:mm', help='pick the time (only 00 or 30 in mm is possible)')
args = parser.parse_args()

people = {
    'email':   args.email,
    'name':    args.name,
    'surname': args.surname,
    'mobile':  args.phone,
    'birthday': {
        'day':   args.birthday.split('-')[0],
        'month': args.birthday.split('-')[1],
        'year':  args.birthday.split('-')[2],
    },
}

def main(driver: WebDriver):
    driver.get(gyms[args.gym])

    # First page (subscription type)
    #  button = driver.find_element_by_id('ubtn-1199')
    #  if not button:
        #  raise Exception('Didn\'t finc the `RESERVEREN` button')
#  
    #  button.click()

    # Second page (email validation)
    #  email_form = driver.find_element_by_class_name('putEmail')
    #  if not email_form:
        #  raise Exception('Didn\'t find the email form')

    #  email_input = email_form.find_element_by_name('email')
    #  if not email_input:
        #  raise Exception('Didn\'t find the email input field')
#  
    #  email_input.send_keys(people['email'])
    #  email_submit_btn = email_form.find_element_by_class_name('checkemail')
    #  if not email_submit_btn:
        #  raise Exception('Didn\'t find the email submit btn')
#  
    #  email_submit_btn.click()

    # Third page (time selector)
    rows = driver.find_element_by_class_name('groupedPerDayViewTable').\
        find_element_by_tag_name('tbody').\
        find_elements_by_tag_name('tr')

    time_to_book = args.time + ' uur'
    found_time = False
    #  for slot in time_slots:
    for row in rows:
        try:
            dayCol = row.find_element_by_xpath('.//td[@class="dayColumn"]')
        except:
            # It is fine as only some rows have a day column
            pass

        if dayCol.text != args.day:
            continue

        # Skipping wrong time
        try:
            timeCol = row.find_element_by_xpath('.//td[@class="timeColumn"]')
        except:
            # skip a row if it has no time column to check
            pass

        if timeCol.text != time_to_book:
            continue

        try:
            link = row.find_element_by_xpath('.//td[@class="linkColumn"]/div/a')
        except NoSuchElementException:
            continue

        link.click()
        found_time = True
        break

    if not found_time:
        raise Exception('No link for your time was found :(. Probably all booked')

    # Fourth page (personal data)
    driver.find_element_by_name('booker[firstname]').send_keys(people['name'])
    driver.find_element_by_name('booker[surname]').send_keys(people['surname'])
    driver.find_element_by_name('booker[email]').send_keys(people['email'])
    driver.find_element_by_name('booker[mobile]').send_keys(people['mobile'])

    driver.find_element_by_id('birthDateDay').send_keys(people['birthday']['day'])
    driver.find_element_by_id('birthDateMonth').send_keys(people['birthday']['month'])
    driver.find_element_by_id('birthDateYear').send_keys(people['birthday']['year'])

    btn = driver.find_element_by_class_name('navbtnnext')
    if 'VERDER' not in btn.text.lower():
        raise Exception('Something wrong with the CONTINIE button...')
    
    btn.click()

    # Fifth page (data processing shit...)
    driver.find_element_by_name('accept').click()

    btn = driver.find_element_by_tag_name('button')
    if 'voltooien' not in btn.text.lower():
        raise Exception('Something wrong with the CONTINIE button...')
    
    btn.click()

    return


if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:
        main(driver)
    except Exception as e:
        print(e)
    else:
        print('Successfull booking ;)')

    driver.quit()
