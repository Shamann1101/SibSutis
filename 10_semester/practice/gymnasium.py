import institution as ei


class Gymnasium(ei.EducationInstitution, ei.SportInstitution):
    def __init__(self, number: int = None):
        super().__init__(number=number, institution_type=ei.InstitutionType.GYMNASIUM)
        self.optional_courses = list()

    @property
    def sport_students(self):
        return self.master_of_sport / (self.number_of_students or 1)

    def print_sport_students(self):
        print('sport students of {} {}: {:.2%}'.format(self.institution_type, self.number, self.sport_students))
