
def main():
    aws_services = ['s3', 'Lambda', 'EC2', 'RDS', 'DynamoDB']
    print(f"AWS services list: {aws_services}")
    print("\n Using a for loop to iterate through the list:")
    for service in aws_services:
        print(service)
    print("\n Using a while loop to iterate through the list in reverse order")    
    index = len(aws_services) - 1
    while index > 0:
        print(aws_services[index])
        index -= 1 


    print("\n Using enumerate() with a for loop to get both index and value:")
    for index, service in enumerate(aws_services):
        print(f"service #{index + 1}: {service}.")    


if __name__ == "__main__":
    main()

