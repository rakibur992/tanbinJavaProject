/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package JavaClass;

import java.time.LocalDate;
import java.util.ArrayList;

/**
 *
 * @author Rakib
 */
public class Client extends User{
    private ArrayList<Booking>bookingList=new ArrayList<>();

    public ArrayList<Booking> getBookingList() {
        return bookingList;
    }

    public void addBooking(String model, String pickUpLoc, String destinationLoc, String time, LocalDate pickUpDate,String status) {
        Booking b=new Booking(model,pickUpLoc,destinationLoc,time,pickUpDate,status);
        bookingList.add(b);
    }
    
    public Client(String name, String userName, String pass, String email, String type) {
        super(name, userName, pass, email, type);
    }
    
}
