from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import csv
from tickets import ticket1,ticket2,ticket3
from banners import banner1, banner2, banner3
from certificates import certificate1, certificate2, certificate3
from mailing import registration_mail

####--------------------------------------Flask Configuration Starts---------------------------------------------------------------------------------------------------------------------------####
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eventlabs.db"
    db = SQLAlchemy()
    db.init_app(app)

    ####-------------------------------------Flask Configuration Ends-------------------------------------------------------------------------------------------------------------------------####


    ####------------------------------Database(Model) starts----------------------------------------------------------------------------------------------------------------------###

    class EventDetails(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        eventname = db.Column(db.String, nullable=False)
        orgname = db.Column(db.String, unique=True, nullable=False)
        orgweb = db.Column(db.String)
        venue = db.Column(db.String, nullable=False)
        startdate = db.Column(db.String, nullable=False)
        enddate = db.Column(db.String, nullable=False)
        starttime = db.Column(db.String, nullable=False)
        endtime = db.Column(db.String, nullable=False)
        logo = db.Column(db.String)
        signature = db.Column(db.String, nullable=False)
        cost = db.Column(db.Integer, nullable=False)
        walletaddress = db.Column(db.String, nullable=False)
        ticketTemplate = db.Column(db.String, nullable=False)
        certificateTemplate= db.Column(db.String, nullable=False)
        bannerTemplate= db.Column(db.String, nullable=False)

        def __init__(self, eventname, orgname, orgweb, venue, startdate, enddate, starttime, endtime, logo, signature, cost, walletaddress, ticketTemplate, certificateTemplate, bannerTemplate):
            self.eventname=eventname
            self.orgname=orgname
            self.orgweb=orgweb
            self.venue=venue
            self.startdate=startdate
            self.enddate=enddate
            self.starttime=starttime
            self.endtime=endtime
            self.logo=logo
            self.signature=signature
            self.cost=cost
            self.walletaddress=walletaddress
            self.ticketTemplate=ticketTemplate
            self.certificateTemplate=certificateTemplate
            self.bannerTemplate=bannerTemplate

    class Participants(db.Model):
        eventid = db.Column(db.Integer, nullable=False)
        eventname = db.Column(db.String, nullable=False)
        email = db.Column(db.String, unique=True, nullable=False, primary_key=True)
        name = db.Column(db.String, nullable=False)
        phone = db.Column(db.Integer, unique=True, nullable=False)
        address = db.Column(db.String, nullable=False)

    class Certificate(db.Model):
        eventid = db.Column(db.Integer, nullable=False)
        eventname = db.Column(db.String, nullable=False)
        email = db.Column(db.String, unique=True, nullable=False, primary_key=True)
        name = db.Column(db.String)
        phone = db.Column(db.Integer, unique=True, nullable=False)
        address = db.Column(db.String, nullable=False)

    with app.app_context():
        db.create_all()
        db.session.commit()

    ####---------------------------------Database(Model) ends------------------------------------------------------------------------------------------------------------------------------------------------------------#####

    ####----------------------------------Main Backend Operation File Starts----------------------------------------------------------------------------------------------------------------------------####

    @app.route("/eventdetails", methods=["GET", "POST"])
    def event_data():
        if request.method=="POST":
            eventname = request.json['eventname']
            orgname = request.json['orgname']
            orgweb = request.json['orgweb']
            venue = request.json['venue']
            startdate = request.json['startdate']
            enddate = request.json['enddate']
            starttime = request.json['starttime']
            endtime = request.json['endtime']
            logo = request.json['logo']
            signature = request.json['signature']
            cost = request.json['cost']
            walletaddress = request.json['walletaddress']
            ticketTemplate = request.json['ticketTemplate']
            certificateTemplate = request.json['certificateTemplate']
            bannerTemplate = request.json['bannerTemplate']
            organizer=EventDetails(eventname=eventname, orgname=orgname, orgweb=orgweb, venue=venue, startdate=startdate, enddate=enddate, starttime=starttime, endtime=endtime, logo=logo, signature=signature, cost=int(cost), walletaddress=walletaddress, ticketTemplate=ticketTemplate, certificateTemplate=certificateTemplate, bannerTemplate=bannerTemplate)
            with app.app_context():
                db.session.add(organizer)
                db.session.commit()
            if bannerTemplate=="1":
                banner1.make_banners1(orgname, eventname, venue, startdate, starttime)
            if bannerTemplate=="2":
                banner2.make_banners2(orgname, eventname, venue, startdate, starttime)
            if bannerTemplate=="3":
                banner3.make_banners3(orgname, eventname, venue, startdate, starttime)
            registration_mail()
            return jsonify({'eventid': id})
        return render_template('index.html')

    @app.route("/participantdetails", methods=["GET", "POST"])
    def participants():
        if request.method == 'POST':
            eventid = request.json['eventid']
            eventname = request.json['eventname']
            email = request.json['email']
            name = request.json['name']
            phone = request.json['phone']
            address = request.json['address']
            Q1=request.json['Q1']
            Q2 = request.json['Q2']
            Q3 = request.json['Q3']
            Q4 = request.json['Q4']
            Q5 = request.json['Q5']
            Q6 = request.json['Q6']
            Q7 = request.json['Q7']
            Q8 = request.json['Q8']
            Q9 = request.json['Q9']
            Q10 = request.json['Q10']
            with open('participantList.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([eventid, eventname, email, name, phone, address, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10])
            registration = Participants(eventid=int(eventid), eventname=eventname, email=email, name=name, phone=int(phone), address=address)
            with app.app_context():
                db.session.add(registration)
                db.session.commit()
            with app.app_context():
                r = db.engine.execute(f"select ticketTemplate, startdate, starttime, venue, orgname from event_details where id={eventid}")
                for i in r:
                    if i[0] == "1":
                        ticket1.make_tickets1(name, eventname, i[1], i[4], i[3], email, phone, i[2])
                    elif i[0] == "2":
                        ticket2.make_tickets2(name, eventname, i[1], i[4], i[3], email, phone, i[2])
                    elif i[0]=="3":
                        ticket3.make_tickets3(name, eventname, i[1], i[4], i[3], email, phone, i[2])
            return jsonify({'trigger': True})
        return render_template('index.html')


    @app.route("/checkout", methods=["GET", "POST"])
    def checkin():
        if request.method == 'POST':
            eventid = request.json['eventid']
            eventname = request.json['eventname']
            email = request.json['email']
            name = request.json['name']
            phone = request.json['phone']
            pronoun= request.json['pronoun']
            address = request.json['address']
            with open('FinalAttendee.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([eventid, eventname, email, name])
            certlist = Certificate(eventid=eventid, eventname=eventname, email=email, name=name, phone=phone, address=address)
            with app.app_context():
                db.session.add(certlist)
                db.session.commit()
            with app.app_context():
                r = db.engine.execute(f"select certificateTemplate,orgname,venue,startdate,logo,signature from event_details where id={eventid}")
                for i in r:
                    if i[0] == "1":
                        certificate1.make_certificates1(name, pronoun, eventname, "Organizer", i[1], i[5], i[4])
                    elif i[0] == "2":
                        certificate2.make_certificates2(name, eventname, i[3], i[2], "Organizer", i[1], i[5], i[4])
                    elif i[0]=="3":
                        certificate3.make_certificates3(name, eventname, i[3], i[1], "Organizer", i[1],  i[5], i[4])
        return render_template('index.html')


    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/apiforevents')
    def apiforevents():
        with app.app_context():
            eventid=[]
            date=[]
            eventname=[]
            venue=[]
            bannerurl=[]
            cost=[]
            final=[]
            r = db.engine.execute("select id, eventname, startdate, venue, cost from event_details")
            for i in r:
                eventid1 = i[0]
                eventname1 = i[1]
                date1 = i[2]
                venue1 = i[3]
                cost1 = i[4]
                bannerurl1 = "https://gdg.community.dev/gdg-kolkata/"
                jsons=({'event': eventid1, 'eventname': eventname1, 'date': date1, 'venue':venue1, 'cost': cost1, 'bannerurl': bannerurl1})
                final.append(jsons)
        return jsonify({'Events': final})


    # with app.app_context():
    #     user = db.session.execute(db.select(EventDetails).filter_by(id=1)).one()
    #     print(user)

    # with app.app_context():
    #     eventid=1
    #     r=db.engine.execute("select id, eventname, startdate, venue, cost from event_details")
    #     for i in r:
    #         print(i)
    ####-------------------------------------------Server Execution Code------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------####

    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=5009)




### eventId, Date (month, date) , event name, venue, small description, banner url, free or paid,  (can be veiwed by anyone unauthorized.)

### (after authorization) toke pathabo: wallet Address, name, email,  ami pabo: upper details aar user ta kon kon event e already registered