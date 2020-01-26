import web
from worker import work

urls=("/","index","/button_2","button_2","/output_3","output_3","/output_0","output_0",)

class index:
	def GET(self):
		render = web.template.render("templates")
		return render.index()

class button_2:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_teller()


class output_3:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_txt_teller()


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

