import web
from worker import work

urls=("/","index","/button_9","button_9","/button_8","button_8","/slider_11/(.*)","slider_11","/button_3","button_3","/button_2","button_2","/button_4","button_4","/button_7","button_7","/button_6","button_6","/select_5/(.*)","select_5","/button_10","button_10","/button_12","button_12","/output_0","output_0",)

class index:
	def GET(self):
		render = web.template.render("templates")
		return render.index()

class button_9:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_last()


class button_8:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_next()


class slider_11:
	def GET(self,val):
		web.header('Content-Type', 'application/json')
		return work.do_sld_volume(val)


class button_3:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_pauze()


class button_2:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_play()


class button_4:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_stop()


class button_7:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_prev()


class button_6:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_first()


class select_5:
	def GET(self,val):
		web.header('Content-Type', 'application/json')
		return work.do_sel_track(val)


class button_10:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_voldown()


class button_12:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return work.do_btn_volup()


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

