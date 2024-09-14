# Multinomial distribution is a generalization of binomial distribution.

# It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

# It has three parameters:

# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.



from numpy import random
import matplotlib.pyplot as mt
import seaborn as sb

sb.distplot(random.multinomial(n=100, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=1000))
mt.show()




# Exponential distribution is used for describing time till next event e.g. failure/success etc.

# It has two parameters:

# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
# size - The shape of the returned array.




x = random.exponential(scale=2 , size=(2,5))
print(x)


sb.distplot(random.exponential(size=1000), hist=False)
mt.show()




# Chi Square distribution is used as a basis to verify the hypothesis.

# It has two parameters:

# df - (degree of freedom).
# size - The shape of the returned array.

sb.distplot(random.chisquare(df=45 , size=200), kde=False)
mt.show()




# Rayleigh distribution is used in signal processing.

# It has two parameters:

# scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size - The shape of the returned array.


sb.distplot(random.rayleigh(scale=10, size=100), hist=False)
mt.show()



x = random.rayleigh(scale=2, size=(2, 3))
print(x)




# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

# It has two parameter:

# a - shape parameter.
# size - The shape of the returned array.


sb.distplot(random.pareto(a=10, size=100), hist=False)
mt.show()



x = random.pareto(a=2, size=(2, 3))
print(x)




# Zipf distributions are used to sample data based on zipf's law.
# Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.

# It has two parameters:

# a - distribution parameter.
# size - The shape of the returned array.



x = random.zipf(a=2, size=(2,3))
print(x)


sb.distplot(random.zipf(a=10, size=100), kde=False)
mt.show()



x = random.zipf(a=2, size=1000)
sb.distplot(x[x<10], kde=False)

mt.show()