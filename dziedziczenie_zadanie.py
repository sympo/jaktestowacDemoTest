class TeamMember:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} Join the team')

    def go_to_kitchen(self):
        print(f'{self.name} Go to kitchen, need coffee!')

    def complain(self):
        print(f'{self.name}This app looks not nice')


class Tester(TeamMember):
    def __init__(self, name, break_impact):
        TeamMember.__init__(self, name)
        self.break_impact = break_impact
        print(f'We got new Tester')

    def hi_complain(self):
        super().complain()
        print(f'{self.name} Hello my friend')

    def test(self):
        print(f'{self.name}Test test test')


class Developer(TeamMember):
    def __init__(self, name, prog_language):
        TeamMember.__init__(self, name)
        self.prog_language = prog_language
        print(f'We got new Develeoper')

    def write_code(self):
        print(f'I am writing a code')

    def make_bug(self):
        print(f'I am making a lot of bugs')


class Leader(TeamMember):
    def __init__(self, name, daily_meetings):
        TeamMember.__init__(self, name)
        self.daily_meetings = daily_meetings
        print(f'We got ner Team Leader')

    def make_meeting(self):
        print(f'We are makings meetings now')

    def prise(self):
        print('Prise')


class Automation(Tester):
    def __init__(self, name, break_impact, will_automate_all):
        Tester.__init__(self, name, break_impact)
        self.will_automate_all = will_automate_all
        print(f'Automation')

    def auto_click(self):
        print("I use selenium madafaka")

    def fix_own_code(self):
        print("EZY")


class Performance(Tester):
    def __init__(self, name, break_impact, voodoo_skill_level):
        Tester.__init__(self, name, break_impact)
        self.voodoo_skill_level = voodoo_skill_level
        print(f"Performance")

    def very_hi_complain(self):
        super().hi_complain()
        print("idk what to say")

    def one_test_break_all(self):
        print(f'shit happens')


print('\nTeam forming')
senior_bart = Developer('Bartosz', 'Java')
junior_remi = Tester('Remigiusz', 3)
medium_kacha = Automation('Katarzyna', 6, True)
senior_gocha = Performance('Małgorzata', 9, 100)
cheef_mark = Leader('Marek', 3)

print('\nStart project')
cheef_mark.make_meeting()
senior_bart.write_code()
junior_remi.test()

print('\nDevelopment')
senior_bart.write_code()
senior_bart.make_bug()
medium_kacha.auto_click()
medium_kacha.hi_complain()
print('\nProduction testing')

senior_gocha.test()
senior_gocha.hi_complain()
senior_gocha.one_test_break_all()
senior_gocha.very_hi_complain()
junior_remi.hi_complain()
senior_bart.complain()

print('\nLeader reaction')
cheef_mark.make_meeting()
cheef_mark.complain()
senior_bart.write_code()
junior_remi.test()
cheef_mark.prise()

print('\nTeam leaves work')
senior_bart.go_to_kitchen()
junior_remi.go_to_kitchen()
medium_kacha.go_to_kitchen()
senior_gocha.go_to_kitchen()