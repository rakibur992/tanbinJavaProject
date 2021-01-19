/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LendingCompany;

import JavaClass.LendingCompany;
import JavaClass.Data;
import JavaClass.User;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;

/**
 * FXML Controller class
 *
 * @author Rakib
 */
public class AddHelicopterFXMLController implements Initializable {

    @FXML
    private TextField hModel;
    @FXML
    private TextField maxPassaengerCapacity;
    @FXML
    private TextField maxWeight;
    @FXML
    private DatePicker availableDate;
    

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        
        // TODO
    }    

    @FXML
    private void addBtn(ActionEvent event) {
//        String hdata=hModel.getText()+","+maxPassaengerCapacity.getText()+","+maxWeight.getText()+","+availableDate.getValue().toString()+","+totalDistance.getText();
        LendingCompany lc =(LendingCompany)Data.user;
        lc.addHelicopter(hModel.getText(), maxPassaengerCapacity.getText(), maxWeight.getText(), availableDate.getValue());
        Data.user=lc;
        System.out.println(availableDate.getValue());
       
        
        
        
    }
    
}
