"""Report view"""


class ReportView:
    
    def prompt_report_choice(self):
        """ Prompt for a report to choice"""
        print("Choose a report : \n"
              "1. All players list report by alphabetical order\n"
              "2. All players list report by ranking\n"
              "3. Tournament players list report by alphabetical order\n"
              "4. Tournament players list report by ranking\n"
              "5. All tournaments list\n"
              "6. All rounds tournament list\n"
              "7. All games tournament list\n"
              "8. Quit\n")
        choice = input('Enter your choice between 1 and 8 : \n')
        return choice


    def print_element_report(self, element_list):
        for element in element_list:
            print(element.name)