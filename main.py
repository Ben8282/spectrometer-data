import os
print("hello welcome to the spectrometer sorting thing")
print("plz make sure that the csv file you would like to open to sort is in the same folder")
print("that the code is in")
print("so first input what the name of the csv file you would like to open is")
class data_point:
    def __init__(self, id,assigned_number,wavelength,intensety):
        self.id = id
        self.assigned_number = assigned_number
        self.wavelength = wavelength
        self.intensety = intensety
reset = 1
while reset == 1:
    filename = input()
    if os.path.exists(filename):
        print("file found sorting")
        data_points = []
        next_id = 1
        with open(filename, "r")as rf:
            next(rf)
            for line in rf:
                parts = line.strip().split(",")
                wavelength = parts[0]
                intensety = parts[1]
                wavelength = float(wavelength)
                intensety = float(intensety)
                assigned_number = intensety
                point = data_point(next_id,assigned_number,wavelength,intensety)
                data_points.append(point)
                next_id = next_id + 1
            def get_assigned_number(point):
                return point.assigned_number  
            data_points.sort(key=get_assigned_number, reverse=True)
            print("the sorting is complete")
            print("would you like to save to file")
            print("or to veiw all of them")
            print("or to veiw just the top few you pick")
            print("please input 1 for saving to file")
            print("please input 2 if you would like to veiw all")
            print("and please input 3 if you would like to veiw a certian amount")
            resetb = 1
            while resetb == 1:
                veiwing = input()
                if veiwing == "1":
                    print("so were would you like to save it give the filename and ill save it there")
                    print("or make your own and itll just create it")
                    print("csv recommended as the program with save it assuming csv format")
                    inputfilename = input()
                    with open(inputfilename, "w") as wf:
                        wf.write("wavelength,intensity\n")
                        for point in data_points:
                            wf.write(f"{point.wavelength},{point.intensety}\n")
                    resetb = 0
                elif veiwing == "2":
                    for point in data_points:
                        print("id: ",point.id,"wavelength: ",point.wavelength,"intensity: ",point.intensety)
                    resetb = 0
                elif veiwing == "3":
                    print("so what amount of datapoints would you like to veiw")
                    resetc = 1
                    while resetc == 1:
                        veiwamount = input()
                        try:
                            veiwamount = int(veiwamount)
                            resetc = 0
                        except ValueError:
                            print("that is not valid number")
                            print("try again please enter a valid number")
                            resetc = 1
                    print("top",veiwamount,"DataPoints")
                    for point in data_points[:veiwamount]:
                          print("id: ",point.id,"wavelength: ",point.wavelength,"intensity: ",point.intensety)
                    resetb = 0
                else:
                    print("please input 1 for saving to file")
                    print("please input 2 if you would like to veiw all")
                    print("and please input 3 if you would like to veiw a certian amount")
        reset = 0 
    else:
        print("file not found")
        print("please try again")
        reset = 1 
