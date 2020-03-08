import institution as ei


class Lyceum(ei.EducationInstitution):
    have_hostel_all = 0

    def __init__(self, number: int = None):
        super().__init__(number=number, institution_type=ei.InstitutionType.LYCEUM)
        self.optional_courses = list()
        self._have_hostel = False

    def __del__(self):
        Lyceum.have_hostel_all -= int(self._have_hostel)
        super().__del__()

    @property
    def have_hostel(self) -> bool:
        return self._have_hostel

    @have_hostel.setter
    def have_hostel(self, value: bool):
        Lyceum.have_hostel_all += -int(self._have_hostel) + int(value)
        self._have_hostel = value
