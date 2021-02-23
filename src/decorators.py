""" decorators """
# see https://wiki.python.org/moin/PythonDecoratorLibrary for some useful decorators!!

import time
import logging

import clogging


def transparent(decorator):
	""" Decorators have a few unwanted side effects.  This decorator, when used on a decorator, reverses those side-effects!

	Longer explanation: This decorator can be used to turn simple functions
	into well-behaved decorators, so long as the decorators
	are fairly simple. If a decorator expects a function and
	returns a function (no descriptors), and if it doesn't
	modify function attributes or docstring, then it is
	eligible to use this. Simply apply @transparent to
	your decorator and it will automatically preserve the
	docstring and function attributes of functions to which
	it is applied.
	"""
	def new_decorator(func, *args, **kwargs):
		g = decorator(func, *args, **kwargs)
		g.__name__ = func.__name__
		g.__doc__ = func.__doc__
		g.__dict__.update(func.__dict__)
		return g
	# Now a few lines needed to make transparent *itself*
	# be a well-behaved decorator!
	new_decorator.__name__ = decorator.__name__
	new_decorator.__doc__ = decorator.__doc__
	new_decorator.__dict__.update(decorator.__dict__)
	return new_decorator

@transparent
def record_elapsed_time(func, file_path='elapsed_times.log'):
	def new_func(*args, **kwargs):
		start_time = time.time()
		out = func(*args, **kwargs)
		end_time = time.time()
		elapsed_time = end_time - start_time
		log_msg = 'function: {}\truntime: {}'.format(func.__name__, elapsed_time)
		logger = clogging.getLogger('elapsed_times', filename=file_path, stdout_level=logging.WARNING)
		logger.info(log_msg + str(logger))
		return out
	return new_func

