import institution as ei


class School(ei.EducationInstitution):
    def __init__(self, number: int = None):
        super().__init__(number=number, institution_type=ei.InstitutionType.SCHOOL)
