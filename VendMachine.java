package cp213;

import javax.swing.*; 

public class VendMachine { 

public static void main(String args[]) {
	// This is the first thing launched when we run the program.
	BuildMachine(); // This uses the "Build Machine" function
	//which goes down below and activates the JFrame so it is shown on the screen.
	// This Uses the VMGUI.class to do this.
} // END main(String args[])

public static void BuildMachine() {
	// This "Builds" the machine. It creates a new object called
	// VendingMachine which is a JFrame object, and shows it on the
	// screen.
	JFrame VendingMachine = new VMGUI();
	// Create new JFrame object, which utilizes the VMGUI.class and the VMGUI function
	VendingMachine.show(); // Show the vending machine jframe. Make it visible to the
	// user.
} // END BuildMachine()

} // END VendMachine 