import copy
class School():
    def __init__(self,name=None):
        self.name=name
        self._roster={}
    def roster(self):
        return self._roster
    def add_student(self, name, grade):
        if grade in self._roster:
            self._roster[grade].append(name)
        else:
            self._roster[grade]=[]
            self._roster[grade].append(name)
        return self._roster
    def sort_roster(self):
        min_grade=min(self.roster().keys())
        max_grade=max(self.roster().keys())
        all_grades=list(range(min_grade,max_grade+1))
        for grade in all_grades:
            print('Grade ', grade,":", self._roster[grade])
        return all_grades