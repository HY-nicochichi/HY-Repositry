from flask import Flask, request, redirect, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
import os
import re

app = Flask(__name__, static_folder='./static')
app.config['SECRET_KEY'] = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)

database_URL = "postgresql://postgres:educa_pass@educa_db:5432/educa_db"

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def index():
    if current_user.is_authenticated == True:
        return redirect('/menu')
    else:
        return render_template('index.html')

@app.route('/new_user', methods=['GET','POST'])
def new_user():
    if current_user.is_authenticated == True:
        return redirect('/menu')
    else:
        if request.method == 'POST':
            educaID = request.form.get('educaID', type=str)
            password = generate_password_hash(request.form.get('password', type=str))
            username = request.form.get('username', type=str)
            connection = psycopg2.connect(database_URL)
            cursor = connection.cursor()
            cursor.execute(f"SELECT educaID FROM educa_accounts WHERE educaID = '{educaID}'")
            result = cursor.fetchone()
            if result != None:
                connection.commit()
                connection.close()
                return redirect('/new_user?state=IDerror')
            else:
                cursor.execute(f"INSERT INTO educa_accounts VALUES ('{educaID}','{password}','{username}')")
                connection.commit()
                connection.close()
                user = User(educaID)
                login_user(user, remember=True)
                return redirect('/menu')
        else:
            state = request.args.get('state', default='default', type=str)
            return render_template('new_user.html', state=state)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect('/menu')
    else:
        if request.method == 'POST':
            educaID = request.form.get('educaID', type=str)
            password = request.form.get('password', type=str)
            connection = psycopg2.connect(database_URL)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM educa_accounts WHERE educaID = '{educaID}'")
            result = cursor.fetchone()
            connection.commit()
            connection.close()
            if result == None:
                return redirect('/login?state=IDerror')
            else:
                if check_password_hash(result[1], password) == False:
                    return redirect('/login?state=PASSerror')
                else:
                    user = User(result[0])
                    login_user(user, remember=True)
                    return redirect('/menu')
        else:
            state = request.args.get('state', default='default', type=str)
            return render_template('login.html', state=state)

@app.route('/logout')
def logout():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        logout_user()
        return redirect('/')

@app.route('/menu')
def menu():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        return render_template('menu.html')

@app.route('/english_top')
def english_top():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        return render_template('english_top.html')

@app.route('/kobun_top')
def kobun_top():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        return render_template('kobun_top.html')
    
@app.route('/room_top')
def room_top():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        roomlist = []
        yourID = current_user.get_id()
        connection = psycopg2.connect(database_URL)
        cursor = connection.cursor()
        cursor.execute(f"SELECT roomID FROM room_members WHERE member = '{yourID}'")
        result1 = cursor.fetchall()
        for x in range(len(result1)):
            cursor.execute(f"SELECT roomID, roomname FROM educa_rooms WHERE roomID = '{result1[x][0]}'")
            result2 = cursor.fetchone()
            roomlist.append({'roomID':result2[0], 'roomname':result2[1]})
        connection.commit()
        connection.close()
        return render_template('room_top.html', roomlist=roomlist)

@app.route('/en_wordlist')
def en_wordlist():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        listNo = request.args.get('listNo', default=1, type=int)
        wordlist = []
        connection = psycopg2.connect(database_URL)
        cursor = connection.cursor()
        for x in range(5):
            searchNo = 5*(listNo-1)+x+1
            cursor.execute(f"SELECT * FROM en_words WHERE Num = {searchNo}")
            result = cursor.fetchone()
            wordlist.append({'No':result[0],'Word':result[1], 'Meaning':result[2]})
        connection.commit()
        connection.close()
        return render_template('en_wordlist.html', listNo=listNo, wordlist=wordlist)

@app.route('/kobun_wordlist')
def kobun_wordlist():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        listNo = request.args.get('listNo', default=1, type=int)
        wordlist = []
        connection = psycopg2.connect(database_URL)
        cursor = connection.cursor()
        for x in range(5):
            searchNo = 5*(listNo-1)+x+1
            cursor.execute(f"SELECT * FROM kobun_words WHERE Num = {searchNo}")
            result = cursor.fetchone()
            wordlist.append({'No':result[0],'Word':result[1], 'Meaning':result[2]})
        connection.commit()
        connection.close()
        return render_template('kobun_wordlist.html', listNo=listNo, wordlist=wordlist)

@app.route('/new_room', methods=['GET','POST'])
def new_room():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        if request.method == 'POST':
            roomID = request.form.get('roomID', type=str)
            roomPASS = generate_password_hash(request.form.get('roomPASS', type=str))
            roomname = request.form.get('roomname', type=str)
            yourID = current_user.get_id()
            connection = psycopg2.connect(database_URL)
            cursor = connection.cursor()
            cursor.execute(f"SELECT roomID FROM educa_rooms WHERE roomID = '{roomID}'")
            result = cursor.fetchone()
            if result != None:
                connection.commit()
                connection.close()
                return redirect('/new_room?state=IDerror')
            else:
                cursor.execute(f"""INSERT INTO educa_rooms VALUES 
                        ('{roomID}','{roomPASS}','{roomname}','{yourID}')""")
                cursor.execute(f"INSERT INTO room_members VALUES ('{roomID}','{yourID}')")
                cursor.execute(f"""CREATE TABLE IF NOT EXISTS room_{roomID}_tests (
                        testID varchar(255) NOT NULL,
                        testname varchar(255) NOT NULL,
                        testSubject varchar(255) NOT NULL,
                        listNo int NOT NULL,
                        startDay int NOT NULL,
                        startTime int NOT NULL,
                        endDay int NOT NULL,
                        endTime int NOT NULL,
                        testTerm varchar(255) NOT NULL,
                        PRIMARY KEY (testID)
                        )""")
                connection.commit()
                connection.close()
                return redirect(f'/room?ID={roomID}')
        else:
            state = request.args.get('state', default='default', type=str)
            return render_template('new_room.html', state=state)

@app.route('/join_room', methods=['GET','POST'])
def join_room():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        if request.method == 'POST':
            roomID = request.form.get('roomID', type=str)
            roomPASS = request.form.get('roomPASS', type=str)
            connection = psycopg2.connect(database_URL)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM educa_rooms WHERE roomID = '{roomID}'")
            result = cursor.fetchone()
            if result == None:
                connection.commit()
                connection.close()
                return redirect('/join_room?state=IDerror')
            else:
                if check_password_hash(result[1], roomPASS) == False:
                    connection.commit()
                    connection.close()
                    return redirect('/join_room?state=PASSerror')
                else:
                    yourID = current_user.get_id()
                    cursor.execute(f"""SELECT * FROM room_members 
                            WHERE roomID = '{roomID}' AND member = '{yourID}'""")
                    result = cursor.fetchone()
                    if result == None:
                        cursor.execute(f"INSERT INTO room_members VALUES ('{roomID}','{yourID}')")
                        cursor.execute(f"SELECT testID FROM room_{roomID}_tests")
                        result = cursor.fetchall()
                        for x in range(len(result)):
                            cursor.execute(f"""INSERT INTO test_{roomID}_{result[x][0]}_answers 
                                    VALUES ('{yourID}',-1)""")
                    connection.commit()
                    connection.close()
                    return redirect(f'/room?ID={roomID}')
        else:
            state = request.args.get('state', default='default', type=str)
            return render_template('join_room.html', state=state)

@app.route('/room')
def room():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        yourID = current_user.get_id()
        roomID = request.args.get('ID', type=str)
        connection = psycopg2.connect(database_URL)
        cursor = connection.cursor()
        cursor.execute(f"""SELECT roomID FROM room_members 
                WHERE roomID = '{roomID}' AND member = '{yourID}'""")
        result = cursor.fetchall()
        if result == None:
            connection.commit()
            connection.close()
            return redirect('/join_room')
        else:
            testlist = []
            cursor.execute(f"""SELECT educaID, username FROM educa_accounts 
                    WHERE educaID = (SELECT educaID FROM educa_rooms WHERE roomID = '{roomID}')""")
            result = cursor.fetchone()
            you = 'guest'
            if yourID == result[0]:
                you = 'host'
            roomDict = {'roomID':roomID, 'hostname':result[1], 'you':you}
            cursor.execute(f"""SELECT testID, testname, startDay, startTime, endDay, endTime, testTerm
                    FROM room_{roomID}_tests""")
            result = cursor.fetchall()
            for x in range(len(result)):
                cursor.execute(f"""SELECT QuizResult FROM test_{roomID}_{result[x][0]}_answers
                        WHERE member = '{yourID}'""")
                result1 = cursor.fetchone()
                testlist.append({'testID':result[x][0], 'title':result[x][1],
                        'startDay':result[x][2], 'startTime':result[x][3],
                        'endDay':result[x][4], 'endTime':result[x][5], 
                        'testTerm':result[x][6], 'quizresult':result1[0]})
            connection.commit()
            connection.close()
            return render_template('room.html', roomDict=roomDict, testlist=testlist)

@app.route('/new_test', methods=['GET','POST'])
def new_test():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        connection = psycopg2.connect(database_URL)
        cursor = connection.cursor()
        if request.method == 'POST':
            roomID = request.form.get('roomID', type=str)
            testID = request.form.get('testID', type=str)
            cursor.execute(f"SELECT testID FROM room_{roomID}_tests WHERE testID = '{testID}'")
            result = cursor.fetchone()
            if result != None:
                connection.commit()
                connection.close()
                return redirect(f'/new_test?roomID={roomID}&state=IDerror')
            else:
                testname = request.form.get('testname', type=str)
                subject = request.form.get('subject', type=str)
                listNo = request.form.get('listNo', type=int)
                starttime = request.form.get('starttime', type=str)
                endtime = request.form.get('endtime', type=str)
                testTerm = f'{starttime}～{endtime}'
                startDayArray = re.split('-', re.split('T', starttime)[0])
                startTimeArray = re.split(':', re.split('T', starttime)[1])
                endDayArray = re.split('-', re.split('T', endtime)[0])
                endTimeArray = re.split(':', re.split('T', endtime)[1])
                startDayStr = ''
                startTimeStr = ''
                endDayStr = ''
                endTimeStr = ''
                for x in range(2):
                    startDayStr += startDayArray[x]
                    startTimeStr += startTimeArray[x]
                    endDayStr += endDayArray[x]
                    endTimeStr += endTimeArray[x]
                startDayStr += startDayArray[2]
                endDayStr += endDayArray[2]
                startDay = int(startDayStr)
                startTime = int(startTimeStr)
                endDay = int(endDayStr)
                endTime = int(endTimeStr)
                cursor.execute(f"""INSERT INTO room_{roomID}_tests VALUES 
                        ('{testID}','{testname}','{subject}',{listNo},
                        {startDay},{startTime},{endDay},{endTime},'{testTerm}')""")
                cursor.execute(f"""create table if not exists test_{roomID}_{testID}_answers (
                        member varchar(255) NOT NULL,
                        QuizResult int NOT NULL
                        )""")
                cursor.execute(f"SELECT member FROM room_members WHERE roomID = '{roomID}'")
                result = cursor.fetchall()
                for x in range(len(result)):
                    cursor.execute(f"""INSERT INTO test_{roomID}_{testID}_answers 
                            VALUES ('{result[x][0]}',-1)""")
                connection.commit()
                connection.close()
                return redirect(f'/room?ID={roomID}')
        else:
            roomID = request.args.get('roomID', type=str)
            state = request.args.get('state', default='default', type=str)
            yourID = current_user.get_id()
            cursor.execute(f"SELECT educaID FROM educa_rooms WHERE roomID = '{roomID}'")
            result = cursor.fetchone()
            if result == None:
                connection.commit()
                connection.close()
                return redirect('/new_room')
            elif yourID != result[0]:
                connection.commit()
                connection.close()
                return redirect(f'/room?ID={roomID}')
            else:
                connection.commit()
                connection.close()
                return render_template('new_test.html', roomID=roomID, state=state)

@app.route('/test', methods=['GET','POST'])
def test():
    if current_user.is_authenticated == False:
        return redirect('/login')
    else:
        connection = psycopg2.connect(database_URL)
        cursor = connection.cursor()
        if request.method == 'POST':
            yourID = current_user.get_id()
            roomID = request.form.get('roomID', type=str)
            testID = request.form.get('testID', type=str)
            subject = request.form.get('subject', type=str)
            listNo = request.form.get('listNo', type=int)
            if subject == 'english':
                table = 'en_words'
            elif subject == 'kobun':
                table = 'kobun_words'
            QuizResult = 0
            testResultList = []
            for x in range(5):
                answer = request.form.get(f'answer{x}', type=str)
                searchNo = 5*(listNo-1)+x+1
                cursor.execute(f"SELECT Word FROM {table} WHERE Num = {searchNo}")
                result = cursor.fetchone()
                if answer == result[0]:
                    QuizResult += 1
                    testResultList.append({'yourAnswer':answer,'Result':'○','rightAnswer':result[0]})
                else:
                    testResultList.append({'yourAnswer':answer,'Result':'×','rightAnswer':result[0]})
            cursor.execute(f"""SELECT QuizResult FROM test_{roomID}_{testID}_answers 
                    WHERE member = '{yourID}'""")
            result = cursor.fetchone()
            if QuizResult > result[0]:
                cursor.execute(f"""UPDATE test_{roomID}_{testID}_answers 
                        SET QuizResult = {QuizResult} WHERE member = '{yourID}'""")
            connection.commit()
            connection.close()
            return render_template('test_result.html', roomID=roomID, 
                    QuizResult=QuizResult, testResultList=testResultList)
        else:
            roomID = request.args.get('roomID', type=str)
            testID = request.args.get('testID', type=str)
            yourID = current_user.get_id()
            cursor.execute(f"SELECT roomID FROM educa_rooms WHERE roomID = '{roomID}'")
            result = cursor.fetchone()
            if result == None:
                connection.commit()
                connection.close()
                return redirect('/new_room')
            else:
                cursor.execute(f"""SELECT roomID FROM room_members 
                        WHERE roomID = '{roomID}' AND member = '{yourID}'""")
                result = cursor.fetchone()
                if result == None:
                    connection.commit()
                    connection.close()
                    return redirect('/join_room')
                else:
                    cursor.execute(f"SELECT educaID FROM educa_rooms WHERE roomID = '{roomID}'")
                    result = cursor.fetchone()
                    you = 'guest'
                    if yourID == result[0]:
                        you = 'host'
                    quizlist = []
                    cursor.execute(f"SELECT * FROM room_{roomID}_tests WHERE testID = '{testID}'")
                    result = cursor.fetchone()
                    if result == None:
                        if you == 'guest':
                            return redirect(f'/room?ID={roomID}')
                        else:
                            return redirect(f'/new_test?roomID={roomID}')
                    else:
                        subject = result[2]
                        listNo = result[3]
                        if result[2] == 'english':
                            table = 'en_words'
                        elif result[2] == 'kobun':
                            table = 'kobun_words'
                        testDict = {'testID':result[0], 'testname':result[1],
                                'subject':subject, 'listNo':listNo,
                                'startDay':result[4], 'startTime':result[5],
                                'endDay':result[6], 'endTime':result[7], 
                                'testTerm':result[8], 'you':you, 'roomID':roomID}
                        for x in range(5):
                            searchNo = 5*(listNo-1)+x+1
                            cursor.execute(f"SELECT Meaning FROM {table} WHERE Num = {searchNo}")
                            result = cursor.fetchone()
                            quizlist.append(result[0])
                        resultlist = []
                        cursor.execute(f"""SELECT * FROM test_{roomID}_{testID}_answers 
                                WHERE member != '{yourID}'""")
                        result1 = cursor.fetchall()
                        for x in range(len(result1)):
                            cursor.execute(f"""SELECT username FROM educa_accounts 
                                    WHERE educaID = '{result1[x][0]}'""")
                            result2 = cursor.fetchone()
                            resultlist.append({'member':result2[0], 'quizresult':result1[x][1]})
                        connection.commit()
                        connection.close()
                        return render_template('test.html', testDict=testDict, 
                                quizlist=quizlist, resultlist=resultlist)       
