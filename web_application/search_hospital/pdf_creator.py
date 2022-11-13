from fpdf import FPDF


class PDF_Creator:
    
    def generate_pdf(self, name, number, email1, reservation, date_time, address, message):
        print(name, address, message)
        pdf = FPDF('p', 'mm', 'A4')
        pdf.add_page()

        pdf.set_font('times', 'BIU', 24)
        pdf.set_text_color(0, 0, 0)
        pdf.set_x(70)

        pdf.cell(60, 50, 'Patient Report', ln=True)

        pdf.set_font('courier', '', 16)
        pdf.cell(40, 10, 'Patient Name:         ' + name, ln=True)

        pdf.cell(40, 10, 'Patient Number:       ' + number, ln=True)
        pdf.cell(40, 10, 'Patient Email:        ' + email1, ln=True)
        pdf.cell(40, 10, 'Date and Time:        ' + date_time, ln=True)

        pdf.cell(40, 20, 'Address:          ', ln=True)
        pdf.cell(180, 20, address, ln=True, border=True)

        pdf.cell(40, 20, 'Reservation:          ', ln=True)
        pdf.cell(180, 20, reservation, ln=True, border=True)

        pdf.cell(40, 20, 'Details About Patient:          ', ln=True)
        pdf.cell(180, 20, message, ln=True, border=True)

        pdf.set_font('times', 'BI', 16)
        pdf.set_y(260)
        pdf.set_x(150)
        pdf.cell(60, 10, 'Signature', ln=True)

        pdf.output('patient_report.pdf')
        print('Reached')


#creator = PDF_Creator()
#creator.generate_pdf('name', 'number', 'email1', 'reservation', 'data_time', 'address', 'message')