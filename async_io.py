import  asyncio


import logging
logging.basicConfig(format='%(asctime)s : %(filename)s:%(lineno)d - %(funcName)s() %(message)s', level=logging.DEBUG)

def main_basic_event_loop():
    #co-routine object
    async def say_Hello():
        logging.debug("HELLO")
        #transfer control back to event loop and on timeout event this co-routine will resume
        await asyncio.sleep(1)
        logging.debug("WORLD")
        return "hello world is done"


    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(say_Hello())

    loop.close()
    logging.info(result)


def main_subtasks_event_loop():
    #co-routine object
    async def main_task():
        logging.debug("main_task starting")
        result1 = await task_one()
        logging.debug("main_task task 1 done")
        result2 = await task_two()
        logging.debug("main_task task 2 done")
        return (result1, result2)

    async def task_one():
        logging.debug("task_one starting ")
        return "TASK 1"


    async def task_two():
        logging.debug("task_two starting ")
        return "TASK 2"

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main_task())

    loop.close()
    logging.info(result)

def main_multiple_subroutine_wait():

    async def get_item(num):
        logging.debug("GET_ITEM start with value {}".format(num))
        await asyncio.sleep(num)
        logging.debug("GET_ITEM end with value {}".format(num))
        return "ITEM " +str(num)


    async def get_items(nums):
        logging.debug("GETTING ITEMS START")
        item_coroutines = [get_item(i) for i in range(1, nums+1)]
        logging.debug("GETTING ITEMS WAITING TO COMPLETE")

        # this will gether result and send in sequence of taks creation
        # its replacement of wait, but in this we can not cancel the task
        #return await asyncio.gather(*item_coroutines) # this will gether result and send in sequence of taks creation

        completed, pending = await asyncio.wait(item_coroutines, timeout=2)
        results = [t.result() for t in completed]
        logging.debug("results {}".format(results))

        if pending:
            logging.debug("Cancelling pending total {} taks ".format(len(pending)))
            for t in pending:
                t.cancel()

        return  results

    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(get_items(4))
    finally:
        loop.close()

    logging.info(result)

def aiohttp_web_applicatoion():
    import aiohttp.web

    #below code have some issue but it will work
    # async def handle(request):
    #     return web.Response("HELLO MAIN")
    #
    #
    # app = web.Application()
    # app.router.add_get("/", handle)
    # #app.router.add_get("/{name}", handle)
    #
    # web.run_app(app)


def aiofiles_apis():
    pass
    # async with aiofile.open("/tmp/myfile") as f:
    #     contents = await f.read()
    # print(contents)


def asyncio_thread():
    pass
    #this is used, if we doing any blocking call in task


def async_dbs():
    pass
    # aiomyssql
    # aiocasandra
    # aiocouchdb
    # aiopg--postgress

if __name__ == "__main__":
    #main_basic_event_loop()
    #main_subtasks_event_loop()
    #main_multiple_subroutine_wait()
    aiohttp_web_applicatoion()




    """
    future has below method
        cancel
        done
        result
        exception
        add_done_callback
    """