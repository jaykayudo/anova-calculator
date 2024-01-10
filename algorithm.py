class ANOVA:
    def __init__(self):
        print("A Python program to calculate Analysis of Variance (ANOVA).") 
        self.treatment = []
        self.num_treatment = 0 # k = number of groups 
    def run(self):
        # self.read_input() # for command line 
        # self.anova_writeup() # for command line
        self.mean_list = self.calculate_mean()
        self.total_mean_value = self.total_mean(self.mean_list)
        self.num_observation_list = self.number_of_obsevation()
        self.variance_list = self.calculate_variance()
        self.total_num_of_obs = self.total_number_of_observation()
        self.deg_of_freedom_treatment = self.num_treatment - 1
        self.deg_of_freedom_error = self.total_num_of_obs - self.num_treatment
        self.deg_of_freedom_total = self.total_num_of_obs - 1 
        return self.display_table()
    def read_input(self):
        """Collect the treatment and compile it into the treatment list""" 
        self.num_treatment = int(input("Enter number of treatments: "))
        print(f"Enter the observations for the {self.num_treatment} treatments below.")
        print("The number of observations of each treatment can be of any length.")
        print("The observations should be in this format, Eg: 9, 5, 7, 4") 
        for x  in range(self.num_treatment):
            self.treatment.append(
            [int(observation) for observation in input( 
            f"Enter your Treatment {x+1} observations:").strip().split(',')])
    def anova_writeup(self):
        print("Hypothesis")
        print("H0: There is no significant difference among the treatmentmeans.")
        print("H1: There is significant difference among the treatment means for at least one treatment.")
        print()
        print("Model: Xij = M + ti + Eij; i=1,...,n / j=1,...,r")
        print()
        print("Assumptions of the model:")
        print("1. Normality")
        print("2. Constant variance")
        print("3. Independence")
        print()
        print("Test Statistic:")
        print("F = MS Treatment / MS Error")
        print()
        print("Decision Rule:")
        print("Reject H0 if Fcal > Ftab, accept if otherwise")
        print()
    def calculate_mean(self):
        """ Return a list of all the treatment means"""
        mean = list(map(lambda x: sum(x)/len(x),self.treatment)) 
        return mean
    def total_mean(self,means):
        """ Return the mean of all the means""" 
        total_means = sum(means)/len(means) 
        return total_means
    def total_number_of_observation(self):
        """ Returns the total sum of all the observations"""
        total_num = sum(list(map(lambda x: len(x),self.treatment))) 
        return total_num
    def number_of_obsevation(self):
        """ Return a list containing the number of observation in each
        treatment"""
        return list(map(lambda x: len(x),self.treatment)) 
    def calculate_variance(self):
        """ Return a list containing the variance of all treatments""" 
        sd = []
        for treat in self.treatment:
            mean = sum(treat)/len(treat)
            squared_mean = list(map(lambda x: (mean-x)**2,treat)) 
            variance = sum(squared_mean)/(len(squared_mean) - 1) 
            sd.append(variance)
        return sd
    def sum_of_squares_treatment(self): 
        """ Return the sum of squares""" 
        total = 0
        for n,mean in zip(self.num_observation_list,self.mean_list): 
            calc = n *((mean - self.total_mean_value)**2)
            total += calc 
            return total