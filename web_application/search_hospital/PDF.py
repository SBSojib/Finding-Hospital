from .pdf_creator import PDF_Creator


class PDF:
    def create(self):
        creator = PDF_Creator()
        creator.generate_pdf('nam', 'number', 'email1', 'reservation', 'data_time', 'address', 'message')
