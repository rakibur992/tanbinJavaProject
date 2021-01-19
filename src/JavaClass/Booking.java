/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package JavaClass;

import java.time.LocalDate;

/**
 *
 * @author Rakib
 */
public class Booking {
    private LocalDate pickUpDate;
    private String model,pickUpLoc,destinationLoc,time,status;
    
    public Booking(String model, String pickUpLoc, String destinationLoc, String time, LocalDate pickUpDate,String status) {
        this.model = model;
        this.pickUpLoc = pickUpLoc;
        this.destinationLoc = destinationLoc;
        this.time = time;
        this.pickUpDate = pickUpDate;
        this.status= status;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getPickUpLoc() {
        return pickUpLoc;
    }

    public void setPickUpLoc(String pickUpLoc) {
        this.pickUpLoc = pickUpLoc;
    }

    public String getDestinationLoc() {
        return destinationLoc;
    }

    public void setDestinationLoc(String destinationLoc) {
        this.destinationLoc = destinationLoc;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public LocalDate getPickUpDate() {
        return pickUpDate;
    }

    public void setPickUpDate(LocalDate pickUpDate) {
        this.pickUpDate = pickUpDate;
    }

    
    
}
