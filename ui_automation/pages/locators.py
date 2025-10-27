###login page locators###
login_field = "input[name='login']"
password_field = "input[name='password']"
submit_button = "button[type='submit']"
profile_icon = "div[aria-label='Зображення профілю']"

###inbox page locators###
email_items_css = "[data-msglist-main-link]"
email_items_xpath = "//*[@data-msglist-main-link]"
from_email_xpath = '(//span[@aria-label="Відправник"])[1]'
to_email_xpath = '(//span[@aria-label="Відправник"])[2]'
subject_xpath = '//button[@aria-label="Відмітити непрочитаним"]/../h1'

###compose page locators###
compose_button = "button:has-text('Написати листа')"
to_field = "#compose-to"
subject_field = "#compose-subject"
iframe_locator = "iframe[id^='mce_']"
body_field = "body#tinymce"
send_button = "button:has-text('Надіслати')"
popup_button_inbox = "//button[text()='Дивитися вхідні']"
sent_folder = "a[title='Надіслані']"
