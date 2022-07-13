Prime=int(input("Enter the Prime Modulus: "))
Generator=int(input("Enter the Generator G: "))
Alice=int(input("Enter the Private Key of Alice: "))
Bob=int(input("Enter the Private Key of Bob: "))
Alice_public_Key=(Generator**Alice)%Prime
Bob_public_Key=(Generator**Bob)%Prime
Shared_secret_Alice=(Bob_public_Key**Alice)%Prime
Shared_secret_Bob=(Alice_public_Key**Bob)%Prime
print("The shared secret is: ",Shared_secret_Alice)