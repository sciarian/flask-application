#########################################################################################
#
# This file is used to populte the databse with data.
#
# @Author Anthony Sciarini
# @Version 8/18/2018
# @Source http://www.patricksoftwareblog.com/database-using-postgresql-and-sqlalchemy/
#
#########################################################################################

###############
### Imports ###
###############

from project import db
from project.models import Course

#Create the database
db.create_all()

####################
#Insert course data#
####################

print(type(db))


#2015 - 2016 Academic year


#TODO change '|' -> '&'
#TODO add courses to database little by little and debug when necessary.

#   Fall 2015
s_d = "Aug 31, 2015"
e_d = "Dec 19, 2015"

crs01 = Course(22085,"CHM 115 02","Principlse of Chemistry I", 
              "Allendale",4.000,"U",s_d,e_d, 
              "MW | T", "6:00 pm - 7:15 pm | 11:00 am - 1:50 pm", 
              "Manitou Hall 102 | Manitou Hall of Science 244", "Taylor | Frollo", "F15")

crs02 = Course(21002, "EGR 100 03", "Introduction to Engineering", "Pew", 1.000, "U" , 
              s_d, e_d, "R", "12:00 pm - 12:50 pm",  
              "Kennedy Hall of Engineering 124", "Johnson","F15")

crs03 = Course(22618, "EGR 106 01", "Introduction to Engineering Design", "Pew", 3.000, "U",
              s_d, e_d, "MW", "8:00 am - 9:50 am", 
              "Kennedy Hall of Engineering 244", "Baine", "F15")

crs04 = Course(13026, "MTH 201 02", "Calculus 1", "Allendale", 4.000, "U", s_d,
              e_d, "MWF | T", "2:00 pm - 2:50 pm | 2:50 pm", 
              "Makcinac Hall BLL118 | Mackinac Hall A2151", "Schlicker", "F15")

crs05 = Course(14463, "WRT 150 02", "Strategies in Writing", "Allendale", 4.000, "U",
              s_d, e_d, "R | T", "8:00 am - 9:50 am", 
              "Lake Superior Hall | The Connection 210", "Lotz", "F15")



#   Winter 2016
s_d = "Jan 11, 2016"
e_d = "Apr 30, 2016"

crs06  = Course(20408,"BIO 120 20", "General Biology I", "Allendale", 4.000, "U", 
               s_d, e_d, "MWF", "11:00 am - 11:50 am", 
               "P. Kindschi Hall of Science 1101", "Zeman", "W16")

crs07  = Course(20422, "BIO 120 905", "General Biology I", "Allendale", 0.000, "U",
               s_d, e_d, "M", "2:00 pm - 4:50 pm",
               "P. Kindschi Hall of Science 2276", "Atkins", "W16")

crs08  = Course(31632, "EGR 107 01", "Inroduction to Engineering Design II", "Pew", 
                3.000, "U", s_d, e_d, "MW", "8:00 am- 9:50 am", 
                "Kennedy Hall of Engineering 244", "Brakora", "W16")

crs09  = Course(25285, "MTH 202 07", "Calculus II", "Allendale", 4.000, "U", s_d, 
                e_d, "T | MWF", "12:00 pm - 12:50 pm | 1:00 pm - 1:50 pm", 
               "Mackinac Hall A2165", "Schwass", "W16")

crs10 = Course(22644, "PHI 102 04", "Ethics", "Allendale", 3.000, "U", s_d, 
               e_d, "TR", "2:30 pm - 3:45 pm", "Mackinnac Hall D1221", 
               "Castelo-Lawless", "W16")


#2016 - 2017 Academic year
s_d = "Aug 29, 2016"
e_d = "Dec 17, 2016"

#   Fall   2016
crs11 = Course(17759, "CIS 162 04", "Computer Science I", "Allendale", 4.000, "U", s_d, e_d, 
               "M | MWF", "12:00 pm - 1:50 pm | 11:00 am - 11:50 am", 
               "Henry Hall 115 | Mackinac Hall B1116", "Scripps", "F16")

crs12 = Course(18540, "ERG 220 903", "Engineering Data Measurement and Data Analysis", "Pew", 
               1.000, "U", s_d, e_d, "R", "8:00 am - 10:50 am", 
               "Kennedy Hall of Engineering 322", "Christoper", "F16")

crs13 = Course(11693, "HST 103 08", "Introduction to American Civilization", "Allendale", 
               3.000, "U", s_d, e_d, "MWF", "2:00 pm - 2:50 pm", "Mackinac Hall D1215", 
               "Salas", "F16")

crs14 = Course(21762, "MTH 302 02", "Linear Algebra and Differential Equations", "Pew", 
               4.000, "U", s_d, e_d, "TR", "1:00 pm - 2:50 pm", "Eberhard Center 716", 
               "Drake", "F16")

crs15 = Course(15404, "PED 103 01", "Tae Kwon Do", "Allendale", 1.000, "U", s_d, e_d, 
               "T", "4:00 pm - 5:40", "Recration Center ct 4,5", "Allen", "F16")

crs16 = Course(22824, "STA 220 40", "Statistical Modeling for Engineers", "Allendale",
               2.000, "U", s_d, e_d, "M", "8:00 am - 9:50am", 
               "Henry Hall 114", "Fox", "F16")



#   Winter 2017 
s_d = "Jan 09, 2017"
e_d = "Arp 29, 2017"

crs17 = Course(20159, "ART 101 10", "Introduction to Art", "Allendale", 3.000, "U", s_d, e_d, 
               "T", "6:00 pm - 8:50 pm", "Calder Art Center 1415", "Hornby", "W17")

crs18 = Course(27273, "CIS 163 03", "Computer Science II", "Allendale", 4.000, "U", s_d, e_d, 
               "T | MWF", "11:00 am - 11:50 am", " Mackinac Hall A1171", "Ferguson", "W17")

crs19 = Course(30966, "PHY 230 40", "Principles of Physics I", "Pew", 5.000, "U", s_d, e_d, 
               "M | TR", "1:00 pm - 1:50 pm | 1:00 pm - 2:15 pm", 
               "Kennedy Hall of Engineering 124", "Krcmar", "W17")

crs20 = Course(30967, "PHY 230 41", "Principles of Physics I", "Pew", 0.000, "U", s_d, e_d, 
               "W", "1:00 pm - 1:50 pm", "Kennedy Hall of Engineering 124", "Krcmar", "W17")

crs21 = Course(23514, "PHY 230 904", "Principles of Physics I", "Pew", 0.000, "U", s_d, e_d,
               "R", "10:00 am - 11:50am", "Kennedy Hall of Engineering 107", "Oostdyk", "W17")

crs22 = Course(33328, "REL 100 04", "Religions of the World", "Allendale", 0.000, "U", 
               s_d, e_d, "TR", "4:00 pm - 5:15 pm", "The Connection 214", "Burnside", "W17")




#2017 - 2018 Acadmeic year
#   Fall   2017
s_d = "Aug 28, 2017"
e_d = "Dec 16, 2017"

crs23 = Course(25392, "CIS 241 01", "System-Level Progamming and Utilities", "Allendale", 
               3.000, "U", s_d, e_d, "TR", "4:00 pm - 5:15 pm", "Mackinac Hall B2235", 
               "Wang", "F17")

crs24 = Course(17908, "CIS 263 02", "Data Structures and Algorithm Analysis", "Allendale", 
               3.000, "U", s_d, e_d, "MW", "4:00 pm - 5:15 pm", "Mackinac Hall B2235", 
               "Dulimarta", "F17")

crs25 = Course(24836, "CIS 290", "CIS Internship Prep", "Allendale", 1.000, "U", s_d, e_d, 
               "R", "3:00 pm - 3:50 pm", "Mackincac Hall D1117", "Lange", "F17")

crs26 = Course(20998, "CIS 350 02", "SWS Intro Software Egr", "Allendale", 3.000, "U", 
               s_d, e_d, "MWF", "10:00 am - 10:50 am", "Mackinac Hall D1117", "Nandigam",
               "F17")

crs27 = Course(21158, "MTH 325 02", "Discrete Structures: Computer Science II", "Allendale", 
               3.000, "U", s_d, e_d, "MWF", "11:00 am - 11:50 am", "Mackinac Hall BLL118", 
               "Santana", "F17")



#   Winter 2018
s_d = "Jan 08, 2018"
e_d = "Apr 28, 2018"

crs28  = Course(27303, "CIS 343 02", "Structures of Programming Languages", "Allendale", 
                3.000, "U", s_d, e_d, "MWF", "3:00 pm - 3:50 pm", "Makcinac Hall B1118", 
                "Woodring", "W18")

crs29  = Course(27323, "CIS 457 10", "Data Communications", "Allendale", 4.000, 
                "U", s_d, e_d, "MWF", "2:00 pm - 2:50 pm", "Mackinac Hall D1117", 
                "Kalafut", "W18")

crs30  = Course(30171, "CIS 457 902", "Data Communications", "Allendale", 0.000, "U", 
                s_d, e_d, "W", "10:00 am - 11:50 am", "Mackinac Hall A1167", 
                "Kalafut", "W18")

crs31  = Course(23260, "PSY 101 02", "Introductory Pyschology", "Allendale", 3.000, "U", 
                s_d, e_d, "TR", "10:00 am - 11:15 am", "Lake Huron Hall 132", 
                "Henderson", "W18")

crs32  = Course(34420, "WRT 350 08", "SWS Business Communication", "Allendale", 3.000, "U", 
                s_d, e_d, "R | T", "1:00 pm - 2:15 pm", 
                "Mackinac Hall A1121 | Mackinac Hall D1227",
                "Dine", "W18")
crs33  = Course(27305, "CIS 353 01", "Database", "Allendale", 3.000, "U", s_d, e_d, "MWF",
                "12:00 pm - 12:50 pm", "Mackinac Hall B1118", "Alsabbagh", "W18")


#2018 - 2019 Acadenic year 
#   Fall   2018 

s_d = "Aug 27, 2018"
e_d = "Dec 15, 2018"

crs34 = Course(26857, "CIS 351 01", "Computer Organization and Assembly Language", 
               "Allendale", 4.000, "U", s_d, e_d, 
               "MWF | T", "8:00 am - 8:50 am | 1:00 pm - 2:50 pm", 
               "Mackinac Hall B1118 | Mackinac Hall A1105", "Kurmas", "F18") 

crs35 = Course(25394, "CIS 357 01", "Mobile Application Development", "Allendale", 3.000, 
               "U", s_d, e_d, "MWF", "1:00 pm - 1:50 pm", "Mackinac Hall A1105", "Engelsma",
               "F18")

crs36 = Course(16977, "ENG 386 01", "Literary Responses to Death and Dying", "Allendale", 
               3.000, "U", s_d, e_d, "M", "6:00 pm - 8:50 pm", "Lake Huron Hall 122", 
               "Persoon", "F18")



#   Winter 2019 

s_d = "Jan 07, 2019" 
e_d = "Apr 27, 2019"

crs37 = Course(32050, "CIS 365 01", "Artificial Intelligence", "Allendale", 3.000, 
               "U", s_d, e_d, "TR", "10:00 am - 11:15 am", 
               "Mackinac Hall D1117", "Moore","W19")

crs38 = Course(33845, "CIS 371 01", "Web Application Programming", "Allendale", 3.000, 
               "U", s_d, e_d, "MWF", "2:00 pm - 2:50 pm", 
               "Mackinac Hall D1117", "TBA",  "W19")

crs39 = Course(31031, "CIS 452 20", "Operating Systems Concepts", "Allendale", 4.000, 
               "U", s_d, e_d, "MWF", "1:00 pm - 1:50 pm", 
               "Mackinanc Hall B2235", "Moore","W19") 

crs40 = Course(33381, "CIS 452 201", "Operatig Systems Concepts", "Allendale", 0.000, 
               "U", s_d, e_d, "R",  "1:00 pm - 2:50 pm", 
               "Mackinac Hall A1105",  "Moore","W19")

crs41 = Course(32738, "CIS 467 02", "Computer Science Project", "Allendale", 3.000, 
               "U", s_d, e_d, "TR", "8:30 am - 9:45 am", 
               "Mackinac Hall D1117", "Adams","W19")


#Delete all rows in table
#db.session.query(Course).filter(Course.title == "Database").delete()

#Add all courses to data base - test with commit
#db.session.add(crs01) # Added 
#db.session.add(crs02) # Added
#db.session.add(crs03) # Added
#db.session.add(crs04) # Added
#db.session.add(crs05) # Added
#db.session.add(crs06) # Added
#db.session.add(crs07) # Added
#db.session.add(crs08) # Added
#db.session.add(crs09) # Added
#db.session.add(crs10) # Added
#db.session.add(crs11) # Added
#db.session.add(crs12) # Added
#db.session.add(crs13) # Added
#db.session.add(crs14) # Added
#db.session.add(crs15) # Added
#db.session.add(crs16) # Added
#db.session.add(crs17) # Added
#db.session.add(crs18) # Added
#db.session.add(crs19) # Added
#db.session.add(crs20) # Added
#db.session.add(crs21) # Added
#db.session.add(crs22) # Added
#db.session.add(crs23) # Added
#db.session.add(crs24) # Added
#db.session.add(crs25) # Added
#db.session.add(crs26) # Added
#db.session.add(crs27) # Added
#db.session.add(crs28) # Added
#db.session.add(crs29) # Added
#db.session.add(crs30) # Added
#db.session.add(crs31) # Added
#db.session.add(crs32) # Added
#db.session.add(crs33) # Added
#db.session.add(crs34) # Added
#db.session.add(crs35) # Added
#db.session.add(crs36) # Added
#db.session.add(crs37) # Added
#db.session.add(crs38) # Added
#db.session.add(crs39) # Added
#db.session.add(crs40) # Added
#db.session.add(crs41) # Added

#Commit the changes to the database.
db.session.commit()
