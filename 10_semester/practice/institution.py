from enum import Enum, auto


class InstitutionType(Enum):
    SCHOOL = auto()
    LYCEUM = auto()
    GYMNASIUM = auto()
    SPORT = auto()
    OLYMPIC = auto()

    def __str__(self):
        return self.name


class Institution:
    institution_count = 0

    def __init__(self, number: int = None, institution_type: 'InstitutionType' = None):
        self.number_of_students = 0
        Institution.institution_count += 1
        self.number = number
        if institution_type is not None and not isinstance(institution_type, InstitutionType):
            raise ValueError(institution_type)
        self._institution_type = institution_type

    def __del__(self):
        Institution.institution_count -= 1

    @property
    def institution_type(self) -> 'InstitutionType':
        return self._institution_type

    @institution_type.setter
    def institution_type(self, value: 'InstitutionType'):
        if not isinstance(value, InstitutionType):
            raise ValueError(value)
        self._institution_type = value


class EducationInstitution(Institution):
    allowed_types = [InstitutionType.SCHOOL, InstitutionType.LYCEUM, InstitutionType.GYMNASIUM]
    graduates_all = 0
    graduates_in_college_all = 0

    def __init__(self, number: int = None, institution_type: 'InstitutionType' = None):
        self._check_allowed_type(institution_type)
        super().__init__(number=number, institution_type=institution_type)
        self._graduates = dict()

    def __del__(self):
        graduates = sum([self.graduates[year]['graduates'] for year in self.graduates])
        EducationInstitution.graduates_all -= graduates
        graduates_college = sum([self.graduates[year]['graduates_college'] for year in self.graduates])
        EducationInstitution.graduates_in_college_all -= graduates_college
        super().__del__()

    @classmethod
    def _check_allowed_type(cls, value: 'InstitutionType'):
        if value is not None and value not in cls.allowed_types:
            raise ValueError(value)

    @property
    def institution_type(self) -> 'InstitutionType':
        return super().institution_type

    @institution_type.setter
    def institution_type(self, value: 'InstitutionType'):
        self._check_allowed_type(value)
        super().institution_type = value

    def set_graduates(self, year: int, graduates: int, graduates_college: int):
        graduates_dict = self._graduates.get(year, {'graduates': 0, 'graduates_college': 0})
        self._graduates[year] = {'graduates': graduates, 'graduates_college': graduates_college}
        EducationInstitution.graduates_all += -graduates_dict['graduates'] + graduates
        EducationInstitution.graduates_in_college_all += -graduates_dict['graduates_college'] + graduates_college

    @property
    def graduates(self) -> dict:
        return self._graduates

    def get_graduates_by_year(self, year: int) -> dict:
        return self._graduates.get(year, {'graduates': 0, 'graduates_college': 0})

    @property
    def graduates_percent(self) -> float:
        graduates = sum([self.graduates[year]['graduates'] for year in self.graduates])
        graduates_college = sum([self.graduates[year]['graduates_college'] for year in self.graduates])
        return graduates_college / graduates

    @classmethod
    def graduates_percent_all(cls) -> float:
        return cls.graduates_in_college_all / cls.graduates_all

    def print_graduates_percent(self):
        print('graduates percent of {} {}: {:.2%}'.format(self.institution_type, self.number, self.graduates_percent))


class SportInstitution(Institution):
    allowed_types = [InstitutionType.SPORT, InstitutionType.OLYMPIC]
    master_of_sport_all = 0

    def __init__(self, number=None, institution_type=None):
        self._check_allowed_type(institution_type)
        super().__init__(number=number, institution_type=institution_type)
        self._master_of_sport = 0

    def __del__(self):
        SportInstitution.master_of_sport_all -= self._master_of_sport
        super().__del__()

    @classmethod
    def _check_allowed_type(cls, value: 'InstitutionType'):
        if value is not None and value not in cls.allowed_types:
            raise ValueError(value)

    @property
    def institution_type(self) -> 'InstitutionType':
        return super().institution_type

    @institution_type.setter
    def institution_type(self, value: 'InstitutionType'):
        self._check_allowed_type(value)
        super().institution_type = value

    @property
    def master_of_sport(self) -> int:
        return self._master_of_sport

    @master_of_sport.setter
    def master_of_sport(self, value: int):
        if value > self.number_of_students:
            raise ValueError(value)
        SportInstitution.master_of_sport_all += self._master_of_sport + value
        self._master_of_sport = value
