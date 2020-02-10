from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html',title = "Contact")

@app.route('/team')
def team():
    return render_template('team.html',title = "Team")

@app.route('/Technical-Events')
def techEvents():
    noOf = 9
    events = ["paperPresenation",
              "projectExpo",
              "rosieTheProgrammer",
              "procoding",
              "blindCoding",
              "switcheroo",
              "hackCon",
              "BTP",
              "tresureTrove"]

    psFile = ["dist/event-posters/Paper-Presentation.jpg",
              "dist/event-posters/Project-Expo.jpg",
              "dist/event-posters/Rosie-the-Wrogrammer.jpg",
              "dist/event-posters/Procoding.jpg",
              "dist/event-posters/Blind-Coding.jpg",
              "dist/event-posters/Switcheroo.jpg",
              "dist/event-posters/HackCon.jpg",
              "dist/event-posters/BTP.jpg",
              "dist/event-posters/TreasureHunt.jpg"]

    return render_template('event-list-layout.html',title = "Technical Events",
                            eventType = "Technical", 
                            noOf = noOf, 
                            events = events,
                            psFile = psFile)


@app.route('/paperPresentation')
def paperPresenation():
    psFile = "dist/event-posters/Paper-Presentation.jpg"
    wsAlt = "Paper Presentation"
    name = "Paper Presentation"
    date = "5th March ,2020"
    time = "Yet to be annouced"
    description = "Paper Presentation is an event that gives budding researchers an opportunity to present their ideas and research and bring out their insights about a topic in front of an esteemed panel of judges."

    rules = [ "> 	Team Members - 2 to 4." ,
              "> 	Abstract submission latest by 1st of March.",
              "> 	Time Constraint for each Team - 5 to 7 mins.", 
              "> 	If the team is under or over the time limit, every 30 seconds the team would be deducted 2 points.",
              "> 	Judges decision is final.",
              "> 	Organizers have the right to disallow/disqualify any participant.",
              "> 	Preference will be given to original papers.",
              "> 	Working models, Samples fetches you extra points.",
              ">	Detail of team members: Name, Year, Department, Institute, Contact number, Topic and its description should be  mentioned in abstract.The description should be of minimum 120 words to maximum 150",
              "> 	A participant should not submit more than two papers.",
              "> 	No participant can be a part of more than one team",
              "> 	There are no restrictions on the number of teams from same college."              
            ]
    contacts = ["Rohini | +91 98406 68223", "Pooja priyadarshni | +91 98417 59321", "E.S.Vikashini sruthi | +91 96000 98232"]
    return render_template('description_layout.html',title = "Paper Presentation",
                            eventType = "WS",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description
                           )
@app.route('/projectExpo')
def projectExpo():
    psFile = "dist/event-posters/Project-Expo.jpg"
    wsAlt = "Project Expo"
    name = "Project Expo"
    date = "6th March ,2020"
    time = "Yet to be annouced"
    description = "Cogito-20 is bringing Project Expo to all the aspiring Engineers and Developers who are looking for a platform to showcase their ideas/dreams in front of an esteemed panel of established innovators, inventors and ideators. So come on and showcase your best ideas at Cogito-20."

    rules = [ "> 	This competition is open to all departments except (MechanicalEngineering, AeroSpace Engineering and Civil Engineering.)" ,
              "> 	Any institute/college can send any number of entries." ,
              "> 	Project can be in the form of a working model |software |simulation based | industry sponsored | experiments | prototype.",
              "> 	Team members of a team should belong to the same institution.",
              "> 	The number of students per project shall not exceed five.",
              "> 	Entry fee for each model will be Rs 300/- payable by cash or Online.Entry fee is not refundable.",
              "> 	The decision given by judges in all matters will be final."
            ]
    contacts = ["Shasanth | +91 96771 83202", "Deepak Sharran  | +91 74180 23612", "Manoj Kumar | +91 73585 17185"]
    return render_template('description_layout.html',title = "Project Expo",
                            eventType = "WS",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description
                           )
@app.route('/rosieTheProgrammer')
def rosieTheProgrammer(): 
    psFile = "dist/event-posters/Rosie-the-Wrogrammer.jpg"
    wsAlt = "Rosie the Wrogrammer"
    name = "Rosie the Wrogrammer"
    date = "5th March ,2020"
    time = "Yet to be annouced"
    description = "Wogrammer is an onsite programming contest specially to encourage women interested in Competitive Programming organised by CSI STUDENT BRANCH for COGITO-2020. Wogrammer is an event in which the brightest women across the nation compete against each other to solve algorithmic problems."

    rules = [ "> 	This competition is open to all departments except (MechanicalEngineering, AeroSpace Engineering and Civil Engineering.)" ,
              "> 	Any institute/college can send any number of entries." ,
              "> 	Project can be in the form of a working model |software |simulation based | industry sponsored | experiments | prototype.",
              "> 	Team members of a team should belong to the same institution.",
              "> 	The number of students per project shall not exceed five.",
              "> 	Entry fee for each model will be Rs 300/- payable by cash or Online.Entry fee is not refundable.",
              "> 	The decision given by judges in all matters will be final."
            ]
    contacts = ["Shasanth | +91 96771 83202", "Deepak Sharran  | +91 74180 23612", "Manoj Kumar | +91 73585 17185"]
    return render_template('description_layout.html',title = "Project Expo",
                            eventType = "WS",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description
                           )
@app.route('/procoding')
def procoding():
    return render_template('description_layout.html')
@app.route('/blindCoding')
def blindCoding():
    return render_template('description_layout.html')
@app.route('/switcheroo')
def switcheroo():
    return render_template('description_layout.html')
@app.route('/hackCon')
def hackCon():
    return render_template('description_layout.html')
@app.route('/BTP')
def BTP():
    return render_template('description_layout.html')
@app.route('/treasureTrove')
def tresureTrove():
    return render_template('description_layout.html')



@app.route('/Non-Technical-Events')
def nonTechEvents():
    noOf = 5
    events = ["googleIT",
              "ZPT",
              "improvBattle",
              "adzap",
              "geekSquad"
             ]

    psFile = ["dist/event-posters/Google-It.jpg",
              "dist/event-posters/zpt.jpg",
              "dist/event-posters/TheImprovBattle.jpg",
              "dist/event-posters/Adzap.jpg",
              "dist/event-posters/Geeks.jpg"
              ]
    
    return render_template('event-list-layout.html',title = "Non-Technical Events",
                            eventType = "Non Technical", 
                            noOf = noOf,
                            events = events,
                            psFile = psFile)

@app.route('/googleIT')
def googleIT():
    return render_template('description_layout.html')
@app.route('/ZPT')
def ZPT():
    return render_template('description_layout.html')
@app.route('/improvBattle')
def improvBattle():
    return render_template('description_layout.html')
@app.route('/adzap')
def adzap():
    return render_template('description_layout.html')
@app.route('/geekSquad')
def geekSquad():
    return render_template('description_layout.html')

@app.route('/UI&UX-Design')
def uiUxDesign():

    psFile = "dist/workshop-posters/UX-UI-Workshop.png"
    wsAlt = "UI & UX Workshop"
    name = "UI & UX Design workshop"
    date = "5th March ,2020"
    time = "8:30 am to 2:45pm"
    description = "User interface design or user interface engineering is the design of user interfaces for machines and software, such as computers, home appliances, mobile devices, and other electronic devices, with the focus on maximizing usability and the user experience.  So come get hands on with UI and UX design with our industry expert from DoodleBlue Innovations."
    rules = [ ">	As seats are offered in first come first serve basis, so kindly register through the online portal to get an assured seat." ,
              "> 	Each attendee should bring their own Laptop.",
              ">    There will be no refund of money once paid.", 
              "> 	Please carry your college IDs."]
    contacts = ["Sanjay Kumar | sanjaykumarx@yahoo.in | +91 99419 10062","Calvin Kumar | thecalvin10101@gmail.com | +91 99403 09162"]
    return render_template('description_layout.html',title = "UI & UX Design",
                            eventType = "WS",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description
                           )
                    
@app.route('/TensorflowWorkshop')
def tensorWorkshop():

    psFile = "dist/workshop-posters/GDG-Workshop-poster.png"
    wsAlt = "Introduction to Machine Learning with Tensorflow Workshop"
    name = "Introduction to Machine Learning with Tensorflow Workshop"
    date = "6th March ,2020"
    time = "8:30 am to 2:45pm"
    description = "JEC CSI in collaboration with the Google Developers Club proudly brings you an Hands on workshop on Machine Learning with TensorFlow to all the passionate learners."
    rules = [ ">	As seats are offered in first come first serve basis, so kindly register through the online portal to get an assured seat." ,
              "> 	Each attendee should bring their own Laptop.",
              ">    There will be no refund of money once paid.", 
              "> 	Please carry your college IDs."]
    contacts = ["Febron Rodriguez | me.ifebronr@gmail.com | +91 9953072714","V Balaji | vbalaji65@gmail.com | +91 81245 44723"]
    link = "ff"
    return render_template('description_layout.html',title = "UI & UX Design",
                            eventType = "WS",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            
                           )

@app.route('/schedule')
def schedule():
    return render_template('schedules.html',title = "Schedule")





if __name__== '__main__':
    app.run(debug=True)