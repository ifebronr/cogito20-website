from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/cog21')
def cog21():
    return render_template('cog21.html')
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
    time = "Schedule will be announced on 1st March,2020"
    description = "Paper Presentation is an event that gives budding researchers an opportunity to present their ideas and research and bring out their insights about a topic in front of an esteemed panel of judges."
    link = "https://forms.gle/QsvJh2mLoE9KQ9hq8"
    rules = [ "> 	Team Members - 2 to 4." ,
              "> 	Abstract submission latest by 1st of March.",
              "> 	Time Constraint for each Team - 5 to 7 mins.", 
              "> 	If the team is under or over the time limit, every 30 seconds the team would be deducted 2 points.",
              "> 	Judges' decisions are final.",
              "> 	Organizers have the right to disallow/disqualify any participant.",
              "> 	Preference will be given to original papers.",
              "> 	Working models, Samples fetches you extra points.",
              ">	Detail of team members: Name, Year, Department, Institute, Contact number, Topic and its description should be  mentioned in abstract.The description should be of minimum 120 words to maximum 150",
              "> 	A participant should not submit more than two papers.",
              "> 	No participant can be a part of more than one team",
              "> 	There are no restrictions on the number of teams from same college."              
              "> 	Last date to send ABSTRACT : 1st March , 2020",              
              "> 	Send the ABSTRACT to cogito.jeccsi@gmail.com"             
            ]
    contacts = ["Rohini | +91 98406 68223", "Pooja priyadarshni | +91 98417 59321", "E.S.Vikashini sruthi | +91 96000 98232"]
    return render_template('description_layout.html',title = "Paper Presentation",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/projectExpo')
def projectExpo():
    psFile = "dist/event-posters/Project-Expo.jpg"
    wsAlt = "Project Expo"
    name = "Project Expo"
    date = "6th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "Cogito-20 is bringing Project Expo to all the aspiring Engineers and Developers who are looking for a platform to showcase their ideas/dreams in front of an esteemed panel of established innovators, inventors and ideators. So come on and showcase your best ideas at Cogito-20."
    link = "https://forms.gle/9yBNpZeErshVTpCb6"
    rules = [ "> 	This competition is open to all departments except (MechanicalEngineering, AeroSpace Engineering and Civil Engineering.)" ,
              "> 	Any institute/college can send any number of entries." ,
              "> 	Project can be in the form of a working model |software |simulation based | industry sponsored | experiments | prototype.",
              "> 	Team members of a team should belong to the same institution.",
              "> 	The number of students per project shall not exceed five.",
              "> 	Entry fee for each model will be Rs 300/- payable by Cash or Online.Entry fee is not refundable.",
              "> 	The decision given by judges in all matters will be final.",
              "> 	Last date to send ABSTRACT : 1st March , 2020",              
              "> 	Send the ABSTRACT to cogito.jeccsi@gmail.com"
            ]
    contacts = ["Shasanth | +91 96771 83202", "Deepak Sharran  | +91 74180 23612", "Manoj Kumar | +91 73585 17185"]
    return render_template('description_layout.html',title = "Project Expo",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/rosieTheProgrammer')
def rosieTheProgrammer(): 
    psFile = "dist/event-posters/Rosie-the-Wrogrammer.jpg"
    wsAlt = "Rosie the Wrogrammer"
    name = "Rosie the Wrogrammer"
    date = "5th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "Wogrammer is an onsite programming contest specially to encourage women interested in Competitive Programming organised by CSI STUDENT BRANCH for COGITO-2020. Wogrammer is an event in which the brightest women across the nation compete against each other to solve algorithmic problems."
    link = "https://forms.gle/QQK1matEetZA7XGbA"
    rules = [ "> 	This is a solo event only for women" ,
              "> 	Registration for the event closes 30 mins prior to the event." ,
              "> 	Registered Participants must be present in the venue at least 10 minutes before the start of the event.",
              "> 	Participants are not allowed to access the internet during the contest.",
              "> 	Carrying your institutions ID card is a must.",
              "> 	Usage of  electronic device other than allotted PC is will result in a disqualification",
              "> 	Organizers have the right to disallow/disqualify any participant."
              "> 	Prilims might be there"
            ]
    contacts = ["Vaishanavi | +91 96191 92657", "Mansy | +91 7397669094"]
    return render_template('description_layout.html',title = "Rosie the Wrogrammer",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/procoding')
def procoding():
    psFile = "dist/event-posters/Procoding.jpg"
    wsAlt = "Procoding"
    name = "Procoding"
    date = "5th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "Pro Coding is an onsite event where some of the enthusiastic coders compete against each other to solve some challenges. These challenges will test your basic and advanced coding skills."
    link = "https://forms.gle/RC22JxYhvq4EAPUr6"
    rules = [ "> 	This is a solo event" ,
              "> 	Registration for the event closes 30 mins prior to the event." ,
              "> 	Registered Participants must be present in the venue at least 15 minutes before the start of the event.",
              "> 	Use of the internet is strictly prohibited",
              "> 	Carrying your institution ID card is a must.",
              "> 	Use of any electronic device other than your allotted PC is strictly prohibited",
              "> 	Organizers have the right to disallow/disqualify any participant.",
              "> 	Event open to all students(Regardless of the batch).",
              "> 	Prilims might be there",
              
            ]
    contacts = ["Deepan | +91 638O3 O87O1", "Saravanan A P | +91 99626 97951 ","Varun| +91 89390 06706"]

    return render_template('description_layout.html',title = "Procoding",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link =  link
                           )
@app.route('/blindCoding')
def blindCoding():
    psFile = "dist/event-posters/Blind-Coding.jpg"
    wsAlt = "Blind Coding"
    name = "Blind Coding"
    date = "6th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "A fun event spanning over two rounds, Blind Coding is a coding challenge with a twist.It is a fresh and offbeat concept - where the participants need to write and compile their program with the monitor screens switched off."
    link = "https://forms.gle/2pPGkWdqMgPpAsw8A"
    rules = [ "> 	The participants will be given 3 problems of varying difficulty levels" ,
              "> 	Registration for the event closes 30 mins prior to the event." ,
              "> 	Registered Participants must be present in the venue at least 15 minutes before the start of the event.",
              "> 	Use of the internet is strictly prohibited",
              "> 	Carrying your institution ID card is a must.",
              "> 	Use of any electronic device other than your allotted PC is strictly prohibited",
              "> 	Any kind of violation of these rules will mean immediate disqualification of the team",
              "> 	Event open to all students(Regardless of the batch).",
              "> 	Prilims might be there",
              
            ]
    contacts = ["Abishek | +91 93446 31494 ", "P.Soumiya | +91 78249 26317","VS.Yahzhini | 99426 28171"]

    return render_template('description_layout.html',title = "Blind Coding",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/switcheroo')
def switcheroo():
    psFile = "dist/event-posters/Switcheroo.jpg"
    wsAlt = "Switcheroo"
    name = "Switcheroo"
    date = "5th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "Switcheroo is not just regular coding competition, this event not only tests your programming skills as an individual but also how efficiently you can coordinate with your teammate under tense situation."
    link = "https://forms.gle/DJhFHS6gTLzDY5rZ9"
    rules = [ "> 	Teams size: 2 members" ,
              "> 	Member of the team will be seated in different rooms. They will be given different sets of questions to code." ,
              "> 	Periodically, members of the team will switch their positions, i.e, switch their PCs so that the first team member completes the code of their partner. Same follows for the second team member.",
              "> 	Members of a team are not allowed to speak to each other at any time.",
              "> 	No electronic devices would be allowed inside the lab during the event.",
              "> 	Usage of the Internet is prohibited during the contest.",
              "> 	Any kind of violation of these rules will mean immediate disqualification of the team",
              "> 	Event open to all students(Regardless of the batch).",
              "> 	Prilims might be there",
              
            ]
    contacts = ["Joseph Dave | +91 87544 01014"]

    return render_template('description_layout.html',title = "Switchroo",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )


@app.route('/hackCon')
def hackCon():
    psFile = "dist/event-posters/HackCon.jpg"
    wsAlt = "HackCon"
    name = "HackCon(Online)"
    date = "5th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "Its an Online Hacking tournament"
    link = " https://forms.gle/5fokNaFDcxJNjEsAA"
    rules = [ "> 	It's strictly forbidden to perform any kind of Denial of Service Attack (DoS/DDoS) against the servers or the competition's infrastructure" ,
              "> 	Do NOT try to use Brute Force on the flag submission system because the flags are not possible to guess" ,
              "> 	Do NOT try to exchange flags or write-ups during the competition",
              "> 	Do NOT share recent discoveries related to challenges publicly on any channels, nor in any other way with contestants of other teams",
              "> 	Clues will be given in a direct or indirect form stay alert!",
              "> 	The flag pattern will be as follows: CTF{something_here}",
              "> 	The teams may have maximum of 3",
              "> 	Any kind of violation of these rules will mean immediate disqualification of the team",
              "> 	The HackCon Portal will be released on the day of the tournament"
              
            ]
    contacts = ["V Balaji | +91 81245 44723","Bharat | +91 78714 34120"]

    return render_template('description_layout.html',title = "HackCon(Online)",
                            eventType = "O",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/BTP')
def BTP():
    psFile = "dist/event-posters/BTP.jpg"
    wsAlt = "Breaking the Patriarchy"
    name = "Breaking the Patriarchy"
    date = "6th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "As women’s day is coming closer Cogito-20 Team wants to celebrate the equality between men & women and wants to break the stereotypes in the IT sector by promoting a healthy competition between all the programmers and Wogrammers, who aspire to be future IT enthusiasts."
    link = "https://forms.gle/mJssUiZB3au7hhi5A"
    rules = [ "> 	Team of 2 (consisting of either 2 men or 2 women)." ,
              "> 	Teams will be given programming questions of varying difficulties." ,
              "> 	The team that scores the highest points wins",
              "> 	Teams must register online and must have the entry ticket.",
              "> 	Team members can be from different colleges."              
            ]
    contacts = ["Angeline | +91 95971 05608","Vasundhara | 9176964372"]

    return render_template('description_layout.html',title = "Breaking the Patriarchy",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
    
@app.route('/treasureTrove')
def tresureTrove():
    psFile = "dist/event-posters/TreasureHunt.jpg"
    wsAlt = "Treasure Trove"
    name = "Treasure Trove"
    date = "5th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "The game is simple, clues will be hidden around the college and the first clue will be given to the teams , the teams need to find the clues and using the clues the teams need to complete the code within the stipulated time."
    link = "https://forms.gle/E3mmRGxsV5DadJy6A"
    rules = [ "> 	Team Size: 2 - 3." ,
              "> 	Code the given problem statement in the stipulated time." ,
              "> 	Submit the correct answer in the given platform.",
              "> 	Any type of unfair mean will result in an immediate disqualification of the team."              
            ]
    contacts = ["M S Nishaanth  | +91 73582 72962","Kishoreganesh S | +91 63799 54718","Jayanth | +91 97906 81711"]

    return render_template('description_layout.html',title = "Teasure Trove",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
    



@app.route('/Non-Technical-Events')
def nonTechEvents():
    noOf = 6
    events = ["googleIT",
              "ZPT",
              "improvBattle",
              "adzap",
              "geekSquad",
              "FMS"
             ]

    psFile = ["dist/event-posters/Google-It.jpg",
              "dist/event-posters/zpt.jpg",
              "dist/event-posters/TheImprovBattle.jpg",
              "dist/event-posters/Adzap.jpg",
              "dist/event-posters/Geeks.jpg",
              "dist/event-posters/FMS.jpg"
              ]
    
    return render_template('event-list-layout.html',title = "Non-Technical Events",
                            eventType = "Non Technical", 
                            noOf = noOf,
                            events = events,
                            psFile = psFile)

@app.route('/googleIT')
def googleIT():
    psFile = "dist/event-posters/Google-It.jpg"
    wsAlt = "Google It"
    name = "Google It"
    date = "6th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "You’ll be given a doodle from Doodles from Google in a piece of paper. Teams need to find out the year and the reason why the particular doodle was made."
    link = "https://forms.gle/Sb3Kt3tmh4mxg5Wy9"
    rules = [ "> 	Team Size: 1 - 2." ,
              "> 	We will provide a system to find the solutions." ,
              "> 	Don't share the answer with other's.",
              "> 	Questions will be provided as hardcopy.",              
              "> 	Clues will be given in direct or indirect form stay alert",             
              "> 	The competition will last for 45 minutes in a row, no breaks",             
              "> 	Two rounds will be conducted. In each round teams will be evaluated",             
              "> 	Any kind of violation of these rules will mean immediate disqualification of the team"             
            ]
    contacts = ["Seshathiri | +91 80727 71522","Kevin Lyton | +91 99944 54031","Jamal Mohamed shaul | +91 97907 27121"]

    return render_template('description_layout.html',title = "Google It",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/ZPT')
def ZPT():
    psFile = "dist/event-posters/zpt.jpg"
    wsAlt = "Zero Prerequisite Tournament"
    name = "Zero Prerequisite Tournament"
    date = "6th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "It is a fun event where you’ll be tested on your knowledge grasping abilities. You’ll be handed a set of documents which you’ll be using to solve a set of problems."
    link = "https://forms.gle/RYK94hBaeP58EW3aA"
    rules = [ "> 	Team Size: 1 - 2." ,
              "> 	Participants must register at least 30 mins prior to the start of the event." ,
              "> 	Participants must be present at the venue at least 15 mins prior to the start of the event.",
              "> 	You must carry your college/school ID card.",              
              "> 	We’ll give you all necessary documents",             
              "> 	Organiser’s  decision will be final."             
            ]
    contacts = ["M S Nishaanth  | +91 73582 72962","Kishoreganesh S | +91 63799 54718","Jayanth | +91 97906 81711"]

    return render_template('description_layout.html',title = "Zero Prerequisite Tournament",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link 
                           )
@app.route('/improvBattle')
def improvBattle():
    psFile = "dist/event-posters/TheImprovBattle.jpg"
    wsAlt = "The Improv Battle"
    name = "TheImprovBattle"
    date = "?6th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "Supporting the cliche that engineers can adapt,overcome and  improvise in any situation.Cogito 20 is bringing an improv battle to all the aspiring improv ‘ers, it's a  team based event where the teams will be given different situations / constraints asked from the audience and the teams need perform based on these constraints."
    link = "https://forms.gle/Y427xuzR1vvpXtej8"
    rules = [ "> 	Team Size: 4" ,
              "> 	Carry valid College IDs for registration." ,
              "> 	Language: Tamil, or English.",
              "> 	DO NOT use profanity while speaking(Might result in negative points or even disqualification).",              
              "> 	Judges’ decision is final."                         
            ]
    contacts = ["Joseph Dave | +91 87544 01014"]
    return render_template('description_layout.html',title = "The Improv Battle",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/adzap')
def adzap():
    psFile = "dist/event-posters/Adzap.jpg"
    wsAlt = "Adzap"
    name = "Adzap"
    date = "5th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "Adzap is set to bring out the creativity, time management, marketing skills of the innovative minds and to shape their team spirit and coordination. Each team must have a captain who can get in touch with the coordinators of the event. Once the topic is given, the teams can start with their discussion in the venue. The captains will be called to pick a chit from the lot and their team will perform in that order."
    link = "https://forms.gle/SBhXCPgmod436Nq1A"
    rules = [ "> 	Team Size: 4 - 6" ,
              "> 	Preparation Time : 30 minutes" ,
              "> 	Preformance Time : 3 - 5 minutes (above or below the duration will result in -1 point for every 30 seconds)" ,
              "> 	Language: Tamil, or English.",
              "> 	DO NOT use profanity while speaking(Might result in negative points or even disqualification).",              
              "> 	 A warning bell will be rung after 2.5 minutes to intimate the team about the time limit."                         
            ]
    contacts = ["Ishana | +91 88259 25157 "]
    return render_template('description_layout.html',title = "Adzap",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/geekSquad')
def geekSquad():
    psFile = "dist/event-posters/Geeks.jpg"
    wsAlt = "Geeksquad"
    name = "Geeksquad"
    date = "6th March ,2020"
    time = "Schedule will be announced on 1st March,2020"
    description = "Do you think you know all about tech? Do you think you’re the one above all geeks? Come participate in Geek Squad to show your inquisition about Tech!"
    link = "https://forms.gle/yzgmTq16zGDZmzn56"
    rules = [ ">	Team size - 2 to 4." ,
              "> 	There would be 2 rounds.",
              ">    First round, prelims - For every correct answer you get +1 point. You get +2 points for answers with 2 parts.", 
              "> 	Final round - For every bounce (First team to shout the answer) if the bounce is correct you get +10 points. If not -10 points."]
    contacts = ["Sanjay Kumar | +91 99419 10062","Calvin Kumar | +91 99403 09162"]
    return render_template('description_layout.html',title = "Geeksquad",
                            eventType = "E",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )
@app.route('/FMS')
def FMS():
    psFile = "dist/event-posters/FMS.jpg"
    wsAlt = "Flutter Me Shutters"
    name = "Flutter Me Shutters(online)"
    date = "Its already started start send your amazing pictures to us!!"
    time = "NA"
    description = "Flutter Me Shutters  is a National Level Photography competition, For details visit our Instagram page "
    link = "https://www.instagram.com/cogito_2020/"
    rules = [ ">	For every like you get one vote" ,
              "> 	Photos can be DM'ed to @cogito_2020 on Instagram or Email it to us at cogito.jeccsi@gmail.com ",
              ">    For you vote to count the participant must follow the @cogito_2020 on Instagram", 
              ">    Last date to vote is 1st of March,2020", 
              ">    Participants are advised to use #cogito20", 
              "> 	Results will be announced on 5th March ,2020 "]
    contacts = ["Saradha | +91 94458 76310"]
    return render_template('description_layout.html',title = "Flutter Me Shutters",
                            eventType = "O",
                            psFile = psFile,
                            wsAlt = wsAlt,
                            name = name,
                            date = date,
                            time = time,
                            rules = rules,
                            contacts = contacts,
                            description = description,
                            link = link
                           )











@app.route('/UI&UX-Design')
def uiUxDesign():

    psFile = "dist/workshop-posters/UX-UI-Workshop.jpg"
    wsAlt = "UI & UX Workshop"
    name = "UI & UX Design workshop"
    date = "5th March ,2020"
    time = "8:30 am to 2:45pm"
    description = "User interface design or user interface engineering is the design of user interfaces for machines and software, such as computers, home appliances, mobile devices, and other electronic devices, with the focus on maximizing usability and the user experience.  So come get hands on with UI and UX design with our industry expert from DoodleBlue Innovations."
    rules = [ ">	As seats are offered in first come first serve basis, so kindly register through the online portal to get an assured seat." ,
              "> 	Each attendee should bring their own Laptop.",
              ">    There will be no refund of money once paid.", 
              "> 	Please carry your college IDs."]
    link = "https://forms.gle/R1x5NN9Ct5ohWrP28"
    contacts = ["Sanjay Kumar | +91 99419 10062","Calvin Kumar | +91 99403 09162"]
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
                            link = link 
                           )
                    
@app.route('/TensorflowWorkshop')
def tensorWorkshop():

    psFile = "dist/workshop-posters/GDG-Workshop-poster.jpg"
    wsAlt = "Introduction to Machine Learning with Tensorflow Workshop"
    name = "Introduction to Machine Learning with Tensorflow Workshop"
    date = "6th March ,2020"
    time = "8:30 am to 2:45pm"
    description = "JEC CSI in collaboration with the Google Developers Club proudly brings you an Hands on workshop on Machine Learning with TensorFlow to all the passionate learners."
    rules = [ ">	As seats are offered in first come first serve basis, so kindly register through the online portal to get an assured seat." ,
              "> 	Each attendee should bring their own Laptop.",
              ">    There will be no refund of money once paid.", 
              "> 	Please carry your college IDs."]
    contacts = ["Febron Rodriguez | +91 9953072714","V Balaji | +91 81245 44723"]
    link = "https://forms.gle/R1x5NN9Ct5ohWrP28"
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
                            link = link
                            
                           )

@app.route('/schedule')
def schedule():
    return render_template('schedules.html',title = "Schedule")

"""=CONCATENATE(TEXT(TIME(8,COLUMN(A3)*30-30,0),"H:MM AM/PM"), "-" ,TEXT(TIME(8,COLUMN(A3)*30,0),"H:MM AM/PM"))"""



if __name__== '__main__':
    app.run(debug=True)