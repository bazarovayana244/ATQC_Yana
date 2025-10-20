login_field = "input[name='login']"
password_field = "input[name='password']"
submit_button = "button[type='submit']"

email_items_css = "[data-msglist-main-link]"
email_items_xpath = "//*[@data-msglist-main-link]"
from_email_xpath = '(//span[@aria-label="Відправник"])[1]'
to_email_xpath = '(//span[@aria-label="Відправник"])[2]'
subject_xpath = '//button[@aria-label="Відмітити непрочитаним"]/../h1'

compose_button = "button:has-text('Написати листа')"
to_field = "#compose-to"
subject_field = "#compose-subject"
iframe_locator = "iframe[id^='mce_']"
body_field = "body#tinymce"
send_button = "button:has-text('Надіслати')"
sent_folder = "span:has-text('Надіслані')"