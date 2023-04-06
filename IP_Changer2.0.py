# 요구사항에 맞춘 최종버전 2023-04-06

from tkinter import *
from tkinter import messagebox
import os
import socket

font=('Consolas', 10)
bold=('Consolas', 13, 'bold')
btn=('Consolas', 11, 'bold')
# # 자동설정
# def setting_auto():
#     if messagebox.askyesno('확인', '입력된 IP가 제거됩니다.\n\n변경 하시겠습니까?'):
#         print('netsh interface ip set address "이더넷" dhcp')
#         print('netsh interface ip set dns name="이더넷" dhcp')
#         os.system('netsh interface ip set address "이더넷" dhcp')
#         os.system('netsh interface ip set dns name="이더넷" dhcp')
#     else:
#         pass

# 수동설정 1
def setting_1():
    
    # 특수문자 입력 방지 =================================
    def validate_input(value):
        if value.isdigit():
            print('특수문자가 아님')
            return True
        else:
            print('특수문자 입력시')
            # return False
            pass
    # =======================================================
    
    
    root = Toplevel()
    root.title('IP')
    root.geometry('250x150+700+300')
    
    frame = Frame(root)
    frame.pack()
    
    label = Label(frame, text="IP 입력", font=bold)
    label.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

    entry1 = Entry(frame, width=4, validate='key', validatecommand=(root.register(validate_input), '%S'), font=bold)
    entry1.grid(row=1, column=0, padx=5, pady=10)

    label1 = Label(frame, text='.', font=('', 15, 'bold'))
    label1.grid(row=1, column=1)
    
    entry2 = Entry(frame, width=4, validate='key', validatecommand=(root.register(validate_input), '%S'), font=bold)
    entry2.grid(row=1, column=2, padx=5, pady=10)

    label2 = Label(frame, text='.', font=('', 15, 'bold'))
    label2.grid(row=1, column=3)

    entry3 = Entry(frame, width=4, validate='key', validatecommand=(root.register(validate_input), '%S'), font=bold)
    entry3.grid(row=1, column=4, padx=5, pady=10)

    label3 = Label(frame, text='.', font=('', 15, 'bold'))
    label3.grid(row=1, column=5)

    entry4 = Entry(frame, width=4, font=bold)
    entry4.grid(row=1, column=6, padx=5, pady=10)


    # 입력필요인 부분은 환경에 맞게 변경하고 사용해야 합니다.
    def change_ethernet_setting(event=True):
        ip_address = entry1.get()+'.'+entry2.get()+'.'+entry3.get()+'.'+entry4.get()
        subnetmask = '255.255.255.0'
        gateway = entry1.get()+'.'+entry2.get()+'.'+entry3.get()+'.'+'254'
        dns1 = '별도입력'
        dns2 = '별도입력'
        print('netsh interface ip set address "이더넷" static '+ip_address+' '+subnetmask+' '+gateway)
        print('netsh -c int ip set dns name="이더넷" static "'+dns1+'" primary')
        print('netsh -c int ip add dns name="이더넷" "'+dns2+'" index=2')
        
        os.system('netsh interface ip set address "이더넷" static '+ip_address+' '+subnetmask+' '+gateway)
        os.system('netsh -c int ip set dns name="이더넷" static "'+dns1+'" primary')
        os.system('netsh -c int ip add dns name="이더넷" "'+dns2+'" index=2')
        
        messagebox.showinfo('완료', '변경완료')
        root.destroy()
        
    def end_setting(event=True):
        root.destroy()
        
    change_btn = Button(frame, text='적용', width=15, command=change_ethernet_setting, relief='groove', font=btn)
    change_btn.grid(columnspan=7, padx=10, pady=10)
    
    
    # Entry1에 시작 focus
    entry1.focus()
    # . 을 눌러 다음 Entry로
    entry1.bind("<period>", lambda event: entry2.focus_set())
    entry2.bind("<period>", lambda event: entry3.focus_set())
    entry3.bind("<period>", lambda event: entry4.focus_set())
    # 엔터로 다음 Entry로
    entry1.bind("<Return>", lambda event: entry2.focus_set())
    entry2.bind("<Return>", lambda event: entry3.focus_set())
    entry3.bind("<Return>", lambda event: entry4.focus_set())
    # 엔터로 저장
    entry4.bind('<Return>', change_ethernet_setting)
    root.bind('<Escape>', end_setting)




# 수동설정 2
def setting_2():
    
    # 특수문자 입력 방지 =================================
    def validate_input(value):
        if value.isdigit():
            print('특수문자가 아님')
            return True
        else:
            print('특수문자 입력시')
            # return False
            pass
    # =======================================================
    
    
    root = Toplevel()
    root.title('IP')
    root.geometry('250x150+700+300')
    
    frame = Frame(root)
    frame.pack()
    
    label = Label(frame, text="IP 입력", font=bold)
    label.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

    entry1 = Entry(frame, width=4, validate='key', validatecommand=(root.register(validate_input), '%S'), font=bold)
    entry1.grid(row=1, column=0, padx=5, pady=10)

    label1 = Label(frame, text='.', font=('', 15, 'bold'))
    label1.grid(row=1, column=1)
    
    entry2 = Entry(frame, width=4, validate='key', validatecommand=(root.register(validate_input), '%S'), font=bold)
    entry2.grid(row=1, column=2, padx=5, pady=10)

    label2 = Label(frame, text='.', font=('', 15, 'bold'))
    label2.grid(row=1, column=3)

    entry3 = Entry(frame, width=4, validate='key', validatecommand=(root.register(validate_input), '%S'), font=bold)
    entry3.grid(row=1, column=4, padx=5, pady=10)

    label3 = Label(frame, text='.', font=('', 15, 'bold'))
    label3.grid(row=1, column=5)

    entry4 = Entry(frame, width=4, font=bold)
    entry4.grid(row=1, column=6, padx=5, pady=10)


    # 입력필요인 부분은 환경에 맞게 변경하고 사용해야 합니다.
    def change_ethernet_setting(event=True):
        ip_address = entry1.get()+'.'+entry2.get()+'.'+entry3.get()+'.'+entry4.get()
        subnetmask = '255.255.255.0'
        gateway = entry1.get()+'.'+entry2.get()+'.'+entry3.get()+'.'+'254'
        dns1 = '별도입력'
        dns2 = '별도입력'
        print('netsh interface ip set address "이더넷" static '+ip_address+' '+subnetmask+' '+gateway)
        print('netsh -c int ip set dns name="이더넷" static "'+dns1+'" primary')
        print('netsh -c int ip add dns name="이더넷" "'+dns2+'" index=2')
        
        os.system('netsh interface ip set address "이더넷" static '+ip_address+' '+subnetmask+' '+gateway)
        os.system('netsh -c int ip set dns name="이더넷" static "'+dns1+'" primary')
        os.system('netsh -c int ip add dns name="이더넷" "'+dns2+'" index=2')
        
        messagebox.showinfo('완료', '변경완료')
        root.destroy()
        
    def end_setting(event=True):
        root.destroy()
        
    change_btn = Button(frame, text='적용', width=15, command=change_ethernet_setting, relief='groove', font=btn)
    change_btn.grid(columnspan=7, padx=10, pady=10)
    
    
    # Entry1에 시작 focus
    entry1.focus()
    # . 을 눌러 다음 Entry로
    entry1.bind("<period>", lambda event: entry2.focus_set())
    entry2.bind("<period>", lambda event: entry3.focus_set())
    entry3.bind("<period>", lambda event: entry4.focus_set())
    # 엔터로 다음 Entry로
    entry1.bind("<Return>", lambda event: entry2.focus_set())
    entry2.bind("<Return>", lambda event: entry3.focus_set())
    entry3.bind("<Return>", lambda event: entry4.focus_set())
    # 엔터로 저장
    entry4.bind('<Return>', change_ethernet_setting)
    root.bind('<Escape>', end_setting)






def main_window():
    # if messagebox.askyesno('매뉴얼', '[변경 방법]을 확인하고 [예]를 클릭해주세요.\n\n1. 변경 옵션 선택 [민수/방산]\n\n2. 변경할 [IP 입력]\n\n3. [적용] 버튼 클릭'):
        def call():
            os.system('ncpa.cpl')
        win = Tk()
        win.title('IP 변경')
        win.geometry('250x200+400+300')
        win.resizable(False, False)	
        
        lab_ip = Button(win, text=' 현재 IP : '+socket.gethostbyname(socket.gethostname())+' ', 
                        relief='flat', justify ='left', activebackground='darkgreen', activeforeground='white', 
                        background='darkgreen', fg='white', font=bold, command=call)
        lab_ip.pack(padx=5, pady=20)
        
        btn1 = Button(win, text='민수 IP 설정', width=20, command=setting_1, relief='groove', font=btn)
        btn1.pack(padx=5, pady=10)
        
        btn2 = Button(win, text='방산 IP 설정', width=20, command=setting_2, relief='groove', font=btn)
        btn2.pack(padx=5, pady=10)
        
        # btn_auto = Button(win, text='자동 IP 설정', width=20, command=setting_auto, font=font, relief='groove')
        # btn_auto.pack(padx=5, pady=10)
        
        # 메인 윈도우를 ESC로 종료하기
        def end_window(event=True):
            win.destroy()
        win.bind('<Escape>', end_window)
        win.mainloop()
    # else:
        # pass
main_window()