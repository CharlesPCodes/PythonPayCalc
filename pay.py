from appJar import gui

#Window
app = gui("Pay Calc", "800x400")
app.setExpand("both")
app.setPadding([20,20])

#Create Entries
app.addLabelEntry("Hours worked: ", 0,0)
app.addLabelEntry("Hourly wage: ", 1,0)

#Button Function
def press(button):
	if button == "Clear":
		app.clearEntry("Hours worked: ")
		app.clearEntry("Hourly wage: ")
	else:
		hoursWorked = app.getEntry("Hours worked: ")
		hourlyWage = app.getEntry("Hourly wage: ")
		# beforeTax = hoursWorked * hourlyWage


# print(beforeTax)
# app.infoBox("Pay Calc", beforeTax, parent=None)

#Add Buttons
app.addButtons(["Submit", "Clear"], press)

app.setFont(16)
app.setFocus("Hours worked: ")
app.go()
