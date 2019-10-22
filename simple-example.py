# import the necessary packages
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")

#args = vars(ap.parse_args())
#ap = argparse.ArgumentParser()

ap.add_argument("-i", "--idade", required= True,
    help="age of the user")

args = vars(ap.parse_args())


print(args)
# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))

print("Seu nome é {0} e sua idade é {1}".format(args["name"],args["idade"]) )



