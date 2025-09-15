import winsound, os, sys 
import wx
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import sounds


# file path containing the sound track for the correct answer and wrong sound and for the game end sound.
cas_path = r"C:\Users\USER\poetry_master_file\correct-356013.mp3"
was_path = r"C:\Users\USER\poetry_master_file\wrong-answer-21-199825.mp3"
game_end_sound = r"C:\Users\USER\poetry_master_file\game-complete-143022.mp3"


class PoetryMaster(wx.Frame):
    """The class containing my poetry master game."""


    def __init__(self, poems):
        """To initialize the poetry master game window, that contains all the widgets."""
        super().__init__(None, title="Poetry Master", size=(800, 600))
        panel = wx.Panel(self)

        self.poems = poems
        self.current_index = 0
        self.score = 0

        # Widgets
        self.title = wx.StaticText(panel, label = "Poetry Master")
        font = self.title.GetFont()
        font.PointSize += 6
        font = font.Bold()
        self.title.SetFont(font)

        self.poem_text = wx.TextCtrl(panel, value=self.poems[self.current_index]['line'], style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.riddle_text = wx.StaticText(panel, label=self.poems[self.current_index]['riddle'], style=wx.ALIGN_LEFT)
        self.user_answer = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.submit_btn = wx.Button(panel, label="Submit")
        self.next_btn = wx.Button(panel, label="Next")
        self.next_btn.Disable()
        self.feedback = wx.StaticText(panel, label="")
        self.score_label = wx.StaticText(panel, label="Score: 0")

        # this is the layout of the window panel using sizers
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        main_sizer.Add(self.title, 0, wx.ALL | wx.CENTER, 12)
        main_sizer.Add(self.poem_text, 0, wx.ALL | wx.ALIGN_LEFT, 10)
        main_sizer.Add(self.riddle_text, 0, wx.ALL | wx.ALIGN_LEFT, 10)
        main_sizer.Add(self.user_answer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self.submit_btn, 0, wx.ALL, 6)
        btn_sizer.Add(self.next_btn, 0, wx.ALL, 6)
        main_sizer.Add(btn_sizer, 0, wx.CENTER)

        main_sizer.Add(self.feedback, 0, wx.ALL | wx.CENTER, 8)
        main_sizer.Add(self.score_label, 0, wx.ALL | wx.ALIGN_RIGHT, 10)

        panel.SetSizer(main_sizer)

        # Events
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit_button)
        self.next_btn.Bind(wx.EVT_BUTTON, self.next_button)
        self.user_answer.Bind(wx.EVT_TEXT_ENTER, self.on_enter)

        self.Show()


    def on_enter(self, event):
        """handler function, binded to self.user_answer."""
        self.submit_button(event)


    def submit_button(self, event):
        """handler function binded to self.submit_btn."""
        user_answer = self.user_answer.GetValue().lower()
        correct_answer = self.poems[self.current_index]['answer'].lower()
        if user_answer == correct_answer:
            sounds.Correct()
            self.feedback.SetLabel(" Correct!")
            self.score += 1
            self.score_label.SetLabel(f"Score: {self.score}")
            self.current_index += 1
            self.user_answer.SetValue("")
            if self.current_index < len(self.poems):
                self.load_current()
            else:
                self.end_game()
        else:
            sounds.Wrong_answer()
            self.feedback.SetLabel(" Try again!")


    def next_button(self, event):
        """handler function binded to self.next_btn."""
        if self.next_btn.IsEnabled():
            self.current_index += 1
            self.feedback.SetLabel("")
        if self.current_index < len(self.poems):
            self.load_current()
        else:
            self.end_game()


    def load_current(self):
        """loads the current poem line and riddle into the game, and disables the next button until user submits an answer."""
        self.poem_text.SetLabel(self.poems[self.current_index]['line'])
        self.riddle_text.SetLabel(self.poems[self.current_index]['riddle'])
        self.next_btn.Disable()

    def end_game(self):
        """ It ends the game by displaying a completion message and sound and disabling all  controls."""
        sounds.Game_complete()
        wx.MessageBox("Congratulations, You have completed poetry master.")
        self.Close(True)
        wx.GetApp().ExitMainLoop()
        self.user_answer.Disable()
        self.submit_btn.Disable()
        self.next_btn.Disable()

poems = [
    {
        "line": "Remo! Where culture and             reign supreme",
        "riddle": "I am passed down through ages, a custom, a belief. I bind the past to what is to be, in ceremonies, dance or a family tree.",
        "answer": "tradition"
    },
    {
        "line": "Remo! The ------- of peace and prosperity",
        "riddle": "I have a crown but am no king, I have subjects but no voice to sing, I hold great power wealth and land, ruled by a sovereign's firm hand.",
        "answer": "kingdom"
    },
    {
        "line": "Remo! My home, my heritage, my -----",
        "riddle": "I can be a virtue or sin, a feeling of worth, or where troubles begin. I can lift you high or make you fall. a family of lions.",
        "answer": "pride"
    },
    {
        "line": "Remo! Where the Akarigbo;s wisdom ------ us",
        "riddle": "I show the way but have no feet. I open doors but I have no hands, I offer wisdom but I have no voice.",
        "answer": "guides"
    },
    {
        "line": "Remo! The land of ------- soil and abundant harvest",
        "riddle": "I am in the business of production. I produce offspring, plants and ideas. The more you engage me, the more abundant your results are.",
        "answer": "fertile"
    },
    {
        "line": "Remo! Where --------- and family ties are strong",
        "riddle": "I am built of many but I have no bricks, I share joy and sorrow but I have no voice, I grow stronger with connection but I have no roots.",
        "answer": "community"
    },
    {
        "line": "Remo! The heart of Yoruba ------- and tradition",
        "riddle": "I am learned not born, and passed down through generations. I shape your views, your food and your celebrations, I can unite or divide, yet I am constantly evolving.",
        "answer": "culture"
    },
    {
        "line": "Remo! A kingdom rich in ------- and heritage",
        "riddle": "I speak of events long past, but have no voice of my own, I teach lessons from triumphs and disasters, yet I wasn't there to see them sewn.",
        "answer": "history"
    },
    {
        "line": "Remo! My root, my identity, my ----------",
        "riddle": "I have no beginning, and I have no end. I encompass all that is and all that will transcend.",
        "answer": "everything"
    },
    {
        "line": "Remo! The land of festivals and -----------",
        "riddle": "I bring people together with joy and cheer, often marked with music, laughter and no fear. I can be big or small, for a triumph or a birth, what am I that fills the air with mirth",
        "answer": "celebration"
    },
    {
        "line": "Remo! Where the Oro Olapakala and obalofun festivals come -----",
        "riddle": "I can breathe, I can grow, I can feel but I'm not a robot, a stone or steel.",
        "answer": "alive"
    },
    {
        "line": "Remo! A -----------",
        "riddle": "I open doors, not with a key, and make strangers feel like family. I offer comfort, food and cheer, dispelling all your doubt and fear.",
        "answer": "hospitality"
    },
    {
        "line": "Remo! Where tradition meets ----------",
        "riddle": "I am born from a thought but I change the world, I am not magic, but I make the impossible unfurl. I am sometimes feared, but always sought.",
        "answer": "innovation"
    },
    {
        "line": "Remo! My heritage, my pride, my ------",
        "riddle": "I am what's left when you are gone, a story whispered, a torch passed on. I can be built with effort or fade with time, a shadow stretching, a truth sublime.",
        "answer": "legacy"
    },
    {
        "line": "Remo! Remo! Remo! ----!",
        "riddle": "I am a word repeated, a constant refrain, from the beginning of the match till a break which is now. I am a community, a place where culture thrives and the traditions of the Yoruba ancestors exist.",
        "answer": "remo"
    }
]

app = wx.App(False)
frame = PoetryMaster(poems)
app.MainLoop()
