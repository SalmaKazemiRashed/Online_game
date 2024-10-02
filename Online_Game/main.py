#!/usr/bin/env python
from flask import Flask, render_template, request, url_for, redirect, jsonify
import sqlite3 as sql

app = Flask(__name__)

##############################################

import mysql.connector




##############################################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def home_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('index.html')
@app.route('/level1', methods=['GET', 'POST'])
def l1_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Level1.html')

@app.route('/level2', methods=['GET', 'POST'])
def l2_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Level2.html')
@app.route('/level3', methods=['GET', 'POST'])
def l3_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Level3.html')

@app.route('/level4', methods=['GET', 'POST'])
def l4_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Level4.html')
@app.route('/P1_help', methods=['GET', 'POST'])
def l1_help_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('P1_help.html')

@app.route('/P2_help', methods=['GET', 'POST'])
def l2_help_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('P2_help.html')
@app.route('/P3_help', methods=['GET', 'POST'])
def l3_help_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('P3_help.html')
@app.route('/P4_help', methods=['GET', 'POST'])
def l4_help_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('P4_help.html')

@app.route('/Cell_info', methods=['GET', 'POST'])
def cell_info_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Cell_info.html')

@app.route('/Us_info', methods=['GET', 'POST'])
def us_info_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Us_info.html')
@app.route('/Info', methods=['GET', 'POST'])
def info_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Info.html')
#@app.route('/Pr1', methods=['GET', 'POST'])
#def p1_func():
#    if request.method == 'POST':
#        return redirect(url_for('index'))
    # show the form, it wasn't submitted
#    return render_template('P1_start.html')
########################################################################################
##########################################################################################
##Thi
import os

IMAGE_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER


########This part would be for practcing


@app.route('/P1_start', methods=['GET', 'POST'])
def P1_game_func():
    if request.method == 'POST':
        if request.form["P1Button"]== 'Start':
            print("P111111 start")

            ###########
            try:
                with sql.connect("P1.sqlite") as con:
                    ID="Hello dear guest!"
                    print("sqllllllllllllllllllllllllllllllllllllll fine")
                    cur = con.cursor()
                    cur.execute("select * from annotate_table;")
                    rows = cur.fetchall()
                    #print("rowssssssssssssssssssssssssssss{}",rows)
                    P1_game_func.imgNo = 0
                    P1_game_func.fileName = rows[0][0]
                    con.commit()
                    P1_first_image_name = rows[0][0]
                    print(P1_first_image_name)
                    #first_image_name =  first_image.replace(',','');
                    P1_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P1_first_image_name )
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template('P1_game.html', ID = ID, image_src = P1_full_filename)
        elif  request.form["P1Button"]== 'Save':

            ur_label = request.form.getlist('labelButton') 
            try:
                with sql.connect("P1.sqlite") as con:
                    ID='Hello dear guest!'
                    cur = con.cursor()
                    cur.execute("select *from annotate_table;")
                    P1_game_func.label_rows = cur.fetchall()
                    
                    
           
                  
                    multiple_labels = P1_game_func.label_rows[P1_game_func.imgNo][1:]
                    right_label = multiple_labels[0].split(',') #labels from Sonja's annotations
                    diff_label = [i for i in right_label + ur_label if i not in right_label or i not in ur_label] #The difference 
        
                    true_label = [i for i in ur_label if i in right_label]# labels which are guessed truly
                    ID = "You were " + str(len(true_label)/len(ur_label)*100) +"% right. The true labels are: "+ ','.join(right_label)
                    
                    
                    con.commit()
                    #P1_game_func.imgNo = P1_game_func.imgNo + 1
                    P1_game_func.page = 'P1_game_next.html'

                    cur = con.cursor()
                    if P1_game_func.imgNo==30:
                        P1_game_func.page= 'P1_game_done.html'


                    con.commit()
                    P1_game_func.fileName = P1_game_func.label_rows[P1_game_func.imgNo][0]
                    P1_first_image_name = P1_game_func.fileName
                    #first_image_name =  first_image.replace(',','');
                    P1_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P1_first_image_name )


            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template(P1_game_func.page, ID = ID, image_src = P1_full_filename)
        elif  request.form["P1Button"]== 'Next':
            P1_game_func.imgNo = P1_game_func.imgNo + 1
            P1_game_func.page = 'P1_game.html'
            
            if P1_game_func.imgNo==30:
                P1_game_func.page= 'P1_game_done.html'
            P1_game_func.fileName = P1_game_func.label_rows[P1_game_func.imgNo][0]
            P1_first_image_name = P1_game_func.fileName
            P1_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P1_first_image_name )
            return render_template(P1_game_func.page, ID = 'You annotate '+ str(P1_game_func.imgNo) +' images. Great effort!', image_src = P1_full_filename)
 
            
        elif  request.form["P1Button"]== 'Exit':
            print("Good luckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(url_for('l1_func'))
        else:
            return redirect(url_for('P1_game_func'))
    # show the form, it wasn't submitted
    return render_template('P1_start.html')
###################################################################################
####This part is for Practicing of second level


@app.route('/P2_start', methods=['GET', 'POST'])
def P2_game_func():
    if request.method == 'POST':
        if request.form["P2Button"]== 'Start':
            print("P22222 start")

            ###########
            try:
                with sql.connect("P2.sqlite") as con:
                    ID="Hello dear guest!"
                    print("sqllllllllllllllllllllllllllllllllllllll fine")
                    cur = con.cursor()
                    cur.execute("select * from annotate_table;")
                    rows = cur.fetchall()
                    print("rowssssssssssssssssssssssssssss{}",rows)
                    P2_game_func.imgNo = 0
                    P2_game_func.fileName = rows[0][0]
                    con.commit()
                    P2_first_image_name = rows[0][0]
                    #print(P2_first_image_name)
                    #first_image_name =  first_image.replace(',','');
                    P2_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P2_first_image_name )
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template('P2_game.html', ID = ID, image_src = P2_full_filename)
        elif  request.form["P2Button"]== 'Save':

            ur_label = request.form.getlist('labelButton') 
            try:
                with sql.connect("P2.sqlite") as con:
                    ID='Hello dear guest!'
                    cur = con.cursor()
                    cur.execute("select *from annotate_table;")
                    P2_game_func.label_rows = cur.fetchall()
                    
                    multiple_labels = P2_game_func.label_rows[P2_game_func.imgNo][1:]
                    right_label = multiple_labels[0].split(',') #labels from Sonja's annotations
                    diff_label = [i for i in right_label + ur_label if i not in right_label or i not in ur_label] #The difference 
        
                    true_label = [i for i in ur_label if i in right_label]# labels which are guessed truly
                    ID = "You were " + str(len(true_label)/len(ur_label)*100) +"% right. The true labels are: "+ ','.join(right_label)
                    
                    
                    con.commit()
                    #P2_game_func.imgNo = P2_game_func.imgNo + 1
                    P2_game_func.page = 'P2_game_next.html'

                    cur = con.cursor()
                    if P2_game_func.imgNo==30:
                        P2_game_func.page= 'P2_game_done.html'


                    con.commit()
                    P2_game_func.fileName = P2_game_func.label_rows[P2_game_func.imgNo][0]
                    P2_first_image_name = P2_game_func.fileName
                    #first_image_name =  first_image.replace(',','');
                    P2_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P2_first_image_name )


            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template(P2_game_func.page, ID = ID, image_src = P2_full_filename)
        elif  request.form["P2Button"]== 'Next':
            P2_game_func.imgNo = P2_game_func.imgNo + 1
            P2_game_func.page = 'P2_game.html'
            
            if P2_game_func.imgNo==30:
                P2_game_func.page= 'P2_game_done.html'
            P2_game_func.fileName = P2_game_func.label_rows[P2_game_func.imgNo][0]
            P2_first_image_name = P2_game_func.fileName
            P2_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P2_first_image_name )
            return render_template(P2_game_func.page, ID = 'You annotate '+ str(P2_game_func.imgNo) +' images. Great effort!', image_src = P2_full_filename)
 
            
        elif  request.form["P2Button"]== 'Exit':
            print("Good luckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(url_for('l1_func'))
        else:
            return redirect(url_for('P2_game_func'))
    # show the form, it wasn't submitted
    return render_template('P2_start.html')
###################################################################################


@app.route('/P3_start', methods=['GET', 'POST'])
def P3_game_func():
    if request.method == 'POST':
        if request.form["P3Button"]== 'Start':
            print("P3333 start")

            ###########
            try:
                with sql.connect("P3.sqlite") as con:
                    ID="Hello dear guest!"
                    print("sqllllllllllllllllllllllllllllllllllllll fine")
                    cur = con.cursor()
                    cur.execute("select * from annotate_table;")
                    rows = cur.fetchall()
                    print("rowssssssssssssssssssssssssssss{}",rows)
                    P3_game_func.imgNo = 0
                    P3_game_func.fileName = rows[0][0]
                    con.commit()
                    P3_first_image_name = rows[0][0]
                    print(P3_first_image_name)
                    #first_image_name =  first_image.replace(',','');
                    P3_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P3_first_image_name )
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template('P3_game.html', ID = ID, image_src = P3_full_filename)
        elif  request.form["P3Button"]== 'Save':

            ur_label = request.form.getlist('labelButton') 
            try:
                with sql.connect("P3.sqlite") as con:
                    ID='Hello dear guest!'
                    cur = con.cursor()
                    cur.execute("select *from annotate_table;")
                    P3_game_func.label_rows = cur.fetchall()
                    
                    multiple_labels = P3_game_func.label_rows[P3_game_func.imgNo][1:]
                    right_label = multiple_labels[0].split(',')  #labels from Sonja's annotations
                    diff_label = [i for i in right_label + ur_label if i not in right_label or i not in ur_label] #The difference 
        
                    true_label = [i for i in ur_label if i in right_label]# labels which are guessed truly
                    ID = "You were " + str(len(true_label)/len(ur_label)*100) +"% right. The true labels are: "+ ','.join(right_label)
                    
                    
                    con.commit()
                    #P3_game_func.imgNo = P3_game_func.imgNo + 1
                    P3_game_func.page = 'P3_game_next.html'

                    cur = con.cursor()
                    if P3_game_func.imgNo==30:
                        P3_game_func.page= 'P3_game_done.html'


                    con.commit()
                    P3_game_func.fileName = P3_game_func.label_rows[P3_game_func.imgNo][0]
                    P3_first_image_name = P3_game_func.fileName
                    #first_image_name =  first_image.replace(',','');
                    P3_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P3_first_image_name )


            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template(P3_game_func.page, ID = ID, image_src = P3_full_filename)
        elif  request.form["P3Button"]== 'Next':
            P3_game_func.imgNo = P3_game_func.imgNo + 1
            P3_game_func.page = 'P3_game.html'
            
            if P3_game_func.imgNo==30:
                P3_game_func.page= 'P3_game_done.html'
            P3_game_func.fileName = P3_game_func.label_rows[P3_game_func.imgNo][0]
            P3_first_image_name = P3_game_func.fileName
            P3_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P3_first_image_name )
            return render_template(P3_game_func.page, ID = 'You annotate '+ str(P3_game_func.imgNo) +' images. Great effort!', image_src = P3_full_filename)
 
            
        elif  request.form["P3Button"]== 'Exit':
            print("Good luckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(url_for('l1_func'))
        else:
            return redirect(url_for('P3_game_func'))
    # show the form, it wasn't submitted
    return render_template('P3_start.html')

####################################################################################
## Practicing for level4

@app.route('/P4_start', methods=['GET', 'POST'])
def P4_game_func():
    if request.method == 'POST':
        if request.form["P4Button"]== 'Start':
            print("P444444 start")

            ###########
            try:
                with sql.connect("P4.sqlite") as con:
                    ID="Hello dear guest!"
                    print("sqllllllllllllllllllllllllllllllllllllll fine")
                    cur = con.cursor()
                    cur.execute("select * from annotate_table;")
                    rows = cur.fetchall()
                    print("rowssssssssssssssssssssssssssss{}",rows)
                    P4_game_func.imgNo = 0
                    P4_game_func.fileName = rows[0][0]
                    con.commit()
                    P4_first_image_name = rows[0][0]
                    print(P4_first_image_name)
                    #first_image_name =  first_image.replace(',','');
                    P4_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P4_first_image_name )
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template('P4_game.html', ID = ID, image_src = P4_full_filename)
        elif  request.form["P4Button"]== 'Save':

            ur_label = request.form.getlist('labelButton') 
            try:
                with sql.connect("P4.sqlite") as con:
                    ID='Hello dear guest!'
                    cur = con.cursor()
                    cur.execute("select *from annotate_table;")
                    P4_game_func.label_rows = cur.fetchall()
                    
                    multiple_labels = P4_game_func.label_rows[P4_game_func.imgNo][1:]
                    right_label = multiple_labels[0].split(',')  #labels from Sonja's annotations
                    diff_label = [i for i in right_label + ur_label if i not in right_label or i not in ur_label] #The difference 
        
                    true_label = [i for i in ur_label if i in right_label]# labels which are guessed truly
                    ID = "You were " + str(len(true_label)/len(ur_label)*100) +"% right. The true labels are: "+ ','.join(right_label)
                    
                    
                    con.commit()
                    #P4_game_func.imgNo = P4_game_func.imgNo + 1
                    P4_game_func.page = 'P4_game_next.html'

                    cur = con.cursor()
                    if P4_game_func.imgNo==30:
                        P4_game_func.page= 'P4_game_done.html'


                    con.commit()
                    P4_game_func.fileName = P4_game_func.label_rows[P4_game_func.imgNo][0]
                    P4_first_image_name = P4_game_func.fileName
                    #first_image_name =  first_image.replace(',','');
                    P4_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P4_first_image_name )


            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template(P4_game_func.page, ID = ID, image_src = P4_full_filename)
        elif  request.form["P4Button"]== 'Next':
            P4_game_func.imgNo = P4_game_func.imgNo + 1
            P4_game_func.page = 'P4_game.html'
            
            if P4_game_func.imgNo==30:
                P4_game_func.page= 'P4_game_done.html'
            P4_game_func.fileName = P4_game_func.label_rows[P4_game_func.imgNo][0]
            P4_first_image_name = P4_game_func.fileName
            P4_full_filename = os.path.join(app.config['UPLOAD_FOLDER'], P4_first_image_name )
            return render_template(P4_game_func.page, ID = 'You annotate '+ str(P4_game_func.imgNo) +' images. Great effort!', image_src = P4_full_filename)
 
            
        elif  request.form["P4Button"]== 'Exit':
            print("Good luckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(url_for('l1_func'))
        else:
            return redirect(url_for('P4_game_func'))
    # show the form, it wasn't submitted
    return render_template('P4_start.html')


####################################################################################

@app.route('/Help', methods=['GET', 'POST'])
def help_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Help.html')

@app.route('/Game', methods=['GET', 'POST'])
def game_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('Game.html')


@app.route('/help_second', methods=['GET', 'POST'])
def help_second_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('help_second.html')

################################
############################################################

import os
import csv

IMAGE_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

############################################################



@app.route('/Quality_game', methods=['GET', 'POST'])
def quality_game_func():
    if request.method == 'POST':
        if request.form.get('fname'):

            ###########
            try:
                with sql.connect("Quality.sqlite") as con:
                    quality_game_func.ID = request.form.get('fname')
                    quality_game_func.ctr = 0
                    cur = con.cursor()
                    cur.execute("select id from annotate_table where first_label='' limit 1;")
                    rows = cur.fetchall()
                    quality_game_func.labelNo = "first_label"

                    if len(rows)==0:
                        cur.execute("select id from annotate_table where second_label='' limit 1;")
                        rows = cur.fetchall()
                        quality_game_func.labelNo = "second_label"
                        print("hereeeeeee",quality_game_func.labelNo)
                        print(len(rows))
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where third_label='' limit 1;")
                        rows = cur.fetchall()
                        quality_game_func.labelNo = "third_label"
                        print("hereeeeeee",quality_game_func.labelNo)
                    if len(rows)==0:
                        quality_game_func.ID = "All images are labeled! Thank you for your cooperation!"
                        cur.execute("select id from annotate_table limit 1;")
                        rows = cur.fetchall()

                    print("after first ifs checkinggggggggggggggggggggggggg!")
                    quality_game_func.fileName = rows[0][0]



                    con.commit()

                    first_image_name = rows[0][0]
                    #first_image_name =  first_image.replace(',','');
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], first_image_name )
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template('Quality_game_main.html', ID = quality_game_func.ID+' annotated: ' + str(quality_game_func.ctr), image_src = full_filename)
        elif  request.form["qualityButton"]== 'Save':

            #print(','.join(request.form.getlist('labelButton')) + ','+ quality_game_func.ID)
            label = ','.join(request.form.getlist('labelButton')) + ','+ quality_game_func.ID
            quality_game_func.ctr = quality_game_func.ctr+1
            try:
                with sql.connect("Quality.sqlite") as con:
                    #ID=quality_game_func.ID
                    cur = con.cursor()
                    label_column = quality_game_func.labelNo
                    print("Labellllllllllllllllcolumn",label_column)
                    if label_column =="first_label":
                        cur.execute("update annotate_table set first_label=? where id = ?;",(label, quality_game_func.fileName))
                        con.commit()
                    elif label_column == "second_label":
                        cur.execute("update annotate_table set second_label=? where id = ?;",(label, quality_game_func.fileName))
                        con.commit()
                    elif label_column == "third_label":
                        cur.execute("update annotate_table set third_label=? where id = ?;",(label, quality_game_func.fileName))
                        con.commit()

                    msg = "Label successfully added"
                    print(msg)
                    cur = con.cursor()
                    cur.execute("select id from annotate_table where first_label='' limit 1;")
                    rows = cur.fetchall()
                    print("rowwwwwwwwwwwwwwwwwwwwwwwwwwww after Save",rows)
                    quality_game_func.labelNo = "first_label"
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where second_label='' limit 1;")
                        rows = cur.fetchall()
                        quality_game_func.labelNo = "second_label"
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where third_label='' limit 1;")
                        rows = cur.fetchall()
                        quality_game_func.labelNo = "third_label"
                    if len(rows)==0:
                        ID = "All images are labeled. Thank you for your cooperation!"
                        cur.execute("select id from annotate_table limit 1;")
                        rows = cur.fetchall()

                    quality_game_func.fileName = rows[0][0]

                    con.commit()

                    first_image_name = quality_game_func.fileName
                    #first_image_name =  first_image.replace(',','');
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], first_image_name )
                    print(first_image_name)
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                print('This isss importanttttttttttttttttttt:',request.form['labelButton'])
                con.close()
                return render_template('Quality_game_main.html', ID = quality_game_func.ID + ' annotated: ' + str(quality_game_func.ctr), image_src = full_filename)
        elif  request.form["qualityButton"]== 'Exit':
            print("Good luckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('quality_game_func'))
    # show the form, it wasn't submitted
    return render_template('Quality_game.html')


############################################################


@app.route('/Nuclei_game', methods=['GET', 'POST'])
def nuclei_game_func():
    if request.method == 'POST':
        if request.form.get('fname'):

            ###########
            try:
                with sql.connect("Nuclei.sqlite") as con:
                    nuclei_game_func.ID = request.form.get('fname')
                    nuclei_game_func.ctr = 0
                    cur = con.cursor()
                    cur.execute("select id from annotate_table where first_label='' limit 1;")
                    rows = cur.fetchall()
                    nuclei_game_func.labelNo = "first_label"

                    if len(rows)==0:
                        cur.execute("select id from annotate_table where second_label='' limit 1;")
                        rows = cur.fetchall()
                        nuclei_game_func.labelNo = "second_label"
                        print("hereeeeeee",nuclei_game_func.labelNo)
                        print(len(rows))
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where third_label='' limit 1;")
                        rows = cur.fetchall()
                        nuclei_game_func.labelNo = "third_label"
                        print("hereeeeeee",nuclei_game_func.labelNo)
                    if len(rows)==0:
                        nuclei_game_func.ID = "All images are labeled! Thank you for your cooperation!"
                        cur.execute("select id from annotate_table limit 1;")
                        rows = cur.fetchall()

                    print("after first ifs checkinggggggggggggggggggggggggg!")
                    nuclei_game_func.fileName = rows[0][0]



                    con.commit()

                    first_image_name = rows[0][0]
                    #first_image_name =  first_image.replace(',','');
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], first_image_name )
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template('Nuclei_game_main.html', ID = nuclei_game_func.ID + ' annotated: '+ str(nuclei_game_func.ctr ), image_src = full_filename)
        elif  request.form["nucleiButton"]== 'Save':

            label = ','.join(request.form.getlist('labelButton'))+','+ nuclei_game_func.ID
            nuclei_game_func.ctr = nuclei_game_func.ctr+1
            
            try:
                with sql.connect("Nuclei.sqlite") as con:
                    #ID=nuclei_game_func.ID
                    cur = con.cursor()
                    label_column = nuclei_game_func.labelNo
                    print("Labellllllllllllllllcolumn",label_column)
                    if label_column =="first_label":
                        cur.execute("update annotate_table set first_label=? where id = ?;",(label, nuclei_game_func.fileName))
                        con.commit()
                    elif label_column == "second_label":
                        cur.execute("update annotate_table set second_label=? where id = ?;",(label, nuclei_game_func.fileName))
                        con.commit()
                    elif label_column == "third_label":
                        cur.execute("update annotate_table set third_label=? where id = ?;",(label, nuclei_game_func.fileName))
                        con.commit()

                    msg = "Label successfully added"
                    print(msg)
                    cur = con.cursor()
                    cur.execute("select id from annotate_table where first_label='' limit 1;")
                    rows = cur.fetchall()
                    print("rowwwwwwwwwwwwwwwwwwwwwwwwwwww after Save",rows)
                    nuclei_game_func.labelNo = "first_label"
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where second_label='' limit 1;")
                        rows = cur.fetchall()
                        nuclei_game_func.labelNo = "second_label"
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where third_label='' limit 1;")
                        rows = cur.fetchall()
                        nuclei_game_func.labelNo = "third_label"
                    if len(rows)==0:
                        ID = "All images are labeled. Thank you for your cooperation!"
                        cur.execute("select id from annotate_table limit 1;")
                        rows = cur.fetchall()

                    nuclei_game_func.fileName = rows[0][0]

                    con.commit()

                    first_image_name = nuclei_game_func.fileName
                    #first_image_name =  first_image.replace(',','');
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], first_image_name )
                    print(first_image_name)
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                print('This isss importanttttttttttttttttttt:',request.form['labelButton'])
                con.close()
                return render_template('Nuclei_game_main.html', ID = nuclei_game_func.ID + ' annotated: '+ str(nuclei_game_func.ctr ), image_src = full_filename)
        elif  request.form["nucleiButton"]== 'Exit':
            print("Good luckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('nuclei_game_func'))
    # show the form, it wasn't submitted
    return render_template('Nuclei_game.html')
#####################################################
#######################################################################################



####################################################################


@app.route('/Cytosol_game', methods=['GET', 'POST'])
def cytosol_game_func():
    if request.method == 'POST':
        if request.form.get('fname'):

            ###########
            try:
                with sql.connect("Cytosol.sqlite") as con:
                    cytosol_game_func.ID = request.form.get('fname')
                    cytosol_game_func.ctr = 0
                    cur = con.cursor()
                    cur.execute("select id from annotate_table where first_label='' limit 1;")
                    rows = cur.fetchall()
                    cytosol_game_func.labelNo = "first_label"

                    if len(rows)==0:
                        cur.execute("select id from annotate_table where second_label='' limit 1;")
                        rows = cur.fetchall()
                        cytosol_game_func.labelNo = "second_label"
                        print("hereeeeeee",cytosol_game_func.labelNo)
                        print(len(rows))
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where third_label='' limit 1;")
                        rows = cur.fetchall()
                        cytosol_game_func.labelNo = "third_label"
                        print("hereeeeeee",cytosol_game_func.labelNo)
                    if len(rows)==0:
                        cytosol_game_func.ID = "All images are labeled! Thank you for your cooperation!"
                        cur.execute("select id from annotate_table limit 1;")
                        rows = cur.fetchall()

                    print("after first ifs checkinggggggggggggggggggggggggg!")
                    cytosol_game_func.fileName = rows[0][0]



                    con.commit()

                    first_image_name = rows[0][0]
                    #first_image_name =  first_image.replace(',','');
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], first_image_name )
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template('Cytosol_game_main.html', ID = cytosol_game_func.ID+ ' annotated: '+ str(cytosol_game_func.ctr), image_src = full_filename)
        elif  request.form["cytosolButton"]== 'Save':

            label = ','.join(request.form.getlist('labelButton'))+','+ cytosol_game_func.ID
            cytosol_game_func.ctr += 1
            try:
                with sql.connect("Cytosol.sqlite") as con:
                    cur = con.cursor()
                    label_column = cytosol_game_func.labelNo
                    print("Labellllllllllllllllcolumn",label_column)
                    if label_column =="first_label":
                        cur.execute("update annotate_table set first_label=? where id = ?;",(label, cytosol_game_func.fileName))
                        con.commit()
                    elif label_column == "second_label":
                        cur.execute("update annotate_table set second_label=? where id = ?;",(label, cytosol_game_func.fileName))
                        con.commit()
                    elif label_column == "third_label":
                        cur.execute("update annotate_table set third_label=? where id = ?;",(label, cytosol_game_func.fileName))
                        con.commit()

                    msg = "Label successfully added"
                    print(msg)
                    cur = con.cursor()
                    cur.execute("select id from annotate_table where first_label='' limit 1;")
                    rows = cur.fetchall()
                    print("rowwwwwwwwwwwwwwwwwwwwwwwwwwww after Save",rows)
                    cytosol_game_func.labelNo = "first_label"
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where second_label='' limit 1;")
                        rows = cur.fetchall()
                        cytosol_game_func.labelNo = "second_label"
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where third_label='' limit 1;")
                        rows = cur.fetchall()
                        cytosol_game_func.labelNo = "third_label"
                    if len(rows)==0:
                        cytosol_game_func.ID = "All images are labeled! Thank you for your cooperation!"
                        cur.execute("select id from annotate_table limit 1;")
                        rows = cur.fetchall()

                    cytosol_game_func.fileName = rows[0][0]

                    con.commit()

                    first_image_name = cytosol_game_func.fileName
                    #first_image_name =  first_image.replace(',','');
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], first_image_name )
                    print(first_image_name)
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                print('This isss importanttttttttttttttttttt:',request.form['labelButton'])
                con.close()
                return render_template('Cytosol_game_main.html', ID = cytosol_game_func.ID+' annotated: '+ str(cytosol_game_func.ctr), image_src = full_filename)
        elif  request.form["cytosolButton"]== 'Exit':
            print("Good luckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('cytosol_game_func'))
    # show the form, it wasn't submitted
    return render_template('Cytosol_game.html')


    ######################################Mitochondria#########################################################


@app.route('/Mitochondria_game', methods=['GET', 'POST'])
def mitochondria_game_func():
    if request.method == 'POST':
        if request.form.get('fname'):
            ###########
            try:
                with sql.connect("Mitochondria.sqlite") as con:
                    mitochondria_game_func.ID=request.form.get('fname')
                    mitochondria_game_func.ctr = 0
                    cur = con.cursor()
                    cur.execute("select id from annotate_table where first_label='' limit 1;")
                    rows = cur.fetchall()
                    mitochondria_game_func.labelNo = "first_label"

                    if len(rows)==0:
                        cur.execute("select id from annotate_table where second_label='' limit 1;")
                        rows = cur.fetchall()
                        mitochondria_game_func.labelNo = "second_label"
                        print("hereeeeeee",mitochondria_game_func.labelNo)
                        print(len(rows))
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where third_label='' limit 1;")
                        rows = cur.fetchall()
                        mitochondria_game_func.labelNo = "third_label"
                        print("hereeeeeee",mitochondria_game_func.labelNo)
                    if len(rows)==0:
                        mitochondria_game_func.ID = "All images are labeled! Thank you for your cooperation!"
                        cur.execute("select id from annotate_table limit 1;")
                        rows = cur.fetchall()

                    print("after first ifs checkinggggggggggggggggggggggggg!")
                    mitochondria_game_func.fileName = rows[0][0]

                    con.commit()

                    first_image_name = rows[0][0]
                    #first_image_name =  first_image.replace(',','');
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], first_image_name )
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                con.close()
                return render_template('Mitochondria_game_main.html', ID = mitochondria_game_func.ID +' annotated: '+ str(mitochondria_game_func.ctr), image_src = full_filename)
        elif  request.form["mitochondriaButton"]== 'Save':
            
            label = ','.join(request.form.getlist('labelButton'))+','+mitochondria_game_func.ID
            mitochondria_game_func.ctr= mitochondria_game_func.ctr+1
            try:
                with sql.connect("Mitochondria.sqlite") as con:
                    cur = con.cursor()
                    label_column = mitochondria_game_func.labelNo
                    if label_column =="first_label":
                        cur.execute("update annotate_table set first_label=? where id = ?;",(label, mitochondria_game_func.fileName))
                        con.commit()
                    elif label_column == "second_label":
                        cur.execute("update annotate_table set second_label=? where id = ?;",(label, mitochondria_game_func.fileName))
                        con.commit()
                    elif label_column == "third_label":
                        cur.execute("update annotate_table set third_label=? where id = ?;",(label, mitochondria_game_func.fileName))
                        con.commit()

                    msg = "Label successfully added"
                    print(msg)
                    cur = con.cursor()
                    cur.execute("select id from annotate_table where first_label='' limit 1;")
                    rows = cur.fetchall()
                    print("rowwwwwwwwwwwwwwwwwwwwwwwwwwww after Save",rows)
                    mitochondria_game_func.labelNo = "first_label"
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where second_label='' limit 1;")
                        rows = cur.fetchall()
                        mitochondria_game_func.labelNo = "second_label"
                    if len(rows)==0:
                        cur.execute("select id from annotate_table where third_label='' limit 1;")
                        rows = cur.fetchall()
                        mitochondria_game_func.labelNo = "third_label"
                    if len(rows)==0:
                        ID = "All images are labeled! Thank you for your cooperation!"
                        cur.execute("select id from annotate_table limit 1;")
                        rows = cur.fetchall()

                    mitochondria_game_func.fileName = rows[0][0]

                    con.commit()

                    first_image_name = mitochondria_game_func.fileName
                    #first_image_name =  first_image.replace(',','');
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], first_image_name )
                    print(first_image_name)
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)

            #####
            finally:
                print('This isss importanttttttttttttttttttt:',request.form['labelButton'])
                con.close()
                return render_template('Mitochondria_game_main.html', ID = mitochondria_game_func.ID+' annotated: '+ str(mitochondria_game_func.ctr), image_src = full_filename)
        elif  request.form["mitochondriaButton"]== 'Exit':
            print("Good luckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('mitochondria_game_func'))
    # show the form, it wasn't submitted
    return render_template('Mitochondria_game.html')


#####################################################################

# Route for handling the login page logic

######################################################################



if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)
