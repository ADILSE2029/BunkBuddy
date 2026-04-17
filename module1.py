import os

class Bunkbuddy:

    def __init__(self):
        self.filename = "bunkbuddy"
        
        ## to add subjects
    def add_subject(self):
        self.decorator()

        if not os.path.exists(self.filename):
            print("Storage file not found, use reset option at main menu")
            return

        user_given_subject_name=input("Add Subject: ").upper()

        with open(self.filename,"r") as f:
            fetched_data=f.readlines()
        
        for each_subject in fetched_data:
            broked_data=each_subject.strip().split("|")
            subject_name=broked_data[0]
            if user_given_subject_name == subject_name:
                print("Subject already exist")
                return
        

        with open(self.filename,"a") as f:
            f.write(user_given_subject_name+"|0|0|0|0|0\n")
        print("Added")
        
        ## selection of subjects 
    def subject_selection(self):
        self.decorator()
        subject_list=[]

        try:
            with open(self.filename,"r") as f:
                fetched_data=f.readlines()
    
                for each_subject in fetched_data:
                    broked_data=each_subject.strip().split("|")
                    subject_name=broked_data[0]
                    subject_list.append(subject_name)
                    print(subject_name)
                
                user_selected_subject=input("Select: ").upper()
                if user_selected_subject in subject_list:
                    self.attendence_marker(user_selected_subject)
                else:
                    print("invalid subject name, try again")
                    return


        except ValueError:
            print("Invalid Input,input must be a number")

        ### attendence marking  - connected to subject selection function 
    def attendence_marker(self, which_subject_to_mark):
        self.decorator()

        if not os.path.exists(self.filename):
            print("Storage File Does not Exist,Use Reset Function at main menu")
            return
        
        with open(self.filename, "r") as f:
            fetched_data = f.readlines()
            for index_value,each_subject in enumerate(fetched_data):
                if each_subject.startswith(which_subject_to_mark):
                    selected_subj_data=each_subject.strip().split("|")
                    subject_name=selected_subj_data[0]
                    subject_total_attend = int(selected_subj_data[1])
                    subject_my_attend = int(selected_subj_data[2])
                    subject_my_absents = int(selected_subj_data[3])
                    subject_canceled = int(selected_subj_data[4])
                        

                    given_attendence = input(
                        "[P]resent or [A]bsent or [C]anceled?\nMark:").lower()
                    if given_attendence == "p":
                        subject_total_attend += 1
                        subject_my_attend += 1

                    elif given_attendence == "a":
                        subject_total_attend += 1
                        subject_my_absents += 1

                    elif given_attendence == "c":
                        subject_canceled += 1
                    else:
                        print("Invalid Input")
                        return
                    
                    ### percentage calculations
                    if subject_total_attend > 0:
                        percentage = subject_my_attend/subject_total_attend*100
                    else:
                        percentage = 0

                    ##new line creation
                    new_line = f"{subject_name}|{subject_total_attend}|{subject_my_attend}|{subject_my_absents}|{subject_canceled}|{percentage}\n"
                    fetched_data[index_value] = new_line


                    with open(self.filename, "w") as f:
                        for each_subject in fetched_data:
                            f.write(each_subject)
                    print("\t--Attendence Marked--")

        ### view section
    def view_details(self):
        self.decorator()

        if not os.path.exists(self.filename):
            print("Storage File does not exist,use reset option at main menu")
            return
        
        subject_name = "Subject-Name"
        subject_presents = "Presents"
        subject_percentage = "Percentage"
        total_classs = "Total Classes"
        subject_absent = "Absent"
        subject_canceled = "Canceled"
        
        
        with open(self.filename, "r") as f:
            subject_list = f.readlines()
            print(
                f"{subject_name:<40}{total_classs:<15}{subject_presents:<15}{subject_absent:<15}{subject_canceled:<15}{subject_percentage}")
            

            for i in subject_list:
                subject_data = i.strip().split(
                    '|')
                subject_name = subject_data[0]
                subject_total_attend = int(subject_data[1])
                subject_my_attend = int(subject_data[2])
                subject_my_absents = int(subject_data[3])
                subject_canceled = int(subject_data[4])


                if subject_my_attend > 0:
                    calculated_percentage = int(
                        subject_my_attend)/int(subject_total_attend)*100
                    percentage = str(calculated_percentage)+"%"
                    print(
                        f"{subject_name:<40}{subject_total_attend:<15}{subject_my_attend:<15}{subject_my_absents:<15}{subject_canceled:<15}{percentage}")
                
                else:
                    No_data = "No Data"
                    print(
                        f"{subject_name:<40}{No_data:<15}{No_data:<15}{No_data:<15}{subject_canceled:<15}{No_data}")

        ## warning for low attendence
    def warnings(self):
        self.decorator()

        if not os.path.exists(self.filename):
            print("Storage File does not exist,use reset option at main menu")
            return
        

        with open(self.filename, "r") as f:
            for subject_data in f:
                subject_select = subject_data.strip().split('|')
                subject_name = subject_select[0]
                subject_percentage = float(subject_select[5])
                if subject_percentage < 75:
                    print(
                        f"Attendence Low for Subject :{subject_name}\nAttendence:{subject_percentage}%")
        ## reset info
    def reset_data(self):
        self.decorator()
        stored_subjects_list=[]

        if not os.path.exists(self.filename):
            with open(self.filename,"w") as f:
                f.write("")
                print("File Created")
        else:
            pass
        
        with open(self.filename ,"r") as f:
            fecthed_data=f.readlines()
            for each_subject_name in fecthed_data:
                broked_data=each_subject_name.strip().split("|")
                subject_name=broked_data[0]
                stored_subjects_list.append(subject_name)
        
        with open(self.filename,"w") as f:
            for each_name in stored_subjects_list:
                f.write(each_name+"|0|0|0|0|0\n")
            print("Reset Successfull")
            print("note: if there is no subject to reset , just use add subject at main menu")
        
        
        
        ## this is peak hehe
    def bunkmeter(self):
        self.decorator()

        if not os.path.exists(self.filename):
            print("Storage File does not exist,use reset option at main menu")
            return
        
        with open(self.filename, "r") as f:
            for subject_data in f:
                subject_select = subject_data.strip().split('|')
                subject_name = subject_select[0]
                subject_total_attend = int(subject_select[1])
                subject_my_attend = int(subject_select[2])


                try:
                    counter = 0
                    while (subject_my_attend/(subject_total_attend+counter+1))*100 >= 75:
                        counter += 1
                    print(
                        f"Skipable classes for subject {subject_name:<55}: {counter} ")
                except ZeroDivisionError:
                    print("No Class Data Available")

        ##decoration purposes
    def decorator(self):
        print("="*40)


