/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package JavaClass;

import java.io.Serializable;
import java.time.LocalDate;

/**
 *
 * @author Rakib
 */
public class Helicopter implements  Serializable{
    public String model,maxPassCap,maxWeight;
    public  LocalDate availableDate;

    public Helicopter(String model,String maxPassCap,String maxWeight,LocalDate availableDate) {
        this.model=model;
        this.maxPassCap=maxPassCap;
        this.maxWeight=maxWeight;
        this.availableDate=availableDate;
    }

    public String getModel() {
        return model;
    }

    public String getMaxPassCap() {
        return maxPassCap;
    }

    public String getMaxWeight() {
        return maxWeight;
    }

    public LocalDate getAvailableDate() {
        return availableDate;
    }
    
    
    
    
}
