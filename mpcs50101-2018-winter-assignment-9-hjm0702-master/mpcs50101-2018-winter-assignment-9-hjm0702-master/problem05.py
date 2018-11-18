import time
import datetime
import sys
import re
import pickle

class Task:
    '''create, save, and retreive tasks with due date and priority'''

    def __init__(self, name, duedate, priority):
        self.name = name
        self.next = None
        self.duedate = duedate
        self.priority = priority
        self.createddate = datetime.datetime.now()
        self.id = 0
        self.completedate = None
        self.completed = False

    def getdata(self):
        return self.name, self.duedate, self.priority, self.createddate, self.id, self.completedate, self.completed

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext

    def setid(self, idno):
        self.id = idno

    def setcompletedate(self):
        self.completedate = datetime.datetime.now().date()
        self.completed = True

class Tasks:
    """Ordered list of Task objects."""

    def __init__(self):
        self.head = None

    def add_task(self, name, duedate, priority):
        """Create a new task with a given name"""
        temp = Task(name, duedate, priority)

        current = self.head
        previous = None
        stop = False
        count = 1

        while current != None and not stop:
            if current.getdata()[3] > temp.getdata()[3] :
                stop = True
            else:
                previous = current
                current = current.getnext()

        if previous == None:
            temp.setnext(self.head)
            self.head = temp
            temp.setid(count)
        else:
            temp.setnext(current)
            previous.setnext(temp)
            temp.setid(previous.getdata()[4]+1)

    def remove_task(self, idno):
        """Remove a task with a given id"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata()[4] == idno:
                found = True
            else:
                previous = current
                current = current.getnext()
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())


    def list(self):
        '''print items not completed'''
        print '{0:2} {1:3} {2:11}  {3:10} {4:30}'.format("ID", "Age", "Due Date","Prioirity", "Task")
        print '{0:2} {1:3} {2:11}  {3:10} {4:30}'.format("==", "===", "========","=========", "====")
        current = self.head
        while current != None:
            if current.getdata()[6] == False:
                a = datetime.date.today()-current.getdata()[3].date()
                b = str(a.days) + "d"
                print '{0:2d} {1:2}  {2:10} {3:11}  {4:30}'.format(current.getdata()[4], b,
                 current.getdata()[1],current.getdata()[2], current.getdata()[0])
            current = current.getnext()

    def report(self):
        '''print all items not removed'''
        print '{0:2} {1:3} {2:11}  {3:10} {4:15} {5:10} {6:30}'.format("ID", "Age", "Due Date","Prioirity", "Task", "Created", "Completed")
        print '{0:2} {1:3} {2:11}  {3:10} {4:15} {5:10} {6:30}'.format("==", "===", "========","=========", "====", "=======", "=========")
        current = self.head
        while current != None:
            a = datetime.date.today()-current.getdata()[3].date()
            b = str(a.days) + "d"
            print '{0:2d} {1:3} {2:10} {3:11}  {4:15} {5:%m/%d/%Y} {6:}'.format(current.getdata()[4], b,
             current.getdata()[1],current.getdata()[2], current.getdata()[0], current.getdata()[3], current.getdata()[5])
            current = current.getnext()

    def done(self, idno):
        """Change complete data and complete status by idno"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata()[4] == idno:
                found = True
            else:
                previous = current
                current = current.getnext()
        current.setcompletedate()

    def search(self, keyword):
        '''search task by keyword'''
        current = self.head
        stop = False
        while current !=None and not stop:
            if keyword.lower() in current.getdata()[0].lower():
                a = datetime.date.today()-current.getdata()[3].date()
                b = str(a.days) + "d"
                print '{0:2d} {1:2}  {2:10} {3:11}  {4:30}'.format(current.getdata()[4], b,
                 current.getdata()[1],current.getdata()[2], current.getdata()[0])
                current = current.getnext()
            else:
                if current == None:
                    stop = True
                else:
                    current = current.getnext()

    def __str__(self):
        final_list = []
        current = self.head
        count = 0

        while current != None:
            count = count +1
            final_list.append(str(current.getdata( )))
            current = current.getnext()
        return str(final_list)


if __name__ == "__main__":
    tasklist = Tasks()
    with open('.todo.pickle', 'rb') as f: tasklist = pickle.load(f)

    a = sys.argv
    command = ["add", "delete", "list", "report", "done"]
    try :
        if a[1].lower() == command[3]:
            '''report function'''
            print tasklist.report()
        elif a[1].lower() == command[2]:
            '''list fuction'''
            if len(a) > 2:
                print '{0:2} {1:3} {2:11}  {3:10} {4:30}'.format("ID", "Age", "Due Date","Prioirity", "Task")
                print '{0:2} {1:3} {2:11}  {3:10} {4:30}'.format("==", "===", "========","=========", "====")
                for i in range(len(a)-2):
                    if a[-1-i][0] == "+":
                        tasklist.search(a[-1-i][1:])
                    else:
                        print "Please put + before your keyword."
            else:
                print tasklist.list()
        elif a[1].lower() == command[1]:
            '''delete function'''
            try:
                tasklist.remove_task(int(a[2]))
                print "Deleted task", a[2]
            except:
                print "Can't find the task id you want to remove."
        elif a[1].lower() == command[4]:
            '''done function'''
            try:
                tasklist.done(int(a[2]))
                print "Completed task", a[2]
            except:
                print "Can't find the task id you want to complete."
        elif a[1].lower() == command[0]:
            '''add function'''
            try:
                if ":" in a[-2] and ":" in a[-1]:
                    if "due:" in a[-2].lower() and "priority:" in a[-1].lower():
                        if int(a[-1][9:]) < 4 and int(a[-1][9:]) >0:
                            tasklist.add_task(" ".join(a[2:-2]),a[-2][4:], int(a[-1][9:]))
                            print "Created task", int(str(tasklist).split()[-3][:-1])
                        else:
                            print "Prioirty should be 1, 2, or 3"
                    else:
                        print "Please check command lines again."
                elif ":" not in a[-2] and ":" in a[-1]:
                    if "due:" in a[-1].lower() or "priority:" in a[-1].lower():
                        if "due:" in a[-1].lower():
                            tasklist.add_task(" ".join(a[2:-1]),a[-1][4:], 1)
                            print "Created task", int(str(tasklist).split()[-3][:-1])
                        elif "priority:" in a[-1].lower():
                            if int(a[-1][9:]) < 4 and int(a[-1][9:]) >0:
                                tasklist.add_task(" ".join(a[2:-1]), None, int(a[-1][9:]))
                                print "Created task", int(str(tasklist).split()[-3][:-1])
                            else:
                                print "Prioirty should be 1, 2, or 3"
                    else:
                        print "Please check command lines again."
                elif ":" not in a[-2:-1]:
                    tasklist.add_task(" ".join(a[2:]),None, 1)
                    print "Created task", int(str(tasklist).split()[-3][:-1])
            except:
                print "Please check command lines again."
        else:
            print "Please input possible command lines."
    except:
        print "Please input possible command lines."
    with open('.todo.pickle', 'wb') as f: pickle.dump(tasklist, f)
