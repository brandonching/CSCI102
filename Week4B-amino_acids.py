# Brandon Ching
# ​CSCI 102 – Section C
# Week 4 - Lab B - Amino Acids
# References: N/A
# Time: 10 minutes

print("Input the chemical elements of the amino acid:")
carbon = input("CARBON>")
hydrogen = input("HYDROGEN>")
nitrogen = input("NITROGEN>")
oxygen = input("OXYGEN>")
sulfer = input("SULFER>")

combined_acid = carbon + hydrogen + nitrogen + oxygen + sulfer

if combined_acid == "37120":
    acid = "Alanine"
elif combined_acid == "614420":
    acid = "Arginine"
elif combined_acid == "48230":
    acid = "Asparagine"
elif combined_acid == "37121":
    acid = "Cysteine"
elif combined_acid == "69320":
    acid = "Histidine"
elif combined_acid == "510230":
    acid = "Glutamine"


print(f"The amino acid for {carbon}C-{hydrogen}H-{nitrogen}N-{oxygen}O-{sulfer}S is {acid}")
print(f"OUTPUT {carbon}C-{hydrogen}H-{nitrogen}N-{oxygen}O-{sulfer}S")
print(f"OUTPUT {acid}")
