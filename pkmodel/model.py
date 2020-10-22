#
# Model class
#

class Body:
    """A class which constructs a body with a central compartment. 

    :param V_c:     volume of central compartment
    :param q_c:     quantity of drug in central compartment 
    :param CL:      clearance rate of central compartment
    :param dose:    drug dose function

    functions: 

    - add_compartment:  adds a peripheral compartment to the central compartment
                        :param V: volume of peripheral compartment
                        :param q: quantity of drug in peripheral compartment
                        :param Q: transaction rate between central and peripheral compartment

    - dqdt:             Calculates the rate of change of the drug quantity in the central compartment.

    - run_PKmodel:      runs a pharmokinetic model on the body

    """
    def __init__(self, V_c, q_c, CL, dose):
        """Initialise body object.
        
        """
        self.V_c = V_c
        self.q_c = q_c
        self.CL = CL
        self.dose = dose
        self.compartments = []

    def add_compartment(self, V, q, Q):
        """Adds a peripheral compartment to the model.
        
        :param V: volume of compartment
        :param q: quantity of compartment
        :param Q: transition rate of compartment 

        :returns: created compartment
        """

        from pkmodel.compartment import Compartment

        new_compartment = Compartment(V, q, Q)
        self.compartments.append(new_compartment)
        return new_compartment

    def dqdt(self, t, q):
        """Calculates the rate of change of drug quantity in the central compartment
        
        :returns: rate of change of drug quantity in the central compartment at time t"""

        dq_cdt = self.dose(t) - (self.q_c/self.V_c)*self.CL
        for comp in self.compartments:
            dq_cdt = dq_cdt - comp.dqdt(self)
        return dq_cdt

    def run_PKmodel(self,t):

        import scipy.integrate
        
        q0 = [self.q_c]
        for comp in self.compartments:
            q0.append(comp.q)

        return scipy.integrate.solve_ivp(
            fun=self.dqdt,
            t_span=[t[0], t[-1]],
            y0=q0,
            t_eval=t,
        )
    





