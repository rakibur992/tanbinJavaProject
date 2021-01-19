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
    public String model,maxPassCap,maxWeight,aDate;
    public  LocalDate availableDate;
    public Helicopter(String model,String maxPassCap,String maxWeight,LocalDate availableDate) {
        this.model=model;
        this.maxPassCap=maxPassCap;
        this.maxWeight=maxWeight;
        this.availableDate=availableDate;
    }
    public Helicopter(String model,String maxPassCap,String maxWeight,String aDate) {
        this.model=model;
        this.maxPassCap=maxPassCap;
        this.maxWeight=maxWeight;
        this.aDate=aDate;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public void setMaxPassCap(String maxPassCap) {
        this.maxPassCap = maxPassCap;
    }

    public void setMaxWeight(String maxWeight) {
        this.maxWeight = maxWeight;
    }

    public void setAvailableDate(LocalDate availableDate) {
        this.availableDate = availableDate;
    }

    public String getaDate() {
        return aDate;
    }

    public void setaDate(String aDate) {
        this.aDate = aDate;
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
