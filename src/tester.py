from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
import concurrent.futures
from threading import currentThread
from flask import Flask

from time import sleep


app = Flask(__name__)


@app.route('/test')
def test():
    items = ['1', '2', '3', '4']
    executor = ThreadPoolExecutor(len(items))

    def process_item(item):
        sleep(5)
        print currentThread().getName() + " processed ->" + item
        return item

    future_to_item = {executor.submit(process_item, item): item for item in items}
    result = None
    for future in concurrent.futures.as_completed(future_to_item):
        item = future_to_item[future]
        try:
            result += future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (item, exc))
    return result
