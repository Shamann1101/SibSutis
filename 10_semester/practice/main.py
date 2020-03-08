from gymnasium import Gymnasium
from institution import EducationInstitution
from lyceum import Lyceum
from school import School


def main():
    school_1 = School(146)
    school_1.number_of_students = 105
    school_1.set_graduates(2018, 100, 71)
    school_1.set_graduates(2019, 103, 78)
    school_1.print_graduates_percent()

    school_2 = School(144)
    school_2.number_of_students = 91
    school_2.set_graduates(2018, 90, 68)
    school_2.set_graduates(2019, 92, 72)
    school_2.print_graduates_percent()

    school_3 = School(148)
    school_3.number_of_students = 0
    school_3.set_graduates(2018, 101, 34)
    school_3.set_graduates(2019, 120, 42)
    school_3.print_graduates_percent()
    del school_3

    lyceum_1 = Lyceum(128)
    lyceum_1.number_of_students = 81
    lyceum_1.have_hostel = True
    lyceum_1.set_graduates(2018, 80, 73)
    lyceum_1.set_graduates(2018, 81, 70)
    lyceum_1.print_graduates_percent()

    gymnasium_1 = Gymnasium(8)
    gymnasium_1.number_of_students = 55
    gymnasium_1.master_of_sport = 12
    gymnasium_1.set_graduates(2018, 55, 53)
    gymnasium_1.set_graduates(2019, 55, 54)
    gymnasium_1.print_graduates_percent()
    gymnasium_1.print_sport_students()

    print()
    print(f'institution count: {EducationInstitution.institution_count}')
    print(f'have hostel all: {Lyceum.have_hostel_all}')
    print(f'graduates all: {EducationInstitution.graduates_all}')
    print(f'graduates in college all: {EducationInstitution.graduates_in_college_all}')
    print(f'graduates percent all: {EducationInstitution.graduates_percent_all():.2%}')


if __name__ == '__main__':
    main()
