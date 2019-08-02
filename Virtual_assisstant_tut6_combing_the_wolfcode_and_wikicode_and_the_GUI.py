# Main Exe File for VA
import wx
import wolframalpha, wikipedia
import pyttsx3


engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", rate-50)
engine.say("Welcome. How may I help you?")
engine.runAndWait()
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, 
			pos = wx.DefaultPosition, size = wx.Size(450, 100),
			style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
			wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
			title = "Virtutal Assistant")
		panel = wx.Panel(self)
		my_sizer = wx.BoxSizer(wx.VERTICAL)
		lbl = wx.StaticText(panel,
			label = "Good Morning Sir ! How may I help you today: ")
		my_sizer.Add(lbl, 0, wx.ALL, 5)
		self.txt = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER, 
			size = (400, 30))
		self.txt.SetFocus()
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
		my_sizer.Add(self.txt, 0, wx.ALL, 5)
		panel.SetSizer(my_sizer)
		self.Show()


	def OnEnter(self, event):
		input = self.txt.GetValue()
		input = input.lower()
		try:
			app_id = "27TVTP-U73LTV9EEJ" #storing the app id so that we can the wolframalpha engine 
			client = wolframalpha.Client(app_id) #telling the wolframalpha that we using this app from your own website to search and do shit

			answer = client.query(input)#giving the question to wolframalpha so that it can solve the querry
			output = next(answer.results).text #to format the answer into plain text i.e next().text does that! and answer.results gets the results from wolframalpha api
			print(output)#outputting the answers idiot !!!
			engine.say("The is answer is " + output)
			engine.runAndWait()
		except:
			result = wikipedia.summary(input, sentences = 2) #the sentences kwargs is used for limiting your output it cannot be > 10
			print(result)
			engine.say(result)
			engine.runAndWait()

if __name__ == '__main__':
	app = wx.App(True)
	frame = MyFrame()
	app.MainLoop()
