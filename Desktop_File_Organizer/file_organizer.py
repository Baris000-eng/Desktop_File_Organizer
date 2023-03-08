import os
import shutil
from pathlib import Path

java_file_number = 0
python_file_number = 0
cpp_file_number = 0
swift_file_number = 0
zip_file_number = 0
jar_file_number = 0
sql_file_number = 0

excel_file_number = 0
access_file_number = 0
xml_file_number = 0
bin_file_number = 0
pdf_file_number = 0
txt_file_number = 0
c_file_number = 0
csv_file_number = 0
tar_file_number = 0
word_file_number = 0

# Set the path to the Desktop directory
desktop_path = Path.home() / "Desktop"

# Set the path to the directory where you want to move the Java files
java_path = os.path.join(desktop_path, "Java Files")

# Set the path to the directory where you want to move the C++ files
cpp_path = os.path.join(desktop_path, "C++ Files")

# Set the path to the directory where you want to move the Python files
python_path = os.path.join(desktop_path, "Python Files")

# Set the path to the directory where you want to move the Text files
text_path = os.path.join(desktop_path, "Text Files")

# Set the path to the directory where you want to move the Pdf files
pdf_path = os.path.join(desktop_path, "Pdf Files")

# Set the path to the directory where you want to move the Word files
word_path = os.path.join(desktop_path, "Word Files")

# Set the path to the directory where you want to move the Excel files
excel_path = os.path.join(desktop_path, "Excel Files")

# Set the path to the directory where you want to move the Tar files
tar_path = os.path.join(desktop_path, "Tar Files")

zip_path = os.path.join(desktop_path, "Zip Files")

swift_path = os.path.join(desktop_path, "Swift Files")

xml_path = os.path.join(desktop_path, "Xml Files")

access_db_path = os.path.join(desktop_path, "Access Database Files")

c_path = os.path.join(desktop_path, "C Files")

csv_path = os.path.join(desktop_path, "Csv Files")

bin_path = os.path.join(desktop_path, "Bin Files")

sql_path = os.path.join(desktop_path, "SQL Files")

jar_path = os.path.join(desktop_path, "Jar Files")

# Check if desktop contains java, cpp, python or text files and move them to the respective directories
for file in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file)
    if os.path.isfile(file_path) and file in os.listdir(desktop_path):
        if file.endswith(".java"):
            # Create the directory for Java files if it does not exist
            if not os.path.exists(java_path):
                os.mkdir(java_path)
            # Move the Java file to the Java directory
            shutil.move(file_path, java_path)
            java_file_number += 1
        elif file.endswith(".cpp"):
            # Create the directory for C++ files if it does not exist
            if not os.path.exists(cpp_path):
                os.mkdir(cpp_path)
            # Move the C++ file to the C++ directory
            shutil.move(file_path, cpp_path)
            cpp_file_number += 1
        elif file.endswith(".py"):
            # Create the directory for Python files if it does not exist
            if not os.path.exists(python_path):
                os.mkdir(python_path)
            # Move the Python file to the Python directory
            shutil.move(file_path, python_path)
            python_file_number += 1
        elif file.endswith(".txt"):
            # Create the directory for Text files if it does not exist
            if not os.path.exists(text_path):
                os.mkdir(text_path)
            # Move the Text file to the Text directory
            shutil.move(file_path, text_path)
            txt_file_number += 1
        elif file.endswith(".pdf"):
            if not os.path.exists(pdf_path):
                os.mkdir(pdf_path)
            # Move the Python file to the Python directory
            shutil.move(file_path, pdf_path)
            pdf_file_number += 1
        elif file.endswith(".xlsx") or file.endswith(".xls"):
            if not os.path.exists(excel_path):
                os.mkdir(excel_path)
            shutil.move(file_path, excel_path)
            excel_file_number += 1
        elif file.endswith(".accdb"):
            if not os.path.exists(access_db_path):
                os.mkdir(access_db_path)
            shutil.move(file_path, access_db_path)
            access_file_number += 1
        elif file.endswith(".zip"):
            if not os.path.exists(zip_path):
                os.mkdir(zip_path)
            shutil.move(file_path, zip_path)
            zip_file_number += 1
        elif file.endswith(".bin"):
            if not os.path.exists(bin_path):
                os.mkdir(bin_path)
            shutil.move(file_path, bin_path)
            bin_file_number += 1
        elif file.endswith(".swift"):
            if not os.path.exists(swift_path):
                os.mkdir(swift_path)
            shutil.move(file_path, swift_path)
            swift_file_number += 1
        elif file.endswith(".csv"):
            if not os.path.exists(csv_path):
                os.mkdir(csv_path)
            shutil.move(file_path, csv_path)
            csv_file_number += 1
        elif file.endswith(".tar") or file.endswith(".gz"):
            if not os.path.exists(tar_path):
                os.mkdir(tar_path)
            shutil.move(file_path, tar_path)
            tar_file_number += 1
        elif file.endswith(".c"):
            if not os.path.exists(c_path):
                os.mkdir(c_path)
            shutil.move(file_path, c_path)
            c_file_number += 1
        elif file.endswith(".docx") or file.endswith(".doc"):
            if not os.path.exists(word_path):
                os.mkdir(word_path)
            shutil.move(file_path, word_path)
            word_file_number += 1
        elif file.endswith(".sql"):
            if not os.path.exists(sql_path):
                os.mkdir(sql_path)
            shutil.move(file_path, sql_path)
            sql_file_number += 1

        elif file.endswith(".jar"):
            if not os.path.exists(jar_path):
                os.mkdir(jar_path)
            shutil.move(file_path, jar_path)
            jar_file_number += 1


print("The numbers of different file types in the desktop of this user: ")
print("This user has:")
print(str(java_file_number) + " java files in his/her desktop")
print(str(python_file_number) + " python files in his/her desktop")
print(str(cpp_file_number) + " cpp files in his/her desktop")
print(str(pdf_file_number) + " pdf files in his/her desktop")
print(str(excel_file_number) + " excel files in his/her desktop")
print(str(txt_file_number) + " txt files in his/her desktop")
print(str(access_file_number) + " access database files in his/her desktop")
print(str(zip_file_number) + " zip files in his/her desktop")
print(str(bin_file_number) + " bin files in his/her desktop")
print(str(swift_file_number) + " swift files in his/her desktop")
print(str(csv_file_number) + " csv files in his/her desktop")
print(str(tar_file_number) + " tar files in his/her desktop")
print(str(c_file_number) + " c files in his/her desktop")
print(str(word_file_number) + " word files in his/her desktop")
print(str(sql_file_number) + " sql files in his/her desktop")
print(str(jar_file_number) + " jar files in his/her desktop")
