import sys

pins = []
names = []
variant = 1

def process():
    print("Generating constraint properties from input pin/port pairs")
    print("Listing....")
    for i in range(len(pins)):
        pin = pins[i]
        name = names[i]
        if variant > 1:
            print("set_property PACKAGE_PIN " + pin + " [get_ports {" + name + "}];")
            print("set_property IOSTANDARD LVCMOS33 [get_ports {" + name + "}];")
        else:
            print("set_property -dict {PACKAGE_PIN " + pin + " IOSTANDARD LVCMOS33} [get_ports {" + name + "}];")
    sys.exit(0)


if __name__ == '__main__':
    print("Output in single line (1) or two-line (2) variant? ")
    print("Ex) set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports {CLK}];")
    print("Ex) set_property PACKAGE_PIN E3 [get_ports {CLK}];")
    print("    set_property IOSTANDARD LVCMOS33 [get_ports {CLK}];")

    variant = int(input("Variant (1, 2): "))

    print("Add pin/port name pair combinations")
    print("Tilde (~) to quit.")

    while True:
        pin = input("Pin: ")
        if pin == "~":
            process()

        name = input("Port name: ")
        if name == "~":
            process()

        pins.append(pin)
        names.append(name)
