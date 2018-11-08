# VerilogUtils
Collection of small utilities to make programming in Verilog easier

## Boolean Algebra Converter

Converts 1/2/3/4-bit boolean algebra from a simple, typable format to valid Verilog code.

Spaces are converted to boolean AND "&" (multiplication), while plus signs are converted to boolean OR "|" (addition).

Inverted inputs are input as a', where a is the non-inverted input.

## Constraint Generator

Generates constraints for given port/pin combinations, in one-line (dictionary) format or in traditional two-property format.

Ex) `set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports {CLK}];`

Ex) ```
    set_property PACKAGE_PIN E3 [get_ports {CLK}];
    set_property IOSTANDARD LVCMOS33 [get_ports {CLK}];
    ```
    
Constraints are generated assuming LVCMOS33 I/O Standard (aka 3.3v).