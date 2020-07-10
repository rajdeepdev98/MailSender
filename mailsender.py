import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import addressparser as adp
import textparser as txtp

my_address="rajdeep.dev98@gmail.com"
my_password="shonamaamoni"
my_host_address="smtp.gmail.com"
my_port="587"

def main():
    names,emails=adp.get_contacts('contactlist.txt')
    messagetmp=txtp.read_template("message.txt")

    #setting up the SMTP server
    smtp=smtplib.SMTP(host=my_host_address,port=my_port)
    smtp.starttls()
    smtp.login(my_address, my_password)

    #sending the mail to each contact
    for name,email in zip(names,emails):
        msg=MIMEMultipart()

        #adding the actual person name in the message template
        message=messagetmp.substitute(PERSON_NAME=name.title())

        #printing out the message for our visibility
        print(message)


        #setting up address parameters of the message
        msg["From"]=my_address
        msg['To']=email
        msg['Subject']="Learning something new"

        #adding message from the template file
        msg.attach(MIMEText(message,'plain'))

        smtp.send_message(msg)

        del msg
    #terminating the SMTP session and closing the connection

    smtp.quit()

if __name__ == "__main__":
    #calling the main function which encapsulates everything
    main()
    