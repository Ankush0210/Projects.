class Student:
	def __init__(self, entryNo, courses):
		self.entryNo = entryNo
		self.courses = courses

	def attempt(self, c_code, quiz, attempts):
		for i in self.__courses:
			if i.coursesCode == c_code:
				for j in i.getObject():
					if j.title == quiz:
						return j.att(self.entryNo, attempts)

	def getUnattemptedQuiz(self):
		score = 0
		quizes = 0
		for i in self.__courses:
			for j in i.getObject():
				k = j.getscore(self.entryNo)
				score += k[0]
				quizes += k[1]
		if quizes == 0:
			return 0
		return score / quizes

class Course:
	def __init__(self, coursecode, qobjects):
		self.coursecode=coursecode
		self.__qobjects=qobjects

	def getobjects(self):
		return self.__qobjects

class Quiz:
	def __init__(self, title, correctoption):
		self.title=title
		self.__correctoption=correctoption
		self.__stuAttempt=[]

	def att(self , entry_no, attempts):
		if len(self.__stuAttempt)==0:
			self.__stuAttempt.append([entry_no, attempts])
			return "Attempted Successfully"
		else:
			for k in range(len(self.__stuAttempt)):
				if entry_no==self.__stuAttempt[k][0]:
					return "you can attempt a quiz only once!"
				elif k==len(self.__stuAttempt)-1:
					j.__stuAttempt.append([entry_no, attempts])
					return "Successfully Attempted"


	def count(self, entry_no):
		for i in self.__stuAttempt:
			if i[0]==entry_no:
				return 1
			break
		return 0

	def getScoore(self, entry_no):
		sc=0
		q=0
		for i in self.__stuAttempt:
			if i[0]==entry_no:
				q+=1
				for j in range(len(i[1])):
					if i[1][j]==self.__correctoption[j]:
						sc+=1
		return sc,q



