import time
import tkinter as tk

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

root = tk.Tk()

# Center the window to the screen
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))


def log_in(email, password):
    email = email.get()
    password = password.get()

    root.destroy()

    # IMPORTANT !
    # Get the url of the discussion from the mobile version of facebook
    url = "https://m.facebook.com/messages/read/?tid=cid.c.100010674137983%3A100023722361169"

    # Add the browser driver like chrome or firefox
    driver = webdriver.Chrome("D:\\Programming Files\\Python\\chromedriver.exe")

    driver.get(url)

    driver.find_element_by_id('m_login_email').send_keys(email)
    driver.find_element_by_id('m_login_password').send_keys(password)
    driver.find_element_by_id('u_0_5').click()

    time.sleep(1)

    while True:
        try:
            driver.find_element_by_class_name('primary').click()
        except (NoSuchElementException, StaleElementReferenceException):
            pass


# The main function
def main():
    tk.Label(root, text="Email: ").grid(row=0)
    tk.Label(root, text="Password: ").grid(row=1)

    email = tk.Entry(root)
    email.focus()
    password = tk.Entry(root, show='*')

    email.grid(row=0, column=1)
    password.grid(row=1, column=1)

    root.bind("<Return>", (lambda event: log_in(email, password)))
    tk.Button(root, text='Enter', command=lambda: log_in(email, password)).grid(row=3, column=2, sticky=tk.W, pady=4)

    root.mainloop()


if __name__ == '__main__':
    main()
