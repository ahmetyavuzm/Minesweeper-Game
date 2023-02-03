import PySimpleGUI as sg
from random import randint
import threading
import time
import pandas as pd
import numpy as np
import sys
import os

# for converting .app file

flag = os.path.join(sys._MEIPASS, "icons/flag4.png")
default = os.path.join(sys._MEIPASS, "icons/default.png")
mine = os.path.join(sys._MEIPASS, "icons/darkbomb.png")
clickedButton = os.path.join(sys._MEIPASS, "icons/clickedButton.png")
mainBomb = os.path.join(sys._MEIPASS, "icons/mainBomb.png")
mainDizzy = os.path.join(sys._MEIPASS, "icons/mainDizzy.png")
mainSmile = os.path.join(sys._MEIPASS, "icons/mainSmile.png")
mainFearful = os.path.join(sys._MEIPASS, "icons/mainFearful.png" )

# for run .py file

"""flag = "icons/flag4.png"
default = "icons/default.png"
mine = "icons/darkbomb.png"
clickedButton = "icons/clickedButton.png"
mainBomb = "icons/mainBomb.png"
mainDizzy = "icons/mainDizzy.png"
mainSmile = "icons/mainSmile.png"
mainFearful = "icons/mainFearful.png"""

class windows():
    def ms_window(layout_name):
        def new_game_layout_func():
            dificulityButton= {"expand_x": True, "button_color" : ("black","#C0C0C0"), "size" : (10,1) , "font": ("",15)}

            newGameLayout = [
                [sg.Text("MINESWEEPER",pad=(10,10), font = ("Mario Kart DS", 30 ), expand_x= True, justification= "center", background_color="white", text_color="Black")],
                [sg.Image(filename= mainBomb, subsample=0, background_color= "white", expand_x= True, key="-GIF-")],
                #[sg.Text("Select Game Dificulity", pad=(10,10), font= ("",15), background_color="white", expand_x= True, text_color= "black", justification="center")],
                [
                    sg.Button("Easy",**dificulityButton, key= "-EASY-",enable_events= True),
                    sg.Button("Normal",**dificulityButton, key = "-NORMAL-",enable_events= True),
                    sg.Button("Hard",**dificulityButton, key ="-HARD-", enable_events= True),
                ],
                [sg.Button("Custom Game",**dificulityButton, key= "-CUSTOM_GAME-",enable_events= True)],
                [sg.Text("Made by Ahmet Yavuz MUTLU", pad=(10,10), font= ("",10), background_color="white", expand_x= True, text_color= "black", justification="center")]

            ]

            mainLayout = [
                [sg.Column(newGameLayout, key="-NEW_GAME_PAGE-", background_color="white"),]
                ]
            return mainLayout
            
        def game_layout_func():
            global Game_Buttons
            controlColumnLayout = [
                [
                    sg.Button(image_filename=flag,image_subsample=4, size=(1,1), button_color="#C0C0C0", key = "-FLAG-"), 
                    sg.Button("new game", button_color=("black","#C0C0C0"), expand_y = True, font=("Mario Kart DS", 15 ), key ="-NEW_GAME_BUTTON-")
                    ],
            ]
            headerLayout = [
                [
                    sg.Image(filename=flag, subsample = 3, background_color= "white"),
                    sg.Text(text =current_mine_num, key="-FLAG_COUNTER-", background_color= "white",font= ("digital-7",25),text_color="black" ),
                ]
            ]

            gameLayout = [
                [
                    sg.Text(text = "", background_color="white", font= ("digital-7",25), text_color="black", expand_x=True, justification="left", key="-DIFICULITY_TXT-"),
                    sg.Column(headerLayout,expand_x=True, background_color="white"),
                    sg.Text(text = "00:00", background_color="white", font= ("digital-7",25), text_color="black", expand_x=False, justification="right", key="-CLOCK-", size=(8,1))
                ],
                [
                    sg.Column(Game_Buttons, background_color="white", key=f"{dificulity[:-1]}_BUTTONS"), 
                    #sg.Column(GameButtons, background_color="white", key="-NORMAL_BUTTONS-", visible= False), 
                    #sg.Column(GameButtons, background_color="white", key="-HARD_BUTTONS-", visible= False),
                ],
                [sg.Column(controlColumnLayout, background_color="white", element_justification="right", expand_x=True)]
            ]
            mainLayout = [
                [sg.Column(gameLayout, key="-MINESWEEPER_PAGE-", background_color="white"),]
                ]
            return mainLayout
        if layout_name == "DIFICULITY":
            mainLayout = new_game_layout_func()
        elif layout_name == "GAME":
            mainLayout = game_layout_func()

        return sg.Window("Minesweeper", mainLayout, element_padding = 1,background_color="white", finalize= True, element_justification="right")

    def game_ending():
        ending_layout = [
            [sg.Text('',background_color="white",font= ("Mario Kart DS",25),pad = 20 , text_color = "Black", expand_x = True,justification= "center", key ="-GAME_END_TEXT-")], 
            [
                sg.Button("Show Board",s=10, button_color = ("#E0E0E0","black") ,font= ("",15), key= "-SHOW_BOARD-"), 
                sg.Button("New Game",s=10, button_color = ("#E0E0E0","black") ,font= ("",15), key = "-NEW_GAME_BUTTON-", enable_events=True),
                sg.Button("Quit",s=10, button_color = ("#E0E0E0","black") ,font= ("",15), key = "-QUIT-")
            ],
        ]

        return sg.Window(layout=ending_layout, title = "", disable_close=True, background_color="white", finalize=True)

    def custom_game():
        custom_layout = [
            [
                sg.Text("Width : ", font=("", 25), size=(10,1), background_color= "white", text_color="black"),
                sg.Input(size = (4,1), expand_y= True,font=("", 25), justification="center", key="-GRID_WIDTH-")
                ],
            [
                sg.Text("Height: ", font=("", 25), size=(10,1), background_color= "white", text_color="black"),
                sg.Input(size = (4,1), expand_y= True, font=("", 25), justification="center", key="-GRID_HEIGHT-")
                ],
            [
                sg.Text("Mine Number : ", font=("", 25), size=(10,1), background_color= "white", text_color="black"),
                sg.Input(size = (4,1), expand_y= True,font=("", 25), justification="center",key = "-MINE_NUM-")
                ],
            [sg.Button("PLAY", expand_x=True, font=("Mario Kart Ds", 30), button_color=("black","white"), key="-CUSTOM_PLAY-")]
        ]

        return sg.Window("Custom Game", layout= custom_layout, background_color="white", element_justification="left")
class functions():

    def createGrid(grid_size, mineNum, dificulity):
        Buttons = []
        ButtonsStatus = dict()
        (rowNum, columnNum)= grid_size
        for row in range(1,rowNum+1):
            oneButtonRow = []
            for column in range(1, columnNum+1):
                oneButtonRow.append(sg.Button(image_filename = default,image_subsample=4, size=(1,0) , border_width=10, button_color=("green","#C0C0C0"), mouseover_colors=("red","white") ,key =f"{row}-{column}"))
                ButtonsStatus[f"{row}-{column}"] = {"activate":False, "type" : "empty", "neighbourMineNum" : 0, "flagStatus": False}
            Buttons.append(oneButtonRow)

        def distributeMines(mineNum):
            nonlocal ButtonsStatus, rowNum, columnNum

            def updateNeighbourButtons(row, column):
                ButtonsStatus[f"{row}-{column}"]["neighbourMineNum"] += 1 

            mineSet = set()
            for counter in range(mineNum):
                def minePosition():
                    nonlocal mineSet
                    row = randint(1,rowNum)
                    column = randint(1,columnNum)
                    position = f"{row}-{column}"
                    #print(position)
                    if position in mineSet:
                        return minePosition()
                    else:
                        mineSet.add(position)
                        return position 
                                
                position = minePosition()
                ButtonsStatus[position]["type"] = "mine"
                functions.lookUpNeighbours(position, updateNeighbourButtons)
            return mineSet
        mineSet = distributeMines(mineNum)
        return Buttons, ButtonsStatus, mineSet

    def lookUpNeighbours(position, operationFunc):
        global ButtonsStatus
        row , column = int(position.split("-")[0]), int(position.split("-")[1])
        neighbourRows = [row-1, row, row+1]
        neighbourColumns = [column-1, column, column+1]
        for rowCounter in neighbourRows:
            for columnCounter in neighbourColumns:
                try:
                    operationFunc(rowCounter, columnCounter)
                except KeyError:
                    pass
    
    def flagFunc():
        global putFlag
        if putFlag == True:
            putFlag = False
            window["-FLAG-"].update(button_color= "#C0C0C0")
        else:
            putFlag = True
            window["-FLAG-"].update(button_color= "red")
    
    def allGameFunc():
        global ButtonsStatus, mineSet , putFlag, event, dificulity, current_flag_num, current_mine_num
        position = event
        if putFlag == True:
            if ButtonsStatus[position]["flagStatus"] == False and current_flag_num != current_mine_num:
                ButtonsStatus[position]["flagStatus"] = True
                window[position].update(image_filename = flag, image_subsample = 4)
                
                current_flag_num += 1
                window["-FLAG_COUNTER-"].update(current_mine_num-current_flag_num)

            elif ButtonsStatus[position]["flagStatus"] == True:
                ButtonsStatus[position]["flagStatus"] = False
                window[position].update(image_filename = default,image_subsample=4)
                
                current_flag_num -= 1
                window["-FLAG_COUNTER-"].update(current_mine_num-current_flag_num)
        else:
            if ButtonsStatus[position]["type"] == "mine":
                ButtonsStatus[position]["activate"] = True
                functions.lose_func()
    
            elif ButtonsStatus[position]["neighbourMineNum"] != 0:
                window[position].update(text = ButtonsStatus[position]["neighbourMineNum"], image_filename = clickedButton, image_subsample = 4,button_color="#E0E0E0",disabled = True)
                ButtonsStatus[position]["activate"] = True
            else:
                window[position].update(disabled = True , button_color="#E0E0E0")
                def clickButton(row , column):
                    newPosition = f"{row}-{column}"
                    if ButtonsStatus[newPosition]["activate"] == False:
                        ButtonsStatus[newPosition]["activate"] = True
                        if ButtonsStatus[newPosition]["neighbourMineNum"] != 0:
                            window[newPosition].update(text = ButtonsStatus[newPosition]["neighbourMineNum"],image_filename = clickedButton, image_subsample = 4 ,disabled = True, button_color="#E0E0E0")
                        elif ButtonsStatus[newPosition]["neighbourMineNum"] == 0:
                            window[newPosition].update(image_filename = clickedButton,disabled = True , button_color="#E0E0E0", image_subsample = 4)
                            functions.lookUpNeighbours(newPosition, clickButton)
                    else:
                        pass
                #functions.lookUpNeighbours(position, clickButton)   
                row , column = int(position.split("-")[0]), int(position.split("-")[1])
                clickButton(row, column)  

    def new_game_button_func():
        global putFlag, window ,timer, game_exist
        game_exist = False
        window.close()
        putFlag = False
        timer.cancel()
        window = windows.ms_window("DIFICULITY")
        functions.mouseover_animations()
        

    def timer_func(elapsed_seconds = 0):
        global timer
        def clock_updater():
            nonlocal elapsed_seconds
            elapsed_seconds= elapsed_seconds + 1
            local_time = time.localtime(elapsed_seconds)
            current_clock = time.strftime("%M:%S",local_time)
            window["-CLOCK-"].update(current_clock)
            functions.timer_func(elapsed_seconds)
        timer = threading.Timer(1.0 , clock_updater)
        timer.start()

    def check_winner(buttons_status):
        global dificulity
        bs_df = pd.DataFrame(buttons_status)
        
        def win_func():
            global timer
            timer.cancel()
            functions.disable_board()
            win_window = windows.game_ending()
            win_window["-GAME_END_TEXT-"].update("YOU WIN")
            new_event, new_values = win_window.read(close= True)

            if new_event == sg.WIN_CLOSED:
                win_window.close()
            elif new_event == "-NEW_GAME_BUTTON-":
                functions.new_game_button_func()
            elif new_event == "-QUIT-":
                functions.quit_func()
            elif new_event == "-SHOW_BOARD-":
                pass                

        activate_bincount = np.bincount(bs_df.loc["activate"][:])
        non_activated_button_num = activate_bincount[0]
        #print(activate_bincount)
        if non_activated_button_num == current_mine_num:
            win_func()

    def admin_mode():
        for position in ButtonsStatus:
            if position in mineSet:
                window[position].update(image_filename = mine,image_subsample=2, button_color=("green","#C0C0C0"), disabled = False)
    def lose_func():
        global timer
        for minePosition in mineSet:
            window[minePosition].update(image_filename = mine, button_color = "red", disabled = True , image_subsample = 2)
        functions.disable_board()
        timer.cancel()

        lose_window = windows.game_ending()
        lose_window["-GAME_END_TEXT-"].update("GAME OVER")
        new_event, new_values = lose_window.read(close= True)

        if new_event == sg.WIN_CLOSED:
            lose_window.close()
        elif new_event == "-NEW_GAME_BUTTON-":
            functions.new_game_button_func()
        elif new_event == "-QUIT-":
            functions.quit_func()
        elif new_event == "-SHOW_BOARD-":
            pass                

    def pause_func():
        sg.Window('Pause', 
            [[sg.Text('Game Paused',background_color="white",font= ("",15), text_color = "Black", expand_x = True,justification= "center")], 
            [sg.Button("Continue",s=10, button_color = ("#E0E0E0","black") ,font= ("",15), key= "-CONTINUE_GAME-"), 
            sg.Button("Quit",s=10, button_color = ("#E0E0E0","black") ,font= ("",15), key = "-QUIT-")]], 
            disable_close=True, background_color="white").read(close=True)
    def quit_func():
        global timer, window
        timer.cancel()
        window.close()
    
    def disable_board():
        global ButtonsStatus
        for position_ct in ButtonsStatus:
            window[position_ct].update(disabled = True)

    def mouseover_animations():
        global window
        window["-EASY-"].bind("<Enter>", "MOUSEOVER")
        window["-NORMAL-"].bind("<Enter>", "MOUSEOVER")
        window["-HARD-"].bind("<Enter>", "MOUSEOVER")
        window["-CUSTOM_GAME-"].bind("<Enter>", "MOUSEOVER")        


window = windows.ms_window("DIFICULITY")
timer= None
putFlag = False
game_exist = False

functions.mouseover_animations()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        if timer != None: 
            timer.cancel()
        break
    
    if "MOUSEOVER" in event:
        mouseover_dict = {
            "-EASY-MOUSEOVER": mainSmile,
            "-NORMAL-MOUSEOVER": mainFearful,
            "-HARD-MOUSEOVER": mainDizzy,
            "-CUSTOM_GAME-MOUSEOVER": mainBomb,
            
            }
        window["-GIF-"].update(filename = mouseover_dict[event])

    #SELECT DİFİCULİTY PART
    if event in ("-EASY-","-NORMAL-", "-HARD-", "-CUSTOM_GAME-"):
        mine_num_dict = {"-EASY-": 10,"-NORMAL-": 25, "-HARD-":50}
        grid_size = {"-EASY-": (10,10),"-NORMAL-": (15,15), "-HARD-":(20,20)}
        dificulity = event
        if event == "-CUSTOM_GAME-":
            def custom_game():
                global game_mode_text, window
                window.close()
                window = windows.custom_game()
                game_mode_text = "CUSTOM GAME"
                custom_event, custom_values = window.read()
                if custom_event == "-CUSTOM_PLAY-":
                    try:
                        current_mine_num = int(custom_values["-MINE_NUM-"])
                        grid_height = int(custom_values["-GRID_HEIGHT-"])
                        grid_width = int(custom_values["-GRID_WIDTH-"])
                        current_grid_size = (grid_height, grid_width)
                        current_flag_num = 0
                        if 26>grid_width >1 and 26>grid_height >1 and current_mine_num >0  and grid_height *grid_width > current_mine_num >= 0.1 * grid_height * grid_width:
                            return current_grid_size, current_mine_num, current_flag_num
                        else:
                            sg.popup("Width and Height must be greater than 1 and less than 26. \n Mine Number must be greater than 0.\nMine Number must be minimum %10 of Grid Size", background_color="white", text_color="black", font=("",15), button_color=("black","#C0C0C0"))
                            return custom_game()
                    except:
                        sg.popup("Please, fill the blanks", background_color="white", text_color="black", font=("",15), button_color=("black","#C0C0C0"))
                        return custom_game()
            current_grid_size, current_mine_num, current_flag_num = custom_game()
        else:
            game_mode_text = f"{dificulity[1:-1]} MODE"
            current_mine_num = mine_num_dict[dificulity]
            current_grid_size = grid_size[dificulity]
            current_flag_num = 0

        Game_Buttons, ButtonsStatus, mineSet = functions.createGrid(current_grid_size,current_mine_num,dificulity)
        
        window.close()
        window = windows.ms_window("GAME")
        #functions.admin_mode()
        functions.timer_func()
        window["-DIFICULITY_TXT-"].update(game_mode_text)

        game_exist = True

    # GAME PART
    if game_exist:
        if event == "-NEW_GAME_BUTTON-":
            functions.new_game_button_func()

        if event == "-FLAG-":
            functions.flagFunc()

        if event in ButtonsStatus:
            
            functions.allGameFunc()
            #print(ButtonsStatus[event]["activate"])
            #print(ButtonsStatus[event]["neighbourMineNum"])
            functions.check_winner(ButtonsStatus)

