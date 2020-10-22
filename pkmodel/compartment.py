class Compartment:
    """Peripheral compartment to be used in the PK model. 
    
    :param V: volume of compartment
    :param q: quantity of compartment
    :param Q: transition rate of compartment 
    
    - function dqdt calculates rate of change of drug quantity in the compartment.
    """

    def __init__(self, V, q, Q):
        self.V = V
        self.q = q
        self.Q = Q

    def dqdt(self, PKmodel):
        """Calculates the rate of change of drug quantity for the compartment.
        
        :param PKmodel: model to use quantity and volume of central compartment
        :param V: volume of compartment
        :param q: quantity of compartment
        :param Q: transition rate of compartment
        """

        return self.Q*(PKmodel.q_c/PKmodel.V_c - self.q/self.V)

    
