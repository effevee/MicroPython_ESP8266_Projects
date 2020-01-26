import web
from worker import work

urls=("/","index","/button_3","button_3","/toggle_2/(.*)","toggle_2","/output_0","output_0",)

class index:
	def GET(self):
		render = web.template.render("templates")
		return render.index()

class button_3:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btnStopESP()


class toggle_2:
	def GET(self,val):
		web.header('Content-Type', 'application/json')
		return work.do_tgLedESP(val)


class output_0:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_output_0()


def main():
	try:
		work.start()
		app = web.application(urls,globals())
		app.run()
	except Exception as e:
		print(e)
		print("Server failed or stopped")
		work.stop()

if __name__ == "__main__":
	main()

