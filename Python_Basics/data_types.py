# Data Types

def main():
    # Integer = whole number representation
    num_of_instances = 5
    hours_running = 10

    # Integer (int)
    my_integer = 39

    # String = sequences of character data
    # String (str)
    instance_type = 't2.micro'

    message = "My instances are of type: "

    print(f"{message} {instance_type}. I have {num_of_instances} of them and they have been running for {hours_running} hours.")

    # Boolean
    # one of two values. True or False
    # Boolean (bool)
    is_on = True
    
     # Floating point numbers
    # Floating point number (float)
    instance_cost_per_hour = 0.75
    
    print(f"Are my instances running? {is_on}")
    
    print(f"My variable is of type: {type(is_on)}.")
    
    print(f"The price of running them per hour is {instance_cost_per_hour} USD.")
    
if __name__ == '__main__':
    main()