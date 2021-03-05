""" decorators """
# see https://wiki.python.org/moin/PythonDecoratorLibrary for some useful decorators!!

import time
import logging

import clogging
from ngrams import to_ngrams


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
		log_msg = 'function: {}, runtime: {}, args: {}'.format(func.__name__, elapsed_time, args)
		logger = clogging.getLogger('elapsed_times', filename=file_path, stdout_level=logging.WARNING)
		logger.info(log_msg)
		return out
	return new_func

def on_n_gram(n):
	'''
	Return an n-gram decorator which decorates a distance function.
	A distance function, once decorated, compares sequences of n-grams instead of the base sequences.
	For example, instead of returning
		distance('ABC', 'T')
	on_n_gram(2)(distance) will return
	  distance(('@A', 'AB', 'BC', 'C@'), ('@T', T@'))
	.
	'''
	def on_n_gram_decorator(dist_func):
		def new_dist_func(seq_a, seq_b):
			new_seq_a = to_ngrams(n, seq_a)
			new_seq_b = to_ngrams(n, seq_b)
			return dist_func(new_seq_a, new_seq_b)
		return new_dist_func
	return on_n_gram_decorator






