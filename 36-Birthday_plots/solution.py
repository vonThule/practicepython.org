import json
from bokeh.plotting import figure, show, output_file
from bokeh.models import Range1d


# Read file
def read_data_file(filename):
		with open(filename, "r") as f:
				data = json.load(f)
		return data


# Create list of values:
def create_list(data):
		months = ["January", "February", "March", "April", "May", "June",
				  "July", "August", "September", "October", "November", "December"]
		lst = []
		for month in months:
				if month not in data:
						lst.append(0)
				else:
						lst.append(data[month])
		return lst


# Main function
def main():
		months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
				  "Aug", "Sep", "Oct", "Nov", "Dec"]
		stats = read_data_file("stats.json")
		vals = create_list(stats)
		output_file("plot.html")

		p = figure(plot_width=400, plot_height=400)
		p.x_range = Range1d(0,13)
		p.vbar(x=[1,2,3,4,5,6,7,8,9,10,11,12], width=0.5, bottom=0,
		       top=vals, color="firebrick")

		show(p)


# Run program
if __name__ == "__main__":
		main()

