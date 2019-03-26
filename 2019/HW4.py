from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import glob
import os
import matplotlib
import time
import threading
class Window:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Image Viewer")
        self.window.geometry("640x480")
        self.window.resizable(False, False)
        self.Done=False

        # 메뉴바를 윈도우에 추가한다.
        menubar = tk.Menu(self.window)
        menu_1 = tk.Menu(menubar, tearoff=0)
        menu_1.bind('<<MenuSelect>>')

        menu_1.add_command(label="Open", command=self.fileSelect)
        menubar.add_cascade(label="File", menu=menu_1)


        self.window.config(menu=menubar)

        # 이미지 라벨을 추가한다.
        self.imgLabel = tk.Label(self.window, width=400, height=400, relief='solid')
        self.imgLabel.pack()
        # self.window.mainloop()


    # 메뉴에서 close 가 선택되었을 때 수행한다.
    def close(self):
        self.window.quit()
        self.window.destroy()

    # 파일을 선택한다.
    def fileSelect(self):
        # 초기 디렉토리를 루트로 지정하고 파일을 선택하면 해당 파일명을 selFile에 입력한다.
        selFile=filedialog.askdirectory()
        #selFile = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("image files", "*.jpg *.png"), ("all files", "*.*")))

        print(selFile)
       # filelist
        self.filelist=glob.glob(os.path.join(selFile, "*.png"))
        self.filelist+=glob.glob(os.path.join(selFile, "*.jpg"))
        self.Done=True



    def update(self):
        print("Done : {}".format(self.Done))
        if not self.Done:
            threading.Timer(1, a.update).start()
            return None
        for img in self.filelist:
            self.image = Image.open(img)
            print(self.image.size[0], self.image.size[1])
            # 해당 이미지의 크기를 400, 400으로 resize 한다.
            if self.image.size[1] > self.image.size[0]:
                hSize = int((400 * self.image.size[0] / self.image.size[1]))
                vSize = 400
            else:
                hSize = 400
                vSize = int((400 * self.image.size[1] / self.image.size[0]))

                self.image = self.image.resize((hSize,vSize), Image.ANTIALIAS)
                self.image = ImageTk.PhotoImage(self.image)
                self.imgLabel.config(image = self.image)
            time.sleep(3)
        self.Done=False
        print("모든 이미지 출력 완료!")

        threading.Timer(1, a.update).start()

a = Window()
threading.Timer(1,a.update).start()
a.window.mainloop()

