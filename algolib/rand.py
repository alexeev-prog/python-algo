import time


class RandGen:
	"""
	This class describes a random generate.
	"""

	def __init__(self, seed: float=None):
		"""
		Constructs a new instance.

		:param      seed:  The seed
		:type       seed:  float
		"""
		self.modulus = 2 ** 31
		self.multiplier = 1103515245
		self.seed = seed if seed is not None else int(time.time() * 1000) % self.modulus
		self.increment = 12345
		self.state = seed

	def _lcg(self):
		self.state = (self.multiplier * self.state + self.increment) % self.modulus
		return self.state

	def randint(self, a: int, b: int) -> int:
		return int(a + self._lcg() % (b - a + 1))

	def randfloat(self, a: float = 0.0, b: float = 1.0) -> float:
		return a + (b - a) * (self._lcg() / self.modulus)

	def randchoice(self, seq: list):
		if not seq:
			return None

		index = self._lcg() % len(seq)
		return seq[int(index)]

	def randshuffle(self, lst):
		n = len(lst)
		for i in range(n - 1, 0, -1):
			j = self.randint(0, i)
			lst[int(i)], lst[int(j)] = lst[int(j)], lst[int(i)]

		return lst

	def randuniform(self, a, b):
		return a + (b - a) * (self._lcg() / self.modulus)
