import json
import zipfile
from io import TextIOWrapper
import csv

with open('banks.json', 'r') as file:
    banks_data = {row['name']:row['lei'] for row in json.load(file)} 
       
# banks_data={}    
# for row in json.load(file):
#     row['name'] = row['lei']
    
        #create a dict entry for each row in each row in json.load, list comprehension but in dict, name of bank as a key, lei as value

class Applicant:
    def __init__(self, age, race):
        self.age = age
        self.race = set()
#         race_lookup = {
#         "1": "American Indian or Alaska Native",
#         "2": "Asian",
#         "3": "Black or African American",
#         "4": "Native Hawaiian or Other Pacific Islander",
#         "5": "White",
#         "21": "Asian Indian",
#         "22": "Chinese",
#         "23": "Filipino",
#         "24": "Japanese",
#         "25": "Korean",
#         "26": "Vietnamese",
#         "27": "Other Asian",
#         "41": "Native Hawaiian",
#         "42": "Guamanian or Chamorro",
#         "43": "Samoan",
#         "44": "Other Pacific Islander"
# }
        for r in race:
            if r in race_lookup:
                self.race.add(race_lookup[r])
                
    def __repr__(self):
        sorted_race = sorted(self.race)
        return f"Applicant('{self.age}', {sorted_race})"
        

    def lower_age(self):
        if '-' in self.age:
            age_range = self.age.split('-')
            return int(age_range[0])
        elif self.age.startswith("<"):
            return int(self.age[1:])
        elif self.age.startswith(">"):
            return int(self.age[1:])
        else:
            return int(self.age)
        
    def __lt__(self, other):
        return self.lower_age() < other.lower_age()

race_lookup = {
    "1": "American Indian or Alaska Native",
    "2": "Asian",
    "3": "Black or African American",
    "4": "Native Hawaiian or Other Pacific Islander",
    "5": "White",
    "21": "Asian Indian",
    "22": "Chinese",
    "23": "Filipino",
    "24": "Japanese",
    "25": "Korean",
    "26": "Vietnamese",
    "27": "Other Asian",
    "41": "Native Hawaiian",
    "42": "Guamanian or Chamorro",
    "43": "Samoan",
    "44": "Other Pacific Islander"
}





class Loan:
    def __init__(self, values):
        # Converts strings to floats while handling missing values
        self.loan_amount = float(values["loan_amount"]) if values["loan_amount"] not in ["NA", "Exempt"] else -1
        self.property_value = float(values["property_value"]) if values["property_value"] not in ["NA", "Exempt"] else -1
        self.interest_rate = float(values["interest_rate"]) if values["interest_rate"] not in ["NA", "Exempt"] else -1

        self.applicants = []

        # Creates the primary applicant
        primary_applicant_age = values["applicant_age"]
        primary_applicant_race = [values[f"applicant_race-{i}"] for i in range(1, 6) if values.get(f"applicant_race-{i}")]
        primary_applicant = Applicant(primary_applicant_age, primary_applicant_race)
        self.applicants.append(primary_applicant)

        # Checks if there's a co-applicant
        if values["co-applicant_age"] != "9999":
            co_applicant_age = values["co-applicant_age"]
            co_applicant_race = [values[f"co-applicant_race-{i}"] for i in range(1, 6) if values.get(f"co-applicant_race-{i}")]
            co_applicant = Applicant(co_applicant_age, co_applicant_race)
            self.applicants.append(co_applicant)
    def __str__(self):
        return f"<Loan: {self.interest_rate}% on ${self.property_value} with {len(self.applicants)} applicant(s)>"

    def __repr__(self):
        return self.__str__()
    
#     def yearly_amounts(self, yearly_payment):
#         assert yearly_payment > 0
#         assert self.interest_rate >= 0
#         assert self.loan_amount > 0

#         amt = self.loan_amount

#         while amt > 0:
#             yield amt
#             interest = self.interest_rate / 100 * amt
#             amt = amt + interest - yearly_payment
#             if amt < 0:
#                 amt = 0
    def yearly_amounts(self, yearly_payment):
        # assert yearly_payment > 0
        assert self.interest_rate >= 0
        assert self.loan_amount > 0

        amt = self.loan_amount
        # years = 0

        while amt > 0:
            yield amt
            interest = self.interest_rate / 100 * amt
            amt = amt + interest - yearly_payment
            # years += 1
            # if amt < 0:
            #     amt = 0




# values = {
#     'loan_amount': '325000.0',
#     'property_value': '445000',
#     'interest_rate': '2.5',
#     'applicant_age': '35-44',
#     'applicant_race-1': '5',
#     'applicant_race-2': '',
#     'applicant_race-3': '',
#     'applicant_race-4': '',
#     'applicant_race-5': '',
#     'co-applicant_age': '35-44',
#     'co-applicant_race-1': '5',
#     'co-applicant_race-2': '',
#     'co-applicant_race-3': '',
#     'co-applicant_race-4': '',
#     'co-applicant_race-5': ''
# }
values = {'activity_year': '2021', 'lei': '549300Q76VHK6FGPX546', 'derived_msa-md': '24580', 'state_code': 'WI','county_code': '55009', 'census_tract': '55009020702', 'conforming_loan_limit': 'C', 'derived_loan_product_type': 'Conventional:First Lien', 'derived_dwelling_category': 'Single Family (1-4 Units):Site-Built', 'derived_ethnicity': 'Not Hispanic or Latino', 'derived_race': 'White', 'derived_sex': 'Joint', 'action_taken': '1', 'purchaser_type': '1', 'preapproval': '2', 'loan_type': '1', 'loan_purpose': '31', 'lien_status': '1', 'reverse_mortgage': '2', 'open-end_line_of_credit': '2', 'business_or_commercial_purpose': '2', 'loan_amount': '325000.0', 'loan_to_value_ratio': '73.409', 'interest_rate': '2.5', 'rate_spread': '0.304', 'hoepa_status': '2', 'total_loan_costs': '3932.75', 'total_points_and_fees': 'NA', 'origination_charges': '3117.5', 'discount_points': '', 'lender_credits': '', 'loan_term': '240', 'prepayment_penalty_term': 'NA', 'intro_rate_period': 'NA', 'negative_amortization': '2', 'interest_only_payment': '2', 'balloon_payment': '2', 'other_nonamortizing_features': '2', 'property_value': '445000', 'construction_method': '1', 'occupancy_type': '1', 'manufactured_home_secured_property_type': '3', 'manufactured_home_land_property_interest': '5', 'total_units': '1', 'multifamily_affordable_units': 'NA', 'income': '264', 'debt_to_income_ratio': '20%-<30%', 'applicant_credit_score_type': '2', 'co-applicant_credit_score_type': '9', 'applicant_ethnicity-1': '2', 'applicant_ethnicity-2': '', 'applicant_ethnicity-3': '', 'applicant_ethnicity-4': '', 'applicant_ethnicity-5': '', 'co-applicant_ethnicity-1': '2', 'co-applicant_ethnicity-2': '', 'co-applicant_ethnicity-3': '', 'co-applicant_ethnicity-4': '', 'co-applicant_ethnicity-5': '', 'applicant_ethnicity_observed': '2', 'co-applicant_ethnicity_observed': '2', 'applicant_race-1': '5', 'applicant_race-2': '', 'applicant_race-3': '', 'applicant_race-4': '', 'applicant_race-5': '', 'co-applicant_race-1': '5', 'co-applicant_race-2': '', 'co-applicant_race-3': '', 'co-applicant_race-4': '', 'co-applicant_race-5': '', 'applicant_race_observed': '2', 'co-applicant_race_observed': '2', 'applicant_sex': '1', 'co-applicant_sex': '2', 'applicant_sex_observed': '2', 'co-applicant_sex_observed': '2', 'applicant_age': '35-44', 'co-applicant_age': '35-44', 'applicant_age_above_62': 'No', 'co-applicant_age_above_62': 'No', 'submission_of_application': '1', 'initially_payable_to_institution': '1', 'aus-1': '1', 'aus-2': '', 'aus-3': '', 'aus-4': '', 'aus-5': '', 'denial_reason-1': '10', 'denial_reason-2': '', 'denial_reason-3': '', 'denial_reason-4': '', 'tract_population': '6839', 'tract_minority_population_percent': '8.85999999999999943', 'ffiec_msa_md_median_family_income': '80100', 'tract_to_msa_income_percentage': '150', 'tract_owner_occupied_units': '1701', 'tract_one_to_four_family_homes': '2056', 'tract_median_age_of_housing_units': '15'}



class Bank:
    def __init__(self, name):
        
        #Initialization
        self.name = None
        self.lei = None
        self.loans = []
        
        self.name = name
        self.lei = banks_data[name] #not a string as opposed to above!!! unique key vs column name
        
#         # Check if the bank name exists in the data
        # for bank_info in banks_data:
        #     if 'name' in bank_info and 'lei' in bank_info:
        #         if bank_info['name'] == name:
        #             self.name = bank_info['name']
        #             self.lei = bank_info['lei']
        #             break  # Stop searching once a match is found
                    
                    
        if self.name is None:
            raise ValueError(f"Bank name '{name}' not found in banks.json")
            

        # # Read loans from wi.csv inside wi.zip
        # with zipfile.ZipFile('wi.zip', 'r') as zip_file:
        #     with zip_file.open('wi.csv') as csv_file:
        #         tio = TextIOWrapper(csv_file)
        #         csv_data = csv.DictReader(tio)
        with zipfile.ZipFile('wi.zip', 'r') as zip_file:
            with zip_file.open('wi.csv') as csv_file:
                tio = TextIOWrapper(csv_file)
                csv_data = csv.DictReader(tio)
                for row in csv_data:
                    #print(i)
                    if 'lei' in row and row['lei'] == self.lei:
                        loan = Loan(row)
                        self.loans.append(loan)
                # csv_text = csv_file.read().decode('utf-8')
                # csv_data = csv.DictReader(csv_text.splitlines())
                # for row in csv_data:
                #     if 'lei' in row and row['lei'] == self.lei:
                #         loan = Loan(row)
                #         self.loans.append(loan)
                    # self.loans = [Loan(row) for row in csv_data if 'lei' in row and row['lei'] == self.lei]

    def find_fifth_largest_interest_rate(self):
        def get_fifth_largest(node, count):
            if node is None or count[0] == 5:
                return

            # Traverse the tree in reverse order (right, root, left)
            get_fifth_largest(node.right, count)

            # Check if we've found the fifth largest interest rate
            count[0] += 1
            if count[0] == 5:
                count[1] = node.key

            get_fifth_largest(node.left, count)

        count = [0, None]
        get_fifth_largest(self.bst.root, count)

        if count[1] is not None:
            return count[1]
        else:
            return "No fifth largest interest rate found"
        
    def __len__(self):
        return len(self.loans)
    
    def __getitem__(self, num):
        return self.loans[num]
                        