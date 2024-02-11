package cp213;

import javax.swing.JOptionPane;

public class VM { //main class that is called in the main
		

//CONSTANTS
private static int balance; //  integer for user balance/funds

final static int worth_0 = 125;
final static int worth_1 = 125;
final static int worth_2 = 75;
final static int worth_3 = 295;
final static int worth_4 = 985;
final static int worth_5 = 305;

final static String item_0 = "Coke";
final static String item_1 = "Mountain Dew";
final static String item_2 = "KitKat";
final static String item_3 = "Doritos";
final static String item_4 = "Salad";
final static String item_5 = "SMART water";

						
private static boolean CA = false;
// when a user buys an item the program does not exit
//the program does not exit until the coin return button is pressed

private static int price_tag[] = new int[7]; // This array holds the prices of the items 
private static String item_desc[] = new String[6]; // This array holds the descriptions items 
private static int MaxLen = 0; 


public static void set_desc(int num_item, String theDescription) {
	// sets the description to the item number
	item_desc[num_item] = theDescription; 
} 


public static void setBal(int Balance) {
	// sets the balance to any integer in cents

	balance = Balance; 
} 


public static String desc_get(int num_item) {
	// gets the description given item number
	return item_desc[num_item]; 
} 

public VM(int myBalance, boolean exitAfter) { // initiating function.

	balance = myBalance; //initial balance
	CA = exitAfter;
	// sets the CA private variable to exitAfter variable.
}

public static boolean getCA() {
	return CA;
}

public static int getPrice(int num_item) {
	// return a price in an integer form.
	return price_tag[num_item]; 
} 

public static void price_set(int num_item, int thePrice) {
	// takes the item number and sets that item to a price.
	price_tag[num_item] = thePrice; // set the price of our item.
} 

public static boolean purchase_item(int num_item) {
	boolean val; // This is the boolean value to be returned.
	//buys an item from the inventory of the machine.
	
	// check if the balance that the user has is enough
	if (balance < getPrice(num_item)) 
	{
		//checks if the balance  is less than the cost
		Output("Not enough funds! Add more money.", 1);
		val = false; // buy not successful.
	} 

	else 
	{ // when there is enough money
		balance -= getPrice(num_item); //takes the amount of money spent out of the total funds
		Output("Purchased " + desc_get(num_item) + " for " + money_format(getPrice(num_item)), 1); // Tells the user
		
		val = true; // The buy was successful
	} 

	return val; 
}


public static void Output(String Message, int Type) {
	// takes a message to output in text form
	if (Type == 1) 
	{  // this checks the type of output
		JOptionPane.showMessageDialog(null, Message, "Vending Machine", JOptionPane.PLAIN_MESSAGE);
	} 
	else {
		
	} 
} 


public static String getBalFormat() {
	//formats the balance
	return money_format(balance);
} 

public static int getBalance() {
	return balance; // Return the balance.
} 

public static void addFunds(int Amount) {
	//  adds money to the machine
	balance = balance + Amount; 
} 

public static void Initialize() {
	// initializes the machine so that everything is more organized
	int i = 0; 
	String Desc = null; 
	
    set_desc(0, item_0);
    set_desc(1, item_1);
    set_desc(2, item_2);
    set_desc(3, item_3);
    set_desc(4, item_4);
    set_desc(5, item_5);
    // set the prices for these items.
    price_set(0, worth_0);
    price_set(1, worth_1);
    price_set(2, worth_2);
    price_set(3, worth_3);
    price_set(4, worth_4);
    price_set(5, worth_5);
   
    for(i = 0 ; i < 6; i++) 
    {
		Desc = desc_get(i); // Gets the description of the current one.
		if (Desc.length() > MaxLen) 
		{ 
			MaxLen = desc_get(i).length(); // Set the new max length.
		} 
	} 
} 

public static String money_format (int Money) { 
    int dollars = 0; 
    int cents = 0; 
    int tens = 0; 
	int one = 0; 
	
    String frmted = null; 
    dollars = Money / 100; // Returns how many dollars we have here.
   
    cents = Money % 100; // gets the remainder
    tens = cents / 10; // gets the tens place of our total.
    one = cents % 10; // gets the ones place of our total.
    // String that has the format: $_.__
    frmted = "$" + dollars + "." + tens + one;
    return frmted; 
 
}
public static void ReturnChange() {
	// returns change
	int total_val = getBalance(); 
	
	int dollars = 0; // dolars
	int Quarters = 0; // Quarters
	int Dimes = 0; // Dimes
	int Nickels = 0;  // Nickels
	
	dollars = total_val / 100; // integer division for the number of dollars
	
	total_val -= (100 * dollars); 
	Quarters = total_val / 25; 
	total_val -= (25 * Quarters);
	Dimes = total_val / 10; 
	total_val -= (10 * Dimes); 
	Nickels = total_val / 5; 
	total_val -= (5 * Nickels); 

	// If the total remainder is not zero there is somehow pennies in the machine
	if (!(total_val == 0)) 
	{ 
		Output("Error try again", 1);
	} 

	Output("\nYour change is: \n" + dollars + " dollars\n" + Quarters + " Quarters\n" + Dimes + " Dimes\n" + Nickels + " Nickels\n" + "For a total of " + money_format(getBalance()) ,1);

	setBal(0); // Clear the balance.

} 
} 