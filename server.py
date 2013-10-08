import web, json
import mydb

urls = (
	'/', 'home',
	'/keylog', 'keylog',
    '/keylog/add', 'add',
    '/keylog/source', 'source',
    '/keylog/employee/add', 'employee'
#    '/add', 'add',
)

#where templates live:
render = web.template.render('templates/')

class home:
	def GET(self): #show displaydata.html
		return render.displaydata()

	def POST(self):
		input = web.input()
		web.header('Content-Type', 'application/json')
		return json.dumps({
			'txt' : input.id,
			'dat' : "Paul Stallworth"
		})

class keylog:
	def GET(self): 
		return render.keylog()

#create an aaData property with one entry for each column
#aaData must be an array of arrays, so you gotta figure that out
class add:
    def POST(self):
        input = web.input()
        web.header('Content-Type', 'application/json')
        try:
            mydb.add_record(input)
            return "ok"
        except LookupError:
            web.HTTPError("400: Bad Request",{'Content-Type':'text/html'})
            return "Error: Requestor not found in employee list"

class source:
    def GET(self):
        input = web.input()
        web.header('Content-Type', 'application/json')
        if input.sEcho is not None:
            sEcho = input.sEcho
        else:
            sEcho = 1

        #data = mydb.source_table_json()
        data = mydb.source_table_raw()
        return json.dumps({
            "sEcho" : sEcho,
            "iTotalRecords": "5",
            "iTotalDisplayRecords": "5",
            "aaData" : data
        })


        #return mydb.source_table_json()

class employee:
    def POST(self):
        input = web.input()
        mydb.add_employee(input.id_number, input.name)

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
