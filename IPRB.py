'''
Problem
 Mendel stated that every organism possesses a pair of alleles for a given factor.
 If an individual's two alleles for a given factor are the same,
 then it is homozygous for the factor;
 if the alleles differ, then the individual is heterozygous.
 The first law concludes that for any factor,
 an organism randomly passes one of its two alleles to each offspring,
 so that an individual receives one allele from each parent.
 Mendel also believed that any factor corresponds to only two possible alleles, the dominant and recessive alleles.

Probability is the mathematical study of randomly occurring phenomena.
We will model such a phenomenon with a random variable,
which is simply a variable that can take a number of different distinct outcomes
depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls.
If we let X represent the random variable corresponding to the color of a drawn ball,
then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

Random variables can be combined to yield new random variables.
Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball).
The probability of Y being red depends on whether the first ball was red or blue.
To represent all outcomes of X and Y, we therefore use a probability tree diagram.
This branching diagram represents all possible individual probabilities for X and Y,
with outcomes at the endpoints ("leaves") of the tree.
The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree;

An event is simply a collection of outcomes. Because outcomes are distinct,
the probability of an event can be written as the sum of the probabilities of its constituent outcomes.
For our colored ball example, let A be the event "Y is blue."
Pr(A) is equal to the sum of the probabilities of two different outcomes:
Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25.

Given: Three positive integers k, m, and n,
representing a population containing k+m+n organisms:
k individuals are homozygous dominant for a factor,
m are heterozygous, and
n are homozygous recessive.

Return: The probability that two randomly selected mating organisms
will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype).
Assume that any two organisms can mate.
'''
# Probability issue
def prob_dominant(k, m, n):
    # Total population
    pop_total = k + m + n
    # Total probability
    total_prob = 1
    # Probabilities of choosing different pairs
    prob_kk = (k/pop_total) * ((k-1)/(pop_total-1))
    prob_km = (k/pop_total) * (m/(pop_total-1)) + (m/pop_total) * (k/(pop_total-1))
    prob_kn = (k/pop_total) * (n/(pop_total-1)) + (n/pop_total) * (k/(pop_total-1))
    prob_mm = (m/pop_total) * ((m-1)/(pop_total-1))
    prob_mn = (m/pop_total) * (n/(pop_total-1)) + (n/pop_total) * (m/(pop_total-1))
    prob_nn = (n/pop_total) * ((n-1)/(pop_total-1))
    # Probability of dominant allele
    prob_dom = total_prob * (prob_kk + prob_km + prob_kn + 0.75*prob_mm + 0.5*prob_mn)
    return prob_dom

# k, m, n = 2, 2, 2
# print(prob_dominant(k, m, n))
