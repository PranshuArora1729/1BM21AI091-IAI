def main():
    # Input probabilities
    prob_not_reading_morning = 0.5
    prob_not_reading_evening = 0.4
    prob_reading_both = 0.2
    prob_reading_morning = 1-prob_not_reading_morning
    prob_reading_evening = 1-prob_not_reading_evening

    
    # Calculate the probability of reading morning or evening newspaper
    prob_reading_morning_or_evening = (prob_reading_morning + prob_reading_evening - prob_reading_both)
    
    # Print the result as an irreducible fraction
    print(convert_to_fraction(prob_reading_morning_or_evening))

# Function to convert a decimal to an irreducible fraction
def convert_to_fraction(decimal):
    from fractions import Fraction
    fraction = Fraction(decimal).limit_denominator()
    return f"{fraction.numerator}/{fraction.denominator}"

if __name__ == "__main__":
    main()
