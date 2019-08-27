class Section:
    def __init__(self, section_name, section_desc,q_question):
        self.section_name = section_name
        self.section_desc = section_desc
        self.q_question = q_question
        print('**************************'+self.section_name+'*************************\n')
        print('This section is about'+self.section_desc)