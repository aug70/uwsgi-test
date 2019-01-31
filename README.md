# uwsgi test

Run uwsgi and uwsgitop and test with flask

Make sure you have uwsgitop installed

```
pip install uwsgitop
```

Run the scripts in the following order.

* Run uwsgi.sh
* Run uwsgitop
* Run tester.sh

```
./uwsgi.sh
uwsgitop 127.0.0.1:9191
./tester.sh
```

Test Python multi-threading

```
./run.sh
```

### Links

* [uWSGI, Preforking and Lazy Apps](https://engineering.ticketea.com/uwsgi-preforking-lazy-apps/)
* [uWSGI Project](https://uwsgi-docs.readthedocs.io/en/latest/index.html)
* [uwsgitop](https://pypi.org/project/uwsgitop/)