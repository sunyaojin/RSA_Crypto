from . import *
from util import *
import random

class rsa_keygen:
	def __init__(self, num_bits):
		self.p = generatePrime(num_bits)
		self.q = generatePrime(num_bits)
		self.n = self.p * self.q
		self.phi = (self.p - 1)*(self.q - 1)
	
	def gen_keypair(self):

		p = self.p
		q  = self.q

		

		e = 65537
		while not GCD(e,self.phi) == 1:
			e = random.randrange(1,phi)
		
		d = extGCD(e, self.phi)
		
		return ((e,self.n),(d, self.n))

