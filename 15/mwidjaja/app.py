import csv
import datetime
import traceback
from collections import OrderedDict
from flask import Flask, request, render_template, redirect, url_for


class ShoppingList(object):
    def __init__(self):
        self.data_file = 'shoppingList.csv'
        self.item_list = []
        self.load()

    def get_id(self):
        id = str(datetime.datetime.now())
        return id.replace(' ', '_')


    def add(self, item_name, quantity, unit_price):
        id = self.get_id()
        newitem = OrderedDict([('id', id), ('item_name', item_name),
                               ('quantity', int(quantity)),
                               ('unit_price', float(unit_price))])
        self.item_list.append(newitem)
        self.save()
        return


    def edit(self, id, quantity, unit_price):
        for item in self.get_list():
            if item['id'] == id:
                item['quantity'] = int(quantity)
                item['unit_price'] = float(unit_price)
                self.save()


    def delete(self, id):
        self.item_list = list(filter(lambda x: x['id'] != id, self.item_list[:]))
        self.save()
        return


    def get_list(self):
        return self.item_list


    def save(self):
        try:
            with open(self.data_file, 'w') as df:
                fieldnames = ['id', 'item_name', 'quantity', 'unit_price']
                writer = csv.DictWriter(df, fieldnames=fieldnames)
                writer.writeheader()
                for row in self.item_list:
                    writer.writerow(row)
        except:
            traceback.print_exc()


    def _dump(self):
        print(self.get_list())


    def load(self):
        try:
            with open(self.data_file) as df:
                reader = csv.DictReader(df)
                for row in reader:
                    row['quantity'] = int(row['quantity'])
                    row['unit_price'] = int(row['unit_price'])
                    self.item_list.append(row)
        except:
            traceback.print_exc()



app = Flask(__name__)

### Flask Routers

@app.route('/')
def index():
    return render_template('index.html', items=cart.get_list())


@app.route('/add')
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        item_name  = request.form.get('item_name')
        quantity   = request.form.get('quantity')
        unit_price = request.form.get('unit_price')
        cart.add(item_name, quantity, unit_price)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<id>')
@app.route('/edit', methods=['POST'])
def edit(id=None):
    if request.method == 'POST':
        id         = request.form.get('id')
        quantity   = request.form.get('quantity')
        unit_price = request.form.get('unit_price')
        cart.edit(id, quantity, unit_price)
        return redirect(url_for('index'))
    else:
        for item in cart.get_list():
            if item['id'] == id:
                edited = item
        return render_template('edit.html', edit_item=edited)


@app.route('/delete/<id>')
def delete(id=None):
    cart.delete(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    cart = ShoppingList()
    app.run(debug=True)
