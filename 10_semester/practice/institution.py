from enum import Enum


class InstitutionType(Enum):
    SCHOOL = 1
    LYCEUM = 2
    GYMNASIUM = 3
    SPORT = 4
    OLYMPIC = 5


class Institution:
    institution_count = 0

    def __init__(self, number=None, institution_type=None):
        self.number_of_students = 0
        Institution.institution_count += 1
        self.number = number
        if institution_type is not None and not isinstance(institution_type, InstitutionType):
            raise ValueError(institution_type)
        self._institution_type = institution_type

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

    def __init__(self, number=None, institution_type=None):
        self._check_allowed_type(institution_type)
        super().__init__(number=number, institution_type=institution_type)
        self._graduates = dict()

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
        return self.graduates_in_college_all / self.graduates_all


class SportInstitution(Institution):
    allowed_types = [InstitutionType.SPORT, InstitutionType.OLYMPIC]
    master_of_sport_all = 0

    def __init__(self, number=None, institution_type=None):
        self._check_allowed_type(institution_type)
        super().__init__(number=number, institution_type=institution_type)
        self._master_of_sport = 0

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
        SportInstitution.master_of_sport_all += self._master_of_sport + value
        self._master_of_sport = value
