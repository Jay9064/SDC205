# Student: Jasgut7158
# This program totals five numbers, adds five income records to a CSV,
# creates an Excel pie chart, and displays a Matplotlib bar graph.

import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference


# Use the folder containing this Python file for the CSV and Excel files.
folderPath = os.path.dirname(os.path.abspath(__file__))
os.chdir(folderPath)

# Set the name of the CSV file used to store income records.
csvFileName = "final.csv"

# Create the sample starting CSV only if the course-provided file is absent.
if not os.path.exists(csvFileName):
    with open(csvFileName, "w", newline="", encoding="utf-8") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(["Randy", 40000])
        csvWriter.writerow(["Lisa", 115000])
        csvWriter.writerow(["William", 120000])
        csvWriter.writerow(["Carrie", 150000])


# Ask the user for five numbers, add them, and display the total.
def askUser():
    total = 0

    # This loop gets five numbers and adds each one to the running total.
    for numberCount in range(5):
        number = float(input("Please enter a number: "))
        total += number

    print(f"The sum for the 5 numbers entered is: {total:g}")


# Ask for five names and incomes, then append each record to the CSV.
def askIncome():
    # This loop gathers five people’s names and incomes and saves each record.
    for personCount in range(5):
        name = input("Please enter a name: ")
        income = int(input("Please enter their income: "))

        with open(csvFileName, "a", newline="", encoding="utf-8") as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow([name, income])


# Read the CSV, place its data in Excel, and create an embedded pie chart.
def excelPie():
    nameList = []
    incomeList = []

    with open(csvFileName, "r", newline="", encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile)

        for row in csvReader:
            if len(row) >= 2:
                nameList.append(row[0])
                incomeList.append(int(row[1]))

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Income Data"

    for personIndex in range(len(nameList)):
        worksheet.cell(row=personIndex + 1, column=1, value=nameList[personIndex])
        worksheet.cell(row=personIndex + 1, column=2, value=incomeList[personIndex])

    # Create the Excel pie chart object.
    pieChart = PieChart()
    # Set the chart title to the student ID and today's date.
    dateText = datetime.now().strftime("%B %d, %Y").replace(" 0", " ")
    pieChart.title = f"Jasgut7158 {dateText}"
    # Select the income values that will determine the pie-slice sizes.
    incomeData = Reference(
        worksheet, min_col=2, min_row=1, max_row=len(nameList)
    )
    # Select the names that will label the pie slices.
    nameLabels = Reference(
        worksheet, min_col=1, min_row=1, max_row=len(nameList)
    )
    # Add the income values to the pie chart.
    pieChart.add_data(incomeData)
    # Add the names as labels for the pie slices.
    pieChart.set_categories(nameLabels)
    # Set the chart dimensions.
    pieChart.height = 12
    pieChart.width = 16
    # Place the chart beside the data in the worksheet.
    worksheet.add_chart(pieChart, "D2")
    # Save the data and embedded pie chart in the required Excel file.
    workbook.save("final.xlsx")

    print("Created final.xlsx with the income data and pie chart.")


# Read the same CSV data and display it as a vertical Matplotlib bar graph.
def verticalBar():
    nameList = []
    incomeList = []

    with open(csvFileName, "r", newline="", encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile)

        for row in csvReader:
            if len(row) >= 2:
                nameList.append(row[0])
                incomeList.append(int(row[1]))

    dateText = datetime.now().strftime("%B %d, %Y").replace(" 0", " ")
    plt.bar(nameList, incomeList, color="green", label="Income")
    plt.title(f"Jasgut7158 {dateText}")
    plt.xlabel("Name")
    plt.ylabel("Income")
    plt.legend()
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()


# Run the number-totaling task.
askUser()

# Collect and append five income records.
askIncome()

# Create the Excel file and its pie chart.
excelPie()

# Display the vertical bar graph.
verticalBar()