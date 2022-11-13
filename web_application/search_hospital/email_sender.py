import smtplib
from email.message import EmailMessage


class Email_Sender:
    def send_mail(self, email_to):
        msg = EmailMessage()
        msg['Subject'] = 'Patient Reservation'
        msg['From'] = 'Finding Hospital'
        msg['To'] = email_to
        #msg['To'] = 'mdhasibul-2017415000@cs.du.ac.bd'

        myfile = open('/home/sojib/PycharmProjects/Finding_Hospital/web_application/search_hospital/email_template.txt')
        data = myfile.read()
        msg.set_content(data)
        myfile.close()

        my_attachment = open('/home/sojib/PycharmProjects/Finding_Hospital/web_application/patient_report.pdf', 'rb')
        attachment_data = my_attachment.read()
        attachment_name = my_attachment.name
        msg.add_attachment(attachment_data, maintype='application', subtype='pdf', filename=attachment_name)
        #gaegalxtbeswatdq
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('sjoijniib@gmail.com', 'gaegalxtbeswatdq')
        server.send_message(msg)
        server.quit()


#emailer = Email_Sender()
#emailer.send_mail('mdhasibul-2017415000@cs.du.ac.bd')
