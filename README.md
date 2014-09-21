peacehack
=========


### Ukraine mentions in february 2014 (ukraine revolution):

For more info read [here](http://en.wikipedia.org/wiki/2014_Ukrainian_revolution)


![index](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/ukraine_feb.png)

### Ukraine mentions 9th september (plane shot)

For more info read [here](http://www.bbc.co.uk/news/world-europe-28357880)

![index](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/ukraine_set.png)

### Nigeria mentions in november (kidnap)

For more info read [here](http://www.bbc.co.uk/news/world-africa-27120357)

![index](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/nigeria_nov.png)


### Palestine mentions in 8 july

For more info read [here](http://en.wikipedia.org/wiki/2014_Israel%E2%80%93Gaza_conflict)

![index](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/palestine.png)


### Whatever

Next time go for [spark...](https://spark.apache.org/) 

Some interesting stats on a `db.r3.xlarge` (30gb ram 4 cpu, ~20gb data, 58 cols):


![index](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/index.png)

![reads](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/reads_4.png)

![queue depth](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/q_d_4.png)

```
sudo apt-get install python-virtualenv
git clone git@github.com:papaloizouc/peacehack.git
cd peacehack/peacehack
virtualenv venv
source venv/bin/activate
sourve dev.env
pip install -r req.txt
python manage.py collectstatic
python manage.py runserver
```
