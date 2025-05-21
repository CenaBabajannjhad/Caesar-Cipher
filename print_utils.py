class Show_output :

    def show_result(self , text , type):
        '''this method give text and type and show it with two line in above and below'''
        self.line_printer()
        print(f"The {type} text is : {text}")
        self.line_printer()

    def line_printer(self):
        '''print line , ===='''
        print("=============================")
