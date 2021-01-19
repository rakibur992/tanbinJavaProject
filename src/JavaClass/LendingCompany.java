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
public class LendingCompany extends User{
    public ArrayList<Helicopter>helicopteList=new ArrayList<>();
    
    public LendingCompany(String name, String userName, String pass, String email, String type) {
        super(name, userName, pass, email, type);
    }
    public void addHelicopter(String model,String maxPassCap,String maxWeight,LocalDate availableDate){
        Helicopter h =new Helicopter(model, maxPassCap, maxWeight,availableDate);
        helicopteList.add(h);
        System.out.println("dsad");
    }

}
