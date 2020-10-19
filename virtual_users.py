import requests
import time
import getpass
import selenium
import time
import sys
import csv
import getpass
import os
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

default_target = "10.86.165.82"

options = Options()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

################### please comment this for UI result on Chrome ################
options.add_argument('headless')

def scrape_init(driver, username, password, email):

    driver.get("http://10.86.165.82")
    time.sleep(1)

    ############################# register ######################
    driver.get("http://10.86.165.82/register")
    print("Registering")
    time.sleep(1)
    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)
    print("your username:", username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)
    print("your password:", password)

    # Repeat the password
    pass_check_field = driver.find_element_by_name("pass_check")
    pass_check_field.clear()
    pass_check_field.send_keys(password)

    # Enter email
    email_field = driver.find_element_by_name("email")
    email_field.clear()
    email_field.send_keys(email)
    print("your email:", email)

    # Hit the button
    login_button = driver.find_element_by_xpath("/html/body/div/div/form[1]/button")
    login_button.click()
    print("Registered!")
    return scrape_login(driver, username, password)

def scrape_login(driver, username, password):
    ############################# login ######################
    driver.get("http://10.86.165.82/login")
    print("Logging in")
    time.sleep(1)

    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)

    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    # Hit the button
    login_button = driver.find_element_by_xpath("/html/body/div/div/form[1]/button")
    login_button.click()
    time.sleep(1)
    print("Logged in!")

def scrape_change_details(driver, username, new_em, new_pw):
    ############################### profile page ##########################
    driver.get("http://10.86.165.82/profile")
    time.sleep(1)

    ############################## change email ############################
    email_field = driver.find_element_by_name("email")
    print("Changing email")
    email_field.clear()
    email_field.send_keys(new_em)
    ce_button = driver.find_element_by_xpath("/html/body/div/div/div/form[1]/button")
    ce_button.click()
    print("Email changed, your new email is", new_em)
    time.sleep(1)

    ############################### change password ##########################
    pw_field = driver.find_element_by_name("password")
    print("Changing password")
    pw_field.clear()
    pw_field.send_keys(new_pw)
    ce_button = driver.find_element_by_xpath("/html/body/div/div/div/form[2]/button")
    ce_button.click()
    print("Password changed\nYour new password is:", new_pw)
    print("Re-logging in")
    driver.get("http://10.86.165.82/login")
    time.sleep(1)
    # Enter username
    username_field = driver.find_element_by_name("username")
    username_field.clear()
    username_field.send_keys(username)
    # Enter password
    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(new_pw)
    # Hit the button
    login_button = driver.find_element_by_xpath("/html/body/div/div/form[1]/button")
    login_button.click()
    print("Welcome back!")
    time.sleep(1)

def scrape_career_ahp(driver):
    ############################# resources page #########################
    driver.get("http://10.86.165.82/resources")
    time.sleep(2)

    ############################## career pages ############################
    driver.get("http://10.86.165.82/career")
    for i in range(5):
        career_button = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[{}]/input".format(i+1))
        info = career_button.get_attribute("value").replace(" ","_")
        career_button.click()
        time.sleep(1/2)
        driver.get("http://10.86.165.82/career-pdf/{}.pdf".format(info))
        time.sleep(1)
        driver.back()

    ############################# ahp page ##############################
    driver.get("http://10.86.165.82/academic-honesty-policy")
    time.sleep(1/2)
    driver.get("http://10.86.165.82/other_pdf/ahp.pdf")
    time.sleep(1)

def scrape_uos(driver):
    ############################# resources page #########################
    driver.get("http://10.86.165.82/resources")
    time.sleep(3/2)

    ###################################### unit pages ###############################
    driver.get("http://10.86.165.82/units")
    for i in range(4):
        login_button = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/h1[{}]".format(i+1))
        login_button.click()
        time.sleep(1/2)
        for j in range(7):
            try:
                unit_button = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/ul[{}]/li[{}]/input".format(i+1,j+1))
                unit_button.click()
                time.sleep(1)
                info = unit_button.get_attribute("value").replace(" ","_")
                time.sleep(1/2)
                driver.get("http://10.86.165.82/units-pdf/{}.pdf".format(info))
                time.sleep(3/2)
                driver.back()
                driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/h1[{}]".format(i+1)).click()
            except:
                pass

def scrape_computing_help(driver):
    ############################# resources page #########################
    driver.get("http://10.86.165.82/resources")
    time.sleep(2)

    ############################## computing help #########################
    driver.get("http://10.86.165.82/computing-help")
    for i in range(3):
        login_button = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[{}]/input".format(i+1))
        login_button.click()
        time.sleep(1)

def scrape_upload(driver):
    ############################# resources page #########################
    driver.get("http://10.86.165.82/resources")
    time.sleep(2)

    ############################## computing help #########################
    driver.get("http://10.86.165.82/computing-help")
    for i in range(3):
        login_button = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[{}]/input".format(i+1))
        login_button.click()
        time.sleep(1/2)
        ########################## upload resources ###############################
        iframe = driver.find_elements_by_tag_name("iframe")[0]
        driver.switch_to_frame(iframe)
        file = driver.find_element_by_name("myfile")
        path = os.path.abspath("README2.md")
        file.send_keys(path)
        time.sleep(1)
        click_button = driver.find_element_by_xpath("/html/body/form/input[2]")
        click_button.click()
        time.sleep(1)
        driver.switch_to.default_content()

        print("You uploaded README2.md")
        time.sleep(3/2)

def scrape_discussion(driver):
    ################################# post discussions #######################
    driver.get("http://10.86.165.82/posts")
    time.sleep(1)

    title_field = driver.find_element_by_name("title")
    title_field.clear()
    title_field.send_keys("I am not human")

    message_field = driver.find_element_by_name("text")
    message_field.clear()
    message_field.send_keys("I am just a virtual user, some human created me.\nLeave your comment below.")

    send_button = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/form/label[2]/input")
    send_button.click()
    time.sleep(2)

def scrape_admin_manage(driver):
    ################################# user manage ###################################
    driver.get("http://10.86.165.82/user-manage")
    time.sleep(1)
    delete_user_button = driver.find_element_by_xpath("/html/body/div/div/div/div/table/tbody/tr[4]/td[6]/button")
    delete_user_button.click()
    time.sleep(1)
    print("you deleted a user")

    # ################################# course manage #################################
    # driver.get("http://10.86.165.82/units")
    # button = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/h1[1]")
    # button.click()
    # time.sleep(1/2)
    # buttonu = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/ul[1]/li[3]/input")
    # buttonu.click()
    # button_delete_course = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/button")
    # button_delete_course.click()
    # time.sleep(1)
    # print("you deleted a course guide")

def scrape_messaging(driver):
    ################################# message page #####################################
    driver.get("http://10.86.165.82/message")
    try:
        search_contact_field = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/input")
        search_contact_field.clear()
        search_contact_field.send_keys("admin")

        search_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/i")
        search_button.click()
        time.sleep(1)

        add_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div/div[2]/div/div[2]/div/i")
        add_button.click()
        time.sleep(1)

        contact_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div[2]/a/i")
        contact_button.click()
        time.sleep(1)

        avatar_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div/div[4]/div/div[2]/div/div[2]/i")
        avatar_button.click()
        time.sleep(1)

        text_box = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[3]/div[1]/pre")
        text_box.send_keys("hello my friend, I am a virtual user")
        time.sleep(1)

        send_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[3]/div[2]/input")
        send_button.click()
        time.sleep(2)
        driver8.quit()
    except:
        driver.quit()
        #driver.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        target_url = default_target
    else:
        target_url = sys.argv[1]


    ################## please uncomment this block for another testing on register #####################
    # driver1 = webdriver.Chrome(options=options)
    # scrape_init(driver1, "virtual1", "Virtual123", "virtual@1.com")
    # scrape_change_details(driver1, "virtual1", "virtual@11.com", "Virtual321")
    # driver1.close()
    # print("Virtual user 1 finished")

    ################ please uncomment this block for again another testing on register ###########################
    # driver1 = webdriver.Chrome(options=options)
    # scrape_init(driver1, "virtual99", "Virtual99", "virtual@99.com")
    # scrape_change_details(driver1, "virtual99", "virtual@99problems.com", "VirtualSpam321")
    # driver1.close()
    # print("Virtual user 1 finished")

    driver2 = webdriver.Chrome(options=options)
    scrape_login(driver2, "virtual2", "Virtual124")
    scrape_career_ahp(driver2)
    driver2.close()
    print("Virtual user 2 finished")

    driver3 = webdriver.Chrome(options=options)
    scrape_login(driver3, "virtual3", "Virtual125")
    scrape_uos(driver3)
    driver3.close()
    print("Virtual user 3 finished")

    driver4 = webdriver.Chrome(options=options)
    scrape_login(driver4, "virtual4", "Virtual126")
    scrape_computing_help(driver4)
    driver4.close()
    print("Virtual user 4 finished")

    driver5 = webdriver.Chrome(options=options)
    scrape_login(driver5, "virtual5", "Virtual127")
    scrape_upload(driver5)
    driver5.close()
    print("Virtual user 5 finished")

    driver6 = webdriver.Chrome(options=options)
    scrape_login(driver6, "virtual6", "Virtual128")
    scrape_discussion(driver6)
    driver6.close()
    print("Virtual user 6 finished")

    driver7 = webdriver.Chrome(options=options)
    scrape_login(driver7, "newShawn", "Shawn123")
    scrape_admin_manage(driver7)
    driver7.close()
    print("Virtual user 7 (admin) finished")

    driver8 = webdriver.Chrome(options=options)
    scrape_login(driver8, "virtual8", "Virtual120")
    scrape_messaging(driver8)
    print("Virtual user 8 finished")
    driver8.close()
    #subprocess.run(["killall", "chromedriver"])

    print("All tasks finished!")
