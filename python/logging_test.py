import logging
logging.basicConfig(format='%(asctime)s : Line: %(lineno)d - %(message)s', level=logging.DEBUG)
logging.debug("A Debug Logging Message {}".format("TEST"))



cls.pool = WorkerProcessPool(max_connections=11, slave_timeout=20)


def parse(self, filename, metadata):
    with self.get_pool().get_connection_context() as worker_process:
        self._logger.info('slave starts working on file: {}'.format(filename))
        result = worker_process.execute_func(_parse_and_wrap_output, cPickle.dumps(self), filename,
                                             self._preprocess(metadata))
        self._logger.info('slave finished working on file: {}'.format(filename))
    result.validate()







class WorkerProcessPool(ConnectionPool):
    def __init__(self, *args, **kwargs):
        interpreter = kwargs.pop('interpreter', DEFAULT_INTERPRETER)
        slave_timeout = kwargs.pop('slave_timeout', DEFAULT_SLAVE_TIMEOUT)
        super(WorkerProcessPool, self).__init__(WorkerProcessFactory(interpreter, slave_timeout), *args, **kwargs)

    def run_in_process(self, func, *args, **kwargs):
        with self.get_connection_context() as worker_process:
            return worker_process.execute_func(func, *args, **kwargs)

    def map(self, func, args):
        jobs = [gevent.spawn(self.run_in_process, func, arg) for arg in args]
        gevent.joinall(jobs, raise_error=True)
        return [job.value for job in jobs]

    def __del__(self):
        self.close()


