from tkinter import *
from tkinter import ttk
import pytube
import time


root = Tk()


class Funcs():
    def limparentries(self):
        self.entry_1.delete(0, END)

    def downloadpercent(self, stream, chunk, bytes_remaining):
        global previousprogress
        total_size = file_size
        bytes_downloaded = total_size - bytes_remaining
        progresso = (int)(bytes_downloaded / total_size * 100)
        if progresso > previousprogress:
            previousprogress = progresso
            progressvar.set(previousprogress)
            label4var.set(f'{previousprogress}%')
            if (previousprogress == 100):
                label4var.set(f'{numerorandom}%')
                progressvar.set(numerorandom)

    def downloadprogress(self):
        global video
        global file_size
        self.s = var.get()
        try:
            self.you = pytube.YouTube(self.s)
            self.you.register_on_progress_callback(self.downloadpercent)
            self.video = self.you.streams.get_highest_resolution()
            file_size = self.video.filesize
            self.video.download()
        except:
            label4var.set('Ocorreu um erro.')


numerorandom = 0
previousprogress = 0


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.inicial()
        self.frames()
        self.botoes()
        self.labels()
        self.entrys()
        self.progressbar()
        root.mainloop()

    def inicial(self):
        self.root.title('Video Downloader')
        self.root.configure(background='#E0E0F8')
        self.root.geometry('800x800')
        self.root.resizable(False, False)
        self.root.maxsize(width=400, height=400)
        self.root.minsize(width=400, height=400)

    def frames(self):
        self.frame_1 = Frame(self.root, bd=3, bg='#B7D5E5',
                             highlightbackground='#008000', highlightthickness=2)
        self.frame_1.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.00)
        self.frame_2 = Frame(self.frame_1, bg='#C4302B')
        self.frame_2.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.15)
        # FRAME 3, dentro de onde coloca o link
        self.frame_3 = Frame(self.frame_1, bg='#ffffff', bd=2,
                             highlightbackground='#000000', highlightthickness=2)
        self.frame_3.place(relx=0.05, rely=0.20, relwidth=0.90, relheight=0.70)

    def botoes(self):
        self.button_1 = Button(self.frame_1, bg='#90ee90', bd=2, text='Iniciar Download', font=(
            'Verdana', 9, 'bold'), command=self.downloadprogress)
        self.button_1.place(relx=0.193, rely=0.5, relwidth=0.55, relheight=0.1)
        self.button_limpar = Button(
            self.frame_3, text="Limpar", command=self.limparentries)
        self.button_limpar.place(relx=0.050, rely=0.30)

    def labels(self):
        self.label_1 = Label(self.frame_1, bg='#ffffff',
                             text="URL do vídeo:", font=('Verdana', 15, 'bold'))
        self.label_1.place(relx=0.28, rely=0.23)
        # TEXTO NA PARTE VERMELHA
        self.label_2 = Label(self.frame_2, text='Aviso: é indispensável o uso do\n "HTTP://" antes da URL',
                             font=('Verdana', 14, 'bold'), bg='#C4302B')
        self.label_2.place(relx=0.05, rely=0.0)
        # PORCENTAGEM DOWNLOAD
        global label4var
        label4var = StringVar()
        self.label_4 = Label(
            self.frame_3, text='Porcentagem do download:', bg='#ffffff')
        self.label_4.place(relx=0.07, rely=0.6, relwidth=0.6)
        self.label_5 = Label(self.frame_3, text='--',
                             textvariable=label4var, bg='#ffffff')
        self.label_5.place(relx=0.60, rely=0.6)

    def entrys(self):
        global var
        var = StringVar()
        self.entry_1 = Entry(self.frame_1, bg='#DCDCDC', textvariable=var)
        self.entry_1.place(relx=0.20, rely=0.35, relwidth=0.59, relheight=0.05)
        

    def progressbar(self):
        global progressvar
        progressvar = DoubleVar()
        self.progressb_1 = ttk.Progressbar(
            self.frame_3, maximum=100, mode="determinate", variable=progressvar)
        self.progressb_1.place(relx=0.15, rely=0.7, relwidth=0.62)


Application()
