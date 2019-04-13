import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import glob
import os
import time
import threading

class Dequeue:

    def __init__(self):
        self.dq = []

    def insertFirst(self, item):
        self.dq.insert(0, item)

    def insertLast(self, item):
        self.dq.append(item)

    def isEmpty(self):
        if len(self.dq) > 0:
            return False
        else:
            return True

    def popFirst(self):
        return self.dq.pop(0)

    def popLast(self):
        return self.dq.pop(-1)

    def peekFirst(self):
        return self.dq[0]

    def peekLast(self):
        return self.dq[-1]

    def print(self):
        print(self.dq)

    def sum(self):
        return sum(self.dq)

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

        # button 추가하기
        f_button = tk.Button(self.window, text = "Filtering", width =15, height=2, command=self.filtering)
        n_button = tk.Button(self.window, text="Noising", width=15, height=2, command=self.noising)
        f_button.pack()
        n_button.pack()

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
        selFile = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("image files", "*.jpg *.png"), ("all files", "*.*")))
        self.image = Image.open(selFile)
        if self.image.size[1] > self.image.size[0]: # width height
            hSize = int((400 * self.image.size[0] / self.image.size[1]))
            vSize = 400
        else:
            hSize = 400
            vSize = int((400 * self.image.size[1] / self.image.size[0]))

        self.image = self.image.resize((hSize, vSize), Image.ANTIALIAS)
        self.image_copy = self.image
        self.image = ImageTk.PhotoImage(self.image)
        self.imgLabel.config(image=self.image) # image update
        self.shape = [self.image_copy.size[1], self.image_copy.size[0], 3]


    # queue를 이용하여 구현하기 : 시간
    def filtering(self):
        start = time.time()
        filtered = np.zeros(self.shape)
        window_size = 3
        gap = window_size // 2 # 제외되는 픽셀수 2: 겹치는 영역
        # 3 by 3 filter
        for i in range(gap, filtered.shape[0] - gap):
            dq = Dequeue()
            for c in range(-gap, gap + 1):
                for r in range(gap, gap + 1):
                    dq.insertLast(self.image_copy[i+r, 1+c])
                    filtered[i, 1] = np.median(dq.dq)
            for j in range(2, filtered.shape[1] - gap):
                for k in range(gap, - gap, -1):
                    dq.popFirst()
                    dq.insertLast(self.image_copy[i + k, j + gap])
                filtered[i,j] = np.median(dq.dq)
        self.image_copy = filtered
        self.image = ImageTk.PhotoImage(Image.fromarray(self.image_copy.astype('uint8')))
        self.imgLabel.config(image=self.image)  # image update
        end = time.time()
        print("time : {}".format(end - start)) # time : 5.266919374465942


    def filtering_before(self):
        start = time.time()
        filtered = np.zeros(self.shape)
        # 3 by 3 filter
        for i in range(1, filtered.shape[0] - 1):
            for j in range(1, filtered.shape[1] - 1):
                filter = Dequeue()
                for c in range(-1,2): # [-1, 0 ,1]
                    for r in range(-1, 2):
                        filter.insertLast(self.image_copy[i+r, j+c])
                filtered[i,j] = np.median(filter.dq)
        self.image_copy = filtered
        self.image = ImageTk.PhotoImage(Image.fromarray(self.image_copy.astype('uint8')))
        self.imgLabel.config(image=self.image)  # image update
        end = time.time()
        print("time : {}".format(end - start)) # time : 8.580297946929932

    def noising(self):
        z = np.random.binomial(1, 0.3, self.shape)
        noise = np.array(self.image_copy).std() * 0.5 + np.random.standard_normal(self.shape)
        z = z * noise
        self.image_copy = self.image_copy + z
        self.image = ImageTk.PhotoImage(Image.fromarray(self.image_copy.astype('uint8')))
        self.imgLabel.config(image=self.image)  # image update


a = Window()
a.window.mainloop()

