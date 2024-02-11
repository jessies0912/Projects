package cp213;

/*

*/

import javax.swing.*;
import java.awt.*; 
import java.awt.event.*; 

public class VMGUI extends JFrame implements ActionListener {

// money in machine to start
private int bal_starting = 0; 
// total num of items
private int itemTot = 0;
public boolean exitAfter = false; 
							

private int Width = 450; // width of the interface.
private int Height = 725; //  height of the interface.

private JButton Buttons[]; // an array of all the buttons
private int i; // This is the integer I use for all of my for loops.
public VM Machine = new VM(bal_starting, exitAfter); // This creates a new machine in VM.java
public JLabel title = new JLabel("   Vending Machine");
public JLabel funds = new JLabel("   Balance: " + Machine.getBalFormat());


public VMGUI() 
{ 

	setTitle("Vending Machine"); //sets the title of the window
	Toolkit myTK = Toolkit.getDefaultToolkit();
	Dimension myD = myTK.getScreenSize();
	
	//sets the bounds to centralize the GUI
	setBounds((myD.width - Width)/2, (myD.height - Height)/2, Width, Height);

	// listen for the window being closed 
	addWindowListener(new WindowAdapter()
	{
		public void windowClosing(WindowEvent e) 
		{
			System.exit(0);
		} 
	}
	); 
	
	// GUI elements
	Buttons = new JButton[12]; //creating the GUI Button array with all the buttons
	Machine.Initialize(); // initializes the machine so that it automatically inputs prices.
	
	//for loop that creates the buttons with the correct names
	for (i = 0 ; i < 6 ; i++) 
	{ 
		Buttons[i] = new JButton(Machine.desc_get(i) + " for " + Machine.money_format(Machine.getPrice(i)));
		
	} 

	//creates the buttons that deal with inputting money and labels the buttons
	Buttons[6] = new JButton("10 Dollar");
	Buttons[7] = new JButton("Dollar");
	Buttons[8] = new JButton("Quarter");
	Buttons[9] = new JButton("Dime");
	Buttons[10] = new JButton("Nickel");
	Buttons[11] = new JButton("Get Change");

	//creates the content pane and then add all the buttons and labels
	Container pane = getContentPane(); 
	pane.setLayout(new GridLayout(7,2)); // grid style layout
	
	getContentPane().setBackground(Color.black);
	
	//setting both Jlabels opaque so that I could change the background to red
	title.setOpaque(true);
	funds.setOpaque(true);
	title.setBackground(Color.red);
	funds.setBackground(Color.red);
	
	// adds the buttons to the content pane and adds action listeners to all
	for(i = 0 ; i < 6; i++) 
	{  
		pane.add(Buttons[i]); // Add buttons to content pane 
		pane.add(Buttons[i+6]); // buttons alternate

		Buttons[i].addActionListener(this); 
		// add action listeners to the buttons
		Buttons[i+6].addActionListener(this);
	
	} 

	pane.add(funds); // This adds the Balance label to the content pane.
	pane.add(title); // This adds the title label to the content pane.

} 

public void actionPerformed(ActionEvent e) 
{
	// function that listens for whenever buttons are clicked
	boolean successful;
	Machine.Initialize();
	Object theButton = e.getSource();
	
	for(i = 6; i<12 ; i++) 
	{ 
		if(theButton == Buttons[i]) 
		{ // if Button is clicked then:
			switch(i) 
			{ 
				case 6: // the button called TenDollar, adds 10 bucks
					Machine.addFunds(1000); // So add 10 dollar 
					break; 
				case 7: // if clicked add 1 dollar
					Machine.addFunds(100); 
					break; 
				case 8: // if clicked add a quarter.
					Machine.addFunds(25); 
					break; // Stop
				case 9: // add dime
					Machine.addFunds(10); 
					break; 
				case 10: //add a nickel
					Machine.addFunds(5); // Add 5 cents.
					break; 
				case 11: // change return
					Machine.ReturnChange(); // Return change
					System.exit(0); // Exit 
			} 
		} 
	}
	// for loop to check if user is buying
	for(i = 0; i < 6; i++) 
	{ 
		if(theButton == Buttons[i]) 
		{ 
			successful = Machine.purchase_item(i); // Buy that item 
			if ((Machine.getCA() == true) || (successful == true)) 
			{
					itemTot = itemTot+1; //add item to the total count
			} 
		} 
	} 
	funds.setText("   Balance: " + VM.getBalFormat()+"\n    Total Items:"+ itemTot);
	
} // END actionPerformed(ActionEvent e)
} 