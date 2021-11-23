import fitz         
import pandas
import numpy
df = pandas.read_csv('bigDonorTest.csv',encoding = 'unicode_escape')#,error_bad_lines=False
nameLen = 0
longestName = ""

# For each of the lines in the csv create a donor card and certificate
for index, row in df.iterrows():
    #The template for the certificate
    cert = fitz.open("template/certificate.pdf")  # or new: fitz.open(), followed by insertPage()
    pagecert = cert[0]
    
    
    #The template for the certificate
    doc = fitz.open("template/donor_card.pdf")           # or new: fitz.open(), followed by insertPage()
    page = doc[0]   # choose some page
    if (str(row["Full Name"]) != "nan"):
        firstName = str(row["Full Name"])
    else:
        firstName = ""
        print("No First Name Found!!!!!!!!!!!!!!!!!!!!!!!")
    if (str(row["Middle Name"]) != "nan"):
        middleName = str(row["Middle Name"])
    else:
        middleName = ""
    if (row["Last Name"] != "nan"):
        lastName = str(row["Last Name"])
    else:
        lastName = ""

    textName = firstName +" "+ middleName +" "+ lastName
    if(nameLen < len(textName)):
        nameLen = len(textName)
        longestName = textName
    certName = fitz.Rect(140, 120, 714, 265)   # rectangle (left, top, right, bottom) in pixels

    pagecert.insertTextbox(certName, textName, fontsize = 30, # choose fontsize (float)
                       color=0,
                       fontname = "Times-Roman",       # a PDF standard font
                       fontfile = None,                # could be a file on your system
                        align = 1)                      # 0 = left, 1 = center, 2 = right

    rectName = fitz.Rect(64, 244, 300, 265)   # rectangle (left, top, right, bottom) in pixels
    textNextOfKinName = row["Next of Kin"]
    textNextOfKinNumber = row["Next of Kin's Phone No"]
    textNextOfKinAll = textNextOfKinName + ", " + str(int(textNextOfKinNumber))
    rectNextOfKin = fitz.Rect(313, 180, 500, 460)  # rectangle (left, top, right, bottom) in pixels

    rectRegNum = fitz.Rect(433, 118, 600, 165)
    textX = "X"
    textRegNum = row["Registration Number"]
    rectAllOrgans = fitz.Rect(514, 192, 530, 600)  # rectangle (left, top, right, bottom) in pixels
    rectAllTissues = fitz.Rect(545, 206, 590, 600)  # rectangle (left, top, right, bottom) in pixels

    #Puts the next of kin name and phone-number that is saved in textNextOfKinAll
    page.insertTextbox(rectNextOfKin, textNextOfKinAll, fontsize = 8, # choose fontsize (float)
                       color=0,
                       fontname = "Times-Roman",       # a PDF standard font
                       fontfile = None,                # could be a file on your system
                        align = 0)                      # 0 = left, 1 = center, 2 = right

    page.insertTextbox(rectName, textName, fontsize = 9, # choose fontsize (float)
                       color = 0,
                        fontname = "Times-Bold",       # a PDF standard font
                       fontfile = None,                # could be a file on your system
                        align = 1)                      # 0 = left, 1 = center, 2 = right
    page.insertTextbox(rectRegNum, textRegNum, fontsize=12,  # choose fontsize (float)
                       color=0,

                       fontname="Times-Roman",  # a PDF standard font
                            fontfile=None,  # could be a file on your system
                            align=0)  # 0 = left, 1 = center, 2 = right

#-------------------ORGANS--------------------
    rectHeart = fitz.Rect(347, 192, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectLungs = fitz.Rect(372, 192, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectKidney = fitz.Rect(405, 192, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectLiver = fitz.Rect(428, 192, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectPancreas = fitz.Rect(461, 192, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectIntestine = fitz.Rect(495, 192, 520, 460)  # rectangle (left, top, right, bottom) in pixels
#------------------Tissues--------------------
    rectCorneas = fitz.Rect(384, 206, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectSkin = fitz.Rect(406, 206, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectBones = fitz.Rect(432, 206, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectHeartValves = fitz.Rect(478, 206, 500, 460)  # rectangle (left, top, right, bottom) in pixels
    rectBloodVessels = fitz.Rect(525, 206, 550, 460)  # rectangle (left, top, right, bottom) in pixels


    organs = row["Organs that I wish to donate"].split(",")
    # Fill in all the fields in the form
    if "ALL" in organs:
        page.insertTextbox(rectAllOrgans, textX, fontsize=9,  # choose fontsize (float)
                           color=0,   #Sets the color to black, remove if you want it to be red
                           fontname="Times-Roman",  # a PDF standard font
                                 fontfile=None,  # could be a file on your system
                                 align=0)  # 0 = left, 1 = center, 2 = right
        page.insertTextbox(rectAllTissues, textX, fontsize=9,  # choose fontsize (float)
                           color=0,
                           fontname="Times-Roman",  # a PDF standard font
                                 fontfile=None,  # could be a file on your system
                                 align=0)  # 0 = left, 1 = center, 2 = right'
    else:
        print(textName, organs)
        if "HEART" in organs:
            page.insertTextbox(rectHeart, textX, fontsize = 9,  # choose fontsize (float)
                               color=0,  # Sets the color to black, remove if you want it to be red
                               fontname = "Times-Roman",  # a PDF standard font
                               fontfile = None,  # could be a file on your system
                               align = 0)                      # 0 = left, 1 = center, 2 = right
        if "LUNGS" in organs:
            rcK = page.insertTextbox(rectLungs, textX, fontsize = 9,  # choose fontsize (float)
                                     color=0,  # Sets the color to black, remove if you want it to be red
                                     fontname = "Times-Roman",  # a PDF standard font
                                     fontfile = None,  # could be a file on your system
                                     align = 0)                      # 0 = left, 1 = center, 2 = right
        if "KIDNEYS" in organs:
            #print(True)

            page.insertTextbox(rectKidney, textX, fontsize = 9,  # choose fontsize (float)
                               fontname = "Times-Roman",  # a PDF standard font
                               color=0,  # Sets the color to black, remove if you want it to be red
                               fontfile = None,  # could be a file on your system
                               align = 0)                      # 0 = left, 1 = center, 2 = right
        if "LIVER" in organs:
            #print("LIVERS")

            page.insertTextbox(rectLiver, textX, fontsize = 9,  # choose fontsize (float)
                               fontname = "Times-Roman",  # a PDF standard font
                               color=0,  # Sets the color to black, remove if you want it to be red
                               fontfile = None,  # could be a file on your system
                               align = 0)                      # 0 = left, 1 = center, 2 = right
        if "PANCREAS" in organs:
            page.insertTextbox(rectPancreas, textX, fontsize = 9, # choose fontsize (float)
                               color=0,  # Sets the color to black, remove if you want it to be red
                                fontname = "Times-Roman",       # a PDF standard font
                               fontfile = None,                # could be a file on your system
                                align = 0)                      # 0 = left, 1 = center, 2 = right
        if "SMALL INTESTINE" in organs:
            page.insertTextbox(rectIntestine, textX, fontsize = 9, # choose fontsize (float)
                               color=0,  # Sets the color to black, remove if you want it to be red
                                fontname = "Times-Roman",       # a PDF standard font
                               fontfile = None,                # could be a file on your system
                                align = 0)                      # 0 = left, 1 = center, 2 = right
        if "CORNEAS" in organs:
            page.insertTextbox(rectCorneas, textX, fontsize=9,  # choose fontsize (float)
                               color=0,  # Sets the color to black, remove if you want it to be red
                               fontname="Times-Roman",  # a PDF standard font
                               fontfile=None,  # could be a file on your system
                               align=0)  # 0 = left, 1 = center, 2 = right
        if "SKIN" in organs:
            page.insertTextbox(rectSkin, textX, fontsize = 9, # choose fontsize (float)
                               color=0,  # Sets the color to black, remove if you want it to be red
                                fontname = "Times-Roman",       # a PDF standard font
                               fontfile = None,                # could be a file on your system
                                align = 0)                      # 0 = left, 1 = center, 2 = right
        if "BONES" in organs:
            page.insertTextbox(rectBones, textX, fontsize = 9, # choose fontsize (float)
                               color=0,  # Sets the color to black, remove if you want it to be red
                                fontname = "Times-Roman",       # a PDF standard font
                               fontfile = None,                # could be a file on your system
                                align = 0)                      # 0 = left, 1 = center, 2 = right
        if "HEART VALVES" in organs:
            page.insertTextbox(rectHeartValves, textX, fontsize = 9, # choose fontsize (float)
                               color=0,  # Sets the color to black, remove if you want it to be red
                                fontname = "Times-Roman",       # a PDF standard font
                               fontfile = None,                # could be a file on your system
                                align = 0)                      # 0 = left, 1 = center, 2 = right
        if "BLOOD VESSLES" in organs:
            page.insertTextbox(rectBloodVessels, textX, fontsize = 9, # choose fontsize (float)
                               color=0,  # Sets the color to black, remove if you want it to be red
                                fontname = "Times-Roman",       # a PDF standard font
                               fontfile = None,                # could be a file on your system
                                align = 0)                      # 0 = left, 1 = center, 2 = right



    saveName = textName+str(index)+".pdf"
    certSaveName = textName+str(index)+"Certificate.pdf"
    doc.save(saveName)   # update file. Save to new instead by doc.save("new.pdf",...)
    cert.save(certSaveName)

