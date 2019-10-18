## Email management

* To get a local SMTP debugging server --> any emails sent through this server will be discarded and shown in the terminal window:

> python -m smtpd -c DebuggingServer -n localhost:1025

* Should make sure that your SMTP connection is encrypted --> SSL (Secure Sockets Layer) and TLS (Transport Layer Security) are two protocols that can be used to encrypt an SMTP connection.

### Useful links
* To understand debug mode: https://realpython.com/python-send-email/
* To configure (i.e. get credentials.json file) and understand production mode: https://developers.google.com/gmail/api/quickstart/python


## Scraping management
* Useful book: Python Web Scraping, Second Edition from Katharine Jarmul, Richard Lawson


## Scheduler managament
* Useful link: https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279